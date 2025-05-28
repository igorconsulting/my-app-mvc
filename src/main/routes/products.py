from flask import Blueprint, request, jsonify

user_routes_bp = Blueprint("product_routes", __name__)

from src.views.product_register_view import ProductRegisterView

@user_routes_bp.route('/rota/product/post', methods=["POST"])
def func_product_post():
    body = request.get_json()
    view = ProductRegisterView()

    http_reponse = view.handle_register_user(body)

    return jsonify(http_reponse)
