from flask import Blueprint,jsonify, request, make_response
from BLL.user_bl import UserBL


usr = Blueprint('user', __name__)
users_bl = UserBL()


# @usr.route("/", methods=['GET'])
# def get_employees():
#     exist,user_fullName,autorized = condition_jwt()
#     if exist==True:
#         empObj = employee_bl.get_all_employee(user_fullName)
#         for emp in empObj:
#             if "Error" in emp:
#                 return make_response(emp,400)
#         return make_response(jsonify(empObj),200)
#     elif autorized == False: 
#         return make_response({"Error_autorized":"You have reach the max number of Actions for today"},401)
#     else:
#         return make_response({"Error":"Not authorized"},401)
    

# @usr.route("/<id>", methods=['GET'])
# def get_employees_by_id(id):
#     exist,user_fullName,autorized = condition_jwt()
#     if exist==True:
#         empObj = employee_bl.get_employee_by_id(id)
#         for emp in empObj:
#             if "Error" in emp:
#                 return make_response(emp,400)
#         return make_response(jsonify(empObj),200)
#     elif autorized == False: 
#         return make_response({"Error_autorized":"You have reach the max number of Actions for today"},401)
#     else:
#         return make_response({"Error":"Not authorized"},401)
    

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

# @usr.route("/<id>",methods=['PUT'])
# def update_emploee(id):
#     exist,user_fullName,autorized = condition_jwt()
#     if exist==True:
#         obj = request.json
#         result = employee_bl.update_employee(id,obj)
#         for res in result:
#             if "Error" in res:
#                 return make_response(res,400)
#         return make_response(jsonify(result),200)
#     elif autorized == False: 
#         return make_response({"Error_autorized":"You have reach the max number of Actions for today"},401)
#     else:
#         return make_response({"Error":"Not authorized"},401)


# @usr.route("/<id>",methods=['DELETE'])
# def delete_emp(id):
#     exist,user_fullName,autorized = condition_jwt()
#     if exist==True:
#         result = employee_bl.delete_employee(id)
#         for res in result:
#             if "Error" in res:
#                 return make_response(res,400)
#         return make_response(jsonify(result),200)
#     elif autorized == False: 
#         return make_response({"Error_autorized":"You have reach the max number of Actions for today"},401)
#     else:
#         return make_response({"Error":"Not authorized"},401)