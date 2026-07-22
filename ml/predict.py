import joblib
import pandas as pd

# Load trained model
model = joblib.load("ml/model.pkl")

# Load encoders
encoders = joblib.load("ml/encoders.pkl")


def predict_attack(row):

    # Make a copy
    data = row.copy()

    # Encode categorical features
    categorical_columns = [
        "protocol_type",
        "service",
        "flag"
    ]

    for column in categorical_columns:

        if data[column] in encoders[column].classes_:
            data[column] = encoders[column].transform([data[column]])[0]
        else:
            # Unknown category
            data[column] = 0

    # Convert to DataFrame
    sample = pd.DataFrame([data])

    # Prediction
    prediction = model.predict(sample)[0]

    # Confidence
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