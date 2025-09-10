from flask import Blueprint, request, jsonify
from app.services import user_service

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_users():
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
    except ValueError:
        return jsonify({"error": {"message": "'page' and 'page_size' must be integers."}}), 400

    page = max(1, page)
    page_size = max(1, min(page_size, 50))

    q = request.args.get('q')
    role = request.args.get('role')
    is_active = request.args.get('is_active')

    print(f"[INFO] GET /users?page={page}&page_size={page_size}&q={q}&role={role}&is_active={is_active}")

    result = user_service.find_users(
        page=page,
        page_size=page_size,
        q=q,
        role=role,
        is_active=is_active
    )
    
    return jsonify(result), 200

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    print(f"[INFO] GET /users/{user_id}")
    user = user_service.find_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    
    return jsonify({"error": {"message": "User not found"}}), 404
