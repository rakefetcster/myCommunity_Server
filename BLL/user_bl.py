from asyncio.windows_events import NULL
from DAL.my_community_db_dal import MyCommunityDBDal
from datetime import date

class UserBL:
    def __init__(self):
        self.__mycommunity_db_dal=MyCommunityDBDal()

    # def get_all_employee(self,user_fullName):     
    #     employee_from_db = self.__mycommunity_db_dal.get_all_employee()
    #     emp_list = list()
    #     for employee in employee_from_db:
    #         if "Error" in employee:
    #             return employee_from_db
    #         else:
    #             shift_list = list()
    #             emp_dict = dict()
    #             shift_emp = ''
    #             if "departmentId" in employee:
    #                 department = self.__mycommunity_db_dal.get_one_department(employee["departmentId"])
                    
    #                 emp_dict.update({"departmentId": employee["departmentId"]})
    #                 if "Error" in department:
    #                     return [department]
    #                 elif department != None:
    #                     emp_dict.update({"Department":department["Name"]})  
    #             shift_emp = self.__mycommunity_db_dal.get_shift_emp_by_empId(employee["_id"])       
    #             for shiftId in shift_emp:
    #                 if "Error" in shiftId:
    #                     return [shiftId]
    #                 this_shift = self.__mycommunity_db_dal.get_one_shift(shiftId["shiftId"])
    #                 if "Error" in this_shift:
    #                     return [this_shift]
    #                 date = str(this_shift["date"].day)+"/"+str(this_shift["date"].month)+"/"+str(this_shift["date"].year)
    #                 shift_list.append({
    #                     "id": this_shift["_id"],
    #                     "date":date,
    #                     "starting_hour":this_shift["starting_hour"],
    #                     "ending_hour":this_shift["ending_hour"]
    #                 })
    #             emp_dict.update({
    #                 "id": employee["_id"],
    #                 "FirstName": employee["FirstName"],
    #                     "LastName" : employee["LastName"],
    #                     "StartWorkYear":employee["StartWorkYear"],
    #                     "shifts":shift_list,
    #                     "user_name":user_fullName
                        
    #                     })
    #             emp_list.append(emp_dict)
    #     return emp_list
        
    
    # def get_employee_by_id(self,id):
    #     dep_name = ''
    #     emp_dict = dict()
    #     shift_list = list()
    #     employee = self.__mycommunity_db_dal.get_one_employee(id)
    #     if "Error" in employee:
    #         return [employee]
    #     if "departmentId" in employee:
    #         department = self.__mycommunity_db_dal.get_one_department(employee["departmentId"])
    #         if "Error" in department:
    #             return [department]
    #         elif department != None:
    #             emp_dict.update({"Department": str(department["Name"])})
    #         emp_dict.update({"departmentId":employee["departmentId"]})
    #     shift_emp = self.__mycommunity_db_dal.get_shift_emp_by_empId(employee["_id"])       
    #     for shiftId in shift_emp:
    #         shift_list.append(self.__mycommunity_db_dal.get_one_shift(shiftId["shiftId"]))
    #     emp_dict.update({
    #             "id": employee["_id"],
    #             "FirstName": employee["FirstName"],
    #                 "LastName" : employee["LastName"],
    #                 "StartWorkYear":employee["StartWorkYear"],
    #                 "shifts":shift_list
    #                 })
    #     return emp_dict
    def logIn_user(self,usrObj):
        obj_dict = {"email":usrObj["email"],"password": usrObj["password"]}
        this_user_obj = self.__mycommunity_db_dal.get_user_email(obj_dict)
        print(this_user_obj)
        if this_user_obj == []:
            return [{"Error": "The user was not found"}]
        for this_user in this_user_obj:
            print(this_user)
            print(this_user)
            if "Error" in this_user:
                return [{"Error": "The user was not found"}]
            elif this_user["password"] == obj_dict["password"]:
                    return [{"Success": "The user was found"}]
            else:
                return [{"Error": "The password is incorrect"}]
            
           
    def add_new_user(self,usrObj):
        obj_dict = dict()
        # use_obj = self.__mycommunity_db_dal.get_department_by_name(usrObj["department_name"])
        # if use_obj == None:
        #     return [{"Error": "The employee was not created - the department name is missing or the employee already exists in the system"}]
        # elif "Error" in use_obj:
        #     return [use_obj]
        
        # else:
        
        obj_dict = {"email":usrObj["email"],"password": usrObj["password"]}
        users_from_db = self.__mycommunity_db_dal.get_all_users()
        for usr in users_from_db:
            print(usr)
            if users_from_db != []:
                if "Error" in usr:
                    return [usr]
                elif usr["email"]==obj_dict["email"] :
                    return [{"Error": "There is an user with the same name"}]
                    break

        result = self.__mycommunity_db_dal.insert_new_employee(obj_dict)
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