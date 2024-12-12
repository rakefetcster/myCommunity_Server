
from pymongo import MongoClient
from bson import ObjectId

class MyCommunityDBDal:
    def __init__(self):
        self.__client = MongoClient("mongodb://localhost:27017")
        self.__db = self.__client["mycommunity"]
        self.__collection_users = self.__db["users"]

    def get_all_users(self):
        result_list = list()
        try:
            result_list = list(self.__collection_users.find({}))
            return result_list
        except Exception as e:
            return [{"Error":"An error occurred, func get_all_users"}]
    
    def get_user_by_id(self,id):
        try:
            result_list = list(self.__collection_users.find({"id":ObjectId(id)})) 
            return result_list
        except Exception as e:
            return []
            
    def get_user_email(self,userObj):
        try:
            print(userObj["email"])
            result_list = list(self.__collection_users.find({"email":str(userObj["email"])})) 
            return result_list
        except Exception as e:
            return [{"Error":"An error occurred"}]
            
    def insert_new_employee(self,userObj):
        try:
            self.__collection_users.insert_one(userObj) 
            print("Success: created with id:"+str(userObj["_id"]))
            return "Created with id: "+ str(userObj["_id"])
        except Exception as e:
            return [{"Error":"An error occurred insert_new_employee"}]
