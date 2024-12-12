from DAL.my_community_db_dal import MyCommunityDBDal
from datetime import date
class UserBL:
    def __init__(self):
        self.__mycommunity_db_dal=MyCommunityDBDal()
    
               
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
                elif str(usr["email"])==str(obj_dict["email"] or usr["appName"])==obj_dict["appName"]: 
                    result =  [{"Error": "There is an user with the same name"}]
        print('insert_new_employee')
        result = self.__mycommunity_db_dal.insert_new_employee(obj_dict)
        print(result)
        return result