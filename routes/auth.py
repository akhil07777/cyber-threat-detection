from flask import request, jsonify, session, redirect, url_for
from database.db import users_collection


def register_user():

    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # Check if email already exists
    existing_user = users_collection.find_one({
        "email": email
    })

    if existing_user:
        return jsonify({
            "success": False,
            "message": "Email already exists"
        })

    # Insert new user
    users_collection.insert_one({
        "name": name,
        "email": email,
        "password": password
    })

    return jsonify({
        "success": True,
        "message": "User registered successfully"
    })


def login_user():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    user = users_collection.find_one({
        "email": email,
        "password": password
    })

    if user:

        session["email"] = user["email"]
        session["name"] = user["name"]

        return jsonify({
            "success": True,
            "message": "Login Successful",
            "name": user["name"],
            "email": user["email"]
        })

    return jsonify({
        "success": False,
        "message": "Invalid Email or Password"
    })


def logout_user():

    session.clear()

    return redirect(url_for("home"))