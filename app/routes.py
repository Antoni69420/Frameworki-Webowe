from flask import Blueprint, jsonify, request, abort
from app.storage import UsersStorage

users_bp = Blueprint("users", __name__)
storage = UsersStorage()


@users_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify(storage.get_all()), 200


@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = storage.get_by_id(user_id)
    if not user:
        abort(400)
    return jsonify(user), 200


@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "lastname" not in data:
        abort(400)
    storage.create(data["name"], data["lastname"])
    return "", 201


@users_bp.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):
    data = request.get_json()
    if not data or not set(data.keys()).issubset({"name", "lastname"}):
        abort(400)
    if not storage.patch(user_id, data):
        abort(400)
    return "", 204


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def put_user(user_id):
    data = request.get_json()
    if not data or "name" not in data or "lastname" not in data:
        abort(400)
    storage.update(user_id, data["name"], data["lastname"])
    return "", 204


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not storage.delete(user_id):
        abort(400)
    return "", 204
