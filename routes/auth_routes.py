from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required
from utils.validation import validate_registration_data
from services.auth_service import register_user,login_user,view_profile
auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['POST'])
def register():
    data=request.get_json()
    result = validate_registration_data(data)
    if not result['success']:
        return jsonify(result),400
    result = register_user(data)
    return jsonify(result),200

@auth_bp.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    result= login_user(data)
    if not result['success']:
        return jsonify(result),400
    return jsonify(result),200

@auth_bp.route('/profile', methods=["GET"])
@jwt_required()
def profile():
    result,status=view_profile()
    return jsonify(result),status
