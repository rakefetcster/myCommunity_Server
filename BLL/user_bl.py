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

    # def update_employee(self,id,obj):
    #     if "shifts" in obj:
    #         result = self.update_emp_shift(id,obj)
    #         if "Error" in result:
    #             return result
    #     dep_id = ''
    #     new_obj = dict()
    #     res = False
    #     this_id_list = list()
    #     if "departmentName" in obj:
    #         department = self.__mycommunity_db_dal.get_all_departments()
    #         for dep in department:
    #             if "Error" in dep:
    #                 return dep
    #             elif str(dep["Name"]) == obj["departmentName"]:
    #                 res = True
    #                 obj["departmentId"] = str(dep["_id"])
    #                 break

    #     elif "department" in obj:
    #         department = self.__mycommunity_db_dal.get_all_departments()
    #         for dep in department:
    #             if "Error" in dep:
    #                 return dep
    #             if str(dep["_id"]) == obj["department"]:
    #                 res = True
    #                 obj["departmentId"] = str(dep["_id"])
    #                 break
    #     if res:
    #         result = self.__mycommunity_db_dal.update_employee(id,obj)
    #         return result
    #     else:        
    #         return [{"Error":" The department was not created - the employee cannot be updated"}]

    # def update_emp_shift(self,id,obj):
    #     if len(obj["shifts"])==0:
    #         result = self.__mycommunity_db_dal.insert_shift_to_emp(id,obj["shifts"])
    #         return result
    #     if len(obj["shifts"]) == 1:
    #         this_id =obj["shifts"][0] 
    #         result = self.__mycommunity_db_dal.insert_shift_to_emp(id,this_id)
    #     elif len(obj["shifts"]) > 1:
    #         for shiftId in obj["shifts"]:
    #             result = self.__mycommunity_db_dal.insert_all_shift(id,shiftId)
    #             if "Error" in result:
    #                 return result
                
     
    # def delete_employee(self,id):
    #     result_str=''
    #     #delete the shifts
    #     result1 = self.__mycommunity_db_dal.delete_shifts_of_emp(id)
    #     #delete the manager from the department
    #     result2 = self.__mycommunity_db_dal.delete_manager_from_departments(id)
    #     #delete employee
    #     result = self.__mycommunity_db_dal.delete_this_employee(id)
    #     for res in result:
    #         if "Error" in res:
    #             return result  
    #         else:
    #             result_str += res["Success"]+"-"
    #     for res in result1:
    #         if "Error" in res:
    #             return result1 
    #         else:
    #             result_str += res["Success"]+"-"
    #     for res in result2:
    #         if "Error" in res:
    #             return result2 
    #         else:
    #             result_str += res["Success"]    
    #     return [{"Success":result_str}]