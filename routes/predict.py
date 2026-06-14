from flask import request
from flask import jsonify

from ml.predict import predict_attack

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

    return jsonify({
        "prediction": prediction
    })