from flask import jsonify, session
from database.db import uploads_collection


def get_reports():

    email = session.get("email")

    reports = []

    uploads = uploads_collection.find(
        {
            "email": email
        }
    ).sort("_id", -1)

    for upload in uploads:

        if upload.get("attack_count", 0) > 0:
            status = "Threats Found"
        else:
            status = "Normal"

        reports.append({

            "_id": str(upload["_id"]),

            "filename": upload.get("filename", "Unknown"),

            "date": upload.get("upload_time", ""),

            "status": status,

            "total_records": upload.get("total_records", 0),

            "attack_count": upload.get("attack_count", 0),

            "normal_count": upload.get("normal_count", 0)

        })

    return jsonify(reports)