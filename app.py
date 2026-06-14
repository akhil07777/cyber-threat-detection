from flask import Flask
from routes.auth import register_user
from routes.auth import login_user
from routes.predict import predict_route

app = Flask(__name__)


@app.route("/")
def home():
    return "Cyber Threat Detection Project Running"


@app.route("/register", methods=["POST"])
def register():
    return register_user()


@app.route("/login", methods=["POST"])
def login():
    return login_user()

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    return predict_route()


if __name__ == "__main__":
    app.run(debug=True)