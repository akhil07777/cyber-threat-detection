from flask import request
from flask import jsonify

from ml.predict import predict_attack
from database.db import reports_collection
from datetime import datetime

def predict_route():

    data = request.json

    duration = data["duration"]

    src_bytes = data["src_bytes"]

    dst_bytes = data["dst_bytes"]

    prediction = predict_attack(
        duration,
        src_bytes,
        dst_bytes
    )
    reports_collection.insert_one({

    "duration": duration,

    "src_bytes": src_bytes,

    "dst_bytes": dst_bytes,

    "prediction": prediction,

    "time": datetime.now()

})
    return jsonify({
        "prediction": prediction
    })
import joblib
import pandas as pd

model = joblib.load("ml/model.pkl")
encoders = joblib.load("ml/encoders.pkl")


def predict_attack(row):

    data = row.copy()

    categorical_columns = [
        "protocol_type",
        "service",
        "flag"
    ]

    for column in categorical_columns:

        if data[column] in encoders[column].classes_:
            data[column] = encoders[column].transform([data[column]])[0]
        else:
            data[column] = 0

    sample = pd.DataFrame([data])

    prediction = model.predict(sample)[0]

    probabilities = model.predict_proba(sample)[0]

    confidence = round(max(probabilities) * 100, 2)

    if prediction == 0:

        prediction_text = "Normal"
        risk = "Low"

    else:

        prediction_text = "Attack"

        if confidence >= 95:
            risk = "Critical"

        elif confidence >= 85:
            risk = "High"

        elif confidence >= 70:
            risk = "Medium"

        else:
            risk = "Low"

    return {
        "prediction": prediction_text,
        "confidence": confidence,
        "risk": risk
    }