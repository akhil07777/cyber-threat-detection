from flask import jsonify, session
from database.db import reports_collection, uploads_collection


def dashboard_data():

    email = session.get("email")

    total = reports_collection.count_documents({
        "email": email
    })

    attack = reports_collection.count_documents({
        "email": email,
        "prediction": "Attack"
    })

    normal = reports_collection.count_documents({
        "email": email,
        "prediction": "Normal"
    })

    recent_uploads = []

    uploads = uploads_collection.find({
        "email": email
    }).sort("_id", -1).limit(5)

    for upload in uploads:

        if upload["attack_count"] > 0:
            status = "Threats Found"
        else:
            status = "Normal"

        recent_uploads.append({

            "_id": str(upload["_id"]),

            "filename": upload["filename"],

            "date": upload["upload_time"],

            "attack": upload["attack_count"],

            "status": status

        })

    return jsonify({

        "total": total,

        "attack": attack,

        "normal": normal,


        "recent": recent_uploads

    })
