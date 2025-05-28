from flask import Blueprint, request, jsonify

user_routes_bp = Blueprint("user_routes", __name__)

from src.views.user_view import UserView
from driver.db_connector import DBConnector
from driver.paths import DB_PATH


db_connector = DBConnector(db_path=DB_PATH)

@user_routes_bp.route('/rota/user/post', methods=["POST"])
def func_user_post():
    body = request.get_json()
    view = UserView(db_connector=db_connector)

    http_response = view.handle_register_user(body)

    return jsonify(http_response)

@user_routes_bp.route('/rota/user/get', methods=["GET"])
def func_user_get():
    name = request.args.get("name")
    view = UserView(db_connector=db_connector)

    http_response = view.handle_get_user(name)

    return jsonify(http_response)
