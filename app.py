from flask import Flask, render_template, session, redirect

from routes.auth import register_user, login_user, logout_user
from routes.predict import predict_route
from routes.report import get_reports
from routes.dashboard import dashboard_data
from routes.upload import upload_csv
from routes.view_report import view_report

app = Flask(__name__)

# Secret key required for Flask sessions
app.secret_key = "cyber_threat_detection_2026"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/register-page")
def register_page():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():

    if "email" not in session:
        return redirect("/")

    return render_template("dashboard.html")


@app.route("/upload")
def upload():

    if "email" not in session:
        return redirect("/")

    return render_template("upload.html")


@app.route("/reports")
def reports():

    if "email" not in session:
        return redirect("/")

    return render_template("reports.html")


@app.route("/upload-csv", methods=["POST"])
def upload_csv_route():

    if "email" not in session:
        return redirect("/")

    return upload_csv()


@app.route("/reports-data")
def reports_data():

    if "email" not in session:
        return redirect("/")

    return get_reports()


@app.route("/dashboard-data")
def dashboard_api():

    if "email" not in session:
        return redirect("/")

    return dashboard_data()


@app.route("/register", methods=["POST"])
def register():
    return register_user()


@app.route("/login", methods=["POST"])
def login():
    return login_user()


@app.route("/logout")
def logout():
    return logout_user()


@app.route("/predict", methods=["POST"])
def predict():

    if "email" not in session:
        return redirect("/")

    return predict_route()


@app.route("/view-report/<report_id>")
def report_details(report_id):

    if "email" not in session:
        return redirect("/")

    return view_report(report_id)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
