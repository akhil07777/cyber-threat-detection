from flask import render_template, session
from bson import ObjectId

from database.db import uploads_collection, reports_collection


def view_report(report_id):

    email = session.get("email")

    # Get upload details only for the logged-in user
    report = uploads_collection.find_one({
        "_id": ObjectId(report_id),
        "email": email
    })

    if not report:
        return "Report not found or Access Denied", 404

    # Get prediction records only for this user and this upload
    predictions = list(

        reports_collection.find(

            {
                "upload_id": report_id,
                "email": email
            },

            {
                "_id": 0
            }

        )

    )

    return render_template(

        "report_details.html",

        report=report,

        predictions=predictions

    )