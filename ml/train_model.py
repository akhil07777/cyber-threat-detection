import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# -------------------------------
# NSL-KDD Column Names
# -------------------------------

column_names = [
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

# -------------------------------
# Read Dataset
# -------------------------------

data = pd.read_csv(
    "dataset/KDDTrain+.txt",
    header=None,
    names=column_names
)

# -------------------------------
# Separate Features and Label
# -------------------------------

X = data.drop(columns=["label", "difficulty"])

y = data["label"]

# -------------------------------
# Binary Classification
# normal = 0
# attack = 1
# -------------------------------

y = y.apply(lambda x: 0 if x == "normal" else 1)

# -------------------------------
# Encode Categorical Columns
# -------------------------------

encoders = {}

categorical_columns = [
    "protocol_type",
    "service",
    "flag"
]

for column in categorical_columns:
    encoder = LabelEncoder()
    X[column] = encoder.fit_transform(X[column])
    encoders[column] = encoder

# -------------------------------
# Train Model
# -------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# -------------------------------
# Save Files
# -------------------------------

joblib.dump(model, "ml/model.pkl")
joblib.dump(encoders, "ml/encoders.pkl")

print("Model trained successfully.")
print("Model saved as model.pkl")
print("Encoders saved as encoders.pkl")