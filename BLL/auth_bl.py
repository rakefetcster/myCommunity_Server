import jwt
from DAL.my_community_db_dal import MyCommunityDBDal

class AuthBL:
    def __init__(self):
        self.__key = "server_my_community"
        self.__algorithm = "HS256"
        self.__mycommunity_db_dal = MyCommunityDBDal()
    
    def get_token(self,username,password):
        user_Obj = self.__check_user(username,password)
        print(user_Obj)
        token=None
        if user_Obj is not None:
            token=jwt.encode({"userid":str(user_Obj['_id'])},self.__key,self.__algorithm)
        return token,user_Obj['appName']
      
    def verify_token(self,token):
        data = jwt.decode(token, self.__key,self.__algorithm)
        user_id = data["userid"]
        this_user_obj = self.__mycommunity_db_dal.get_user_by_id({"id":user_id})
        if this_user_obj == []:
            return False
        else:
            return True
      
    def __check_user(self,username,password):
        res_list = self.logIn_user(username,password)
        if "Error" in res_list:
            return res_list
        else:
            return res_list
    
    def logIn_user(self,username,password):
        obj_dict = {"email":username,"password": password}
        this_user_obj = self.__mycommunity_db_dal.get_user_email(obj_dict)
        print(this_user_obj)
        if this_user_obj == []:
            return [{"Error": "The user was not found"}]
        for this_user in this_user_obj:
            if "Error" in this_user:
                return [{"Error": "The user was not found"}]
            elif this_user["password"] == obj_dict["password"] and this_user["email"] == obj_dict["email"]:
                return this_user
            else:
                return [{"Error": "The password is incorrect"}]
            
    def add_new_user(self,usrObj):
        obj_dict = dict()
        obj_dict = {"appName":usrObj["appName"],"email":usrObj["email"],"password": usrObj["password"]}
        users_from_db = self.__mycommunity_db_dal.get_all_users()
        print('users_from_db:')
        print(users_from_db)
        result = []
        if users_from_db != []:
            for usr in users_from_db:
                if "Error" in usr:
                    print('Error')
                    result = [usr]
                elif str(usr["email"])==str(obj_dict["email"] or usr["appName"])==str(obj_dict["appName"]): 
                    result =  [{"Error": "There is an user with the same name"}]
              
            
        print('insert_new_employee')
        result = self.__mycommunity_db_dal.insert_new_employee(obj_dict)
        print(result)
        return result