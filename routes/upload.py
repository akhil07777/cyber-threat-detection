import os
import pandas as pd

from flask import request, jsonify, session

from ml.predict import predict_attack
from database.db import reports_collection, uploads_collection

UPLOAD_FOLDER = "uploads"

# NSL-KDD column names
COLUMN_NAMES = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes",
    "land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted",
    "num_root","num_file_creations","num_shells","num_access_files",
    "num_outbound_cmds","is_host_login","is_guest_login","count",
    "srv_count","serror_rate","srv_serror_rate","rerror_rate",
    "srv_rerror_rate","same_srv_rate","diff_srv_rate",
    "srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
    "dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "label","difficulty"
]


def upload_csv():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "message": "No file uploaded"
        })

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected"
        })

    if not file.filename.lower().endswith(".csv"):
        return jsonify({
            "success": False,
            "message": "Please upload a CSV file."
        })

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        data = pd.read_csv(
            filepath,
            header=None,
            names=COLUMN_NAMES,
            low_memory=False
        )

    except Exception:
        return jsonify({
            "success": False,
            "message": "Unable to read the CSV file."
        })

    # Remove label & difficulty before prediction
    features = data.drop(
        ["label", "difficulty"],
        axis=1
    )

    predictions = []

    attack_count = 0
    normal_count = 0

    # Create upload record first
    upload_result = uploads_collection.insert_one({

        "filename": file.filename,

        "email": session.get("email", "Unknown"),

        "upload_time": pd.Timestamp.now().strftime("%d-%m-%Y %H:%M"),

        "total_records": 0,

        "attack_count": 0,

        "normal_count": 0,

        "status": "Completed"

    })

    upload_id = str(upload_result.inserted_id)

    # Process every row
    for index, row in features.iterrows():

        result = predict_attack(row)

        report = row.to_dict()
        report["upload_id"] = upload_id
        report["email"] = session["email"]
        report["prediction"] = result["prediction"]
        report["confidence"] = result["confidence"]
        report["risk"] = result["risk"]
        reports_collection.insert_one(report)

        if result["prediction"] == "Attack":
            attack_count += 1
        else:
            normal_count += 1

        predictions.append({

            "id": index + 1,
            "protocol": row["protocol_type"],
            "service": row["service"],
            "prediction": result["prediction"],
            "confidence": result["confidence"],
            "risk": result["risk"]

        })

    # Update upload summary
    uploads_collection.update_one(

        {
            "_id": upload_result.inserted_id
        },

        {
            "$set": {

                "total_records": len(predictions),
                "attack_count": attack_count,
                "normal_count": normal_count

            }
        }

    )

    os.remove(filepath)

    return jsonify({

        "success": True,
        "message": "CSV uploaded and analyzed successfully.",
        "rows": len(predictions),
        "results": predictions

    })