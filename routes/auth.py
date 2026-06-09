from flask import request, jsonify
from database.db import users_collection


def register_user():

    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    existing_user = users_collection.find_one(
        {"email": email}
    )

    if existing_user:
        return jsonify(
            {"message": "Email already exists"}
        )

    users_collection.insert_one({
        "name": name,
        "email": email,
        "password": password
    })

    return jsonify(
        {"message": "User registered successfully"}
    )
def login_user():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    user = users_collection.find_one({
        "email": email,
        "password": password
    })

    if user:
        return jsonify(
            {"message": "Login Successful"}
        )

    return jsonify(
        {"message": "Invalid Credentials"}
    )