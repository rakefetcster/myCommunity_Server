import jwt
from DAL.my_community_db_dal import MyCommunityDBDal
from DAL.kafka_producer import ProducerDal
class AuthBL:
    def __init__(self):
        self.__key = "server_my_community"
        self.__algorithm = "HS256"
        self.__mycommunity_db_dal = MyCommunityDBDal()
        self.__kafka_db_dal = ProducerDal("users")
    
    def get_token(self,username,password):
        this_full_user = self.__check_user(username,password)
        token=None
        if this_full_user is not None:
            token=jwt.encode({"userid": str(this_full_user["_id"])},self.__key,self.__algorithm)
        return token,this_full_user["appName"]
      
    def verify_token(self,token):
        data = jwt.decode(token, self.__key,self.__algorithm)
        user_id = data["userid"]
        this_user_obj = self.__mycommunity_db_dal.get_user_by_id({"id":user_id})
        if this_user_obj == []:
            return False
        else:
            return True
      
    def __check_user(self,username,password):
        this_full_user = self.logIn_user(username,password)
        if "Error" in this_full_user:
            return this_full_user
        else:
            return this_full_user
    
    def logIn_user(self,username,password):
        obj_dict = {"email":username,"password": password}
        #db
        this_user_obj = self.__mycommunity_db_dal.get_user_email(obj_dict)
        if this_user_obj == []:
            return [{"Error": "The user was not found"}]
        for this_full_user in this_user_obj:
            if "Error" in this_full_user:
                return [{"Error": "The user was not found"}]
            elif this_full_user["password"] == obj_dict["password"] and this_full_user["email"] == obj_dict["email"]:
                return this_full_user
            else:
                return [{"Error": "The password is incorrect"}]
            
    def add_new_user(self,usrObj):
        obj_dict = dict()
        obj_dict = {"appName":usrObj["appName"],"email":usrObj["email"],"password": usrObj["password"]}
        users_from_db = self.__mycommunity_db_dal.get_all_users()
        result = []
        if users_from_db != []:
            for usr in users_from_db:
                if "Error" in usr:
                    print('Error')
                    result = [usr]
                elif str(usr["email"])==str(obj_dict["email"] or usr["appName"])==str(obj_dict["appName"]): 
                    result =  [{"Error": "There is an user with the same name"}]
              
            
        result = self.__mycommunity_db_dal.insert_new_employee(obj_dict)
        return result