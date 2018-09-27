from flask import request, jsonify, Blueprint
from api.models import User
import re
from werkzeug.security import generate_password_hash

user = Blueprint('user', __name__)

users = []


@user.route('/api/v1/signup', methods=['POST'])
def register_user():
    data = request.get_json()
    if len(data.keys()) == 0:
        return jsonify({"message": "No user added"}), 400

    if data['user_name'] == "":
        return jsonify({"message": "username cannot be blank"}), 400

    if data['email'] == "":
        return jsonify({"message": "Email cannot be blank"}), 400

    if data['password'] == "":
        return jsonify({"message": "password cannot be blank"}), 400

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", data['email']):
        return jsonify({"message": "Invalid email format"}), 400

    if not re.match(r"([a-zA-Z0-9])", data['user_name']):
        return jsonify({
            "message": "Please enter alphanumerical characters for username"
            }), 400

    if re.match(r"([0-9])", data['user_name']):
        return jsonify({
            "message": "user name cannot contain numbers only"}), 400

    if len(data['password']) < 5:
        return jsonify({"message": "Password too short"}), 400

    for user in users:
        if user.email == data['email']:
            return jsonify({"message": "user already exists!"})

    if isinstance(data['user_name'], str):
        user_id = len(users)
        user_id += 1
        hashed_password = generate_password_hash(data['password'],
                                                 method='sha256')
        user = User(user_id, data['user_name'], data['email'], hashed_password)
        users.append(user)
        return jsonify({"message": "User added successfully"}), 201
    return jsonify({"message": "Invalid fields"}), 400
