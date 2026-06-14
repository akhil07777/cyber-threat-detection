import joblib

model = joblib.load(
    "ml/model.pkl"
)

def predict_attack(
        duration,
        src_bytes,
        dst_bytes
):

    result = model.predict(
        [[
            duration,
            src_bytes,
            dst_bytes
        ]]
    )

    if result[0] == 0:
        return "Normal"

    return "Attack"