from flask import Blueprint,jsonify, request, make_response
from BLL.user_bl import UserBL


usr = Blueprint('user', __name__)
users_bl = UserBL()
 

@usr.route("/", methods=['POST'])
def post_user():
    usrObj=request.json
    print(usrObj["byKey"])
    if usrObj["byKey"]=='signUp':
        result = users_bl.add_new_user(usrObj)
        print(result)
        print(jsonify(result))
    elif usrObj["byKey"]=='logIn':
        result = users_bl.logIn_user(usrObj)
    print(result)  
    return jsonify(result)   