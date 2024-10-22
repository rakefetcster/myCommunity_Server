from DAL.kafka_producer import ProducerDal


class KafkaBL:
    def __init__(self):
        self.producer_kafka=ProducerDal('my-community')
        searchUrl = "local-business-data.p.rapidapi.com//search?"
               
    def send_msg_to_kafka(self,usrObj):
        # obj_dict = dict()
        # obj_dict = {"city1":usrObj["city1"],"city2":usrObj["city2"],"city3": usrObj["city3"]}
        resp = self.producer_kafka.producer_msg(usrObj)
        return resp
    
    # def build_search(self,usrObj):
    #     query=Cooking%20workshops%20in%20yerushlim%2C%20Israel&limit=20&zoom=13&language=en&region=us&extract_emails_and_contacts=false", headers=headers)
        
    #     query=usrObj[activity]+'%20workshops%20in%20yerushlim%2C%20Israel&limit=20&zoom=13&language=en&region=us&extract_emails_and_contacts=false", headers=headers)


    