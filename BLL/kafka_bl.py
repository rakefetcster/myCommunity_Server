from DAL.kafka_producer import ProducerDal
import requests
from CONFIGURATION.header_key import headers_key
url = "https://local-business-data.p.rapidapi.com/search"


class KafkaBL:
    def __init__(self):
        self.producer_kafka=ProducerDal('my-community')
        searchUrl = "local-business-data.p.rapidapi.com//search?"
               
    def send_msg_to_kafka(self,activeObj):
        list_activity=["Sport","With Kids","With Friends","Food","Romantic","Travel"]
        activity_dict={
            "Sport":["Yoga","swimming","dance","football","basketball","Sport"],
            "With Kids":["Beaches", "Zoos, animal parks, animal sanctuaries","Playgrounds and parks"\
                         ,"Amusement parks","Water parks","Pedal-boating and rowing"\
                            ,"Water sports"],
            "With Friends":["Museum","Go camping","Art Gallery","Volunteer","Plan a picnic","biking"],
            "Food":["restaurants","food market","Food workshops"],
            "Romantic":["cooking class", "museum","Hike","movie theater","restaurant","camping"],
            "Travel":["hiking","camping","Beaches"]
        }
        list_paces = ["Tel Aviv-Yafo","Jerusalem","Sea of Galilee","Herzliya","Haifa","Golan","Eilat","Acre","Zikhron Ya'akov"]        
        print(activity_dict[list_activity[activeObj["activity"]]])
        for item in activity_dict[list_activity[activeObj["activity"]]]:
            search = item +" in "+list_paces[activeObj["city"]]+", Israel"
            querystring = {"query":search,"limit":"20","zoom":"13","language":"en","region":"hb","extract_emails_and_contacts":"false"}
            print(querystring)
            headers = headers_key()
            response = requests.get(url, headers=headers, params=querystring)

            resp = self.producer_kafka.producer_msg(response.json())
            return resp
    