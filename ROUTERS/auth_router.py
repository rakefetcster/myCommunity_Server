from flask import Blueprint, request,make_response
from BLL.auth_bl import AuthBL

auth = Blueprint('auth',__name__)
auth_bl = AuthBL()

@auth.route("/login", methods=['POST'])
def logIn():
    username = request.json["username"]
    password = request.json["password"]
    token = None
    token,appName = auth_bl.get_token(username,password)
    if token is not None:
        return make_response({"token":token,"appName":appName},200)
    else:
        return make_response({"error":"You are not authorized"},401)
    
