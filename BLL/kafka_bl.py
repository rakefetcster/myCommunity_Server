from DAL.kafka_producer import ProducerDal
from DAL.kafka_consumer import KafkaStringConsumer
import requests
from CONFIGURATION.header_key import headers_key
import json
import pandas as pd


url = "https://local-business-data.p.rapidapi.com/search"

class KafkaBL:
    def __init__(self):
        self.my_community = ProducerDal('my-community')
        self.is_data_exist=ProducerDal('is-data-exist')
        self.is_data_exist_res=KafkaStringConsumer('is-data-exist-res')
        self.my_community_res=KafkaStringConsumer('my-community-res')
        searchUrl = "local-business-data.p.rapidapi.com//search?"
               
    def send_msg_to_kafka(self,activeObj):
        list_activity=["Sport","With_Kids","With_Friends","Food","Romantic","Travel"]
        activity_dict={
            "Sport":["Yoga","swimming","dance","football","basketball","Sport"],
            "With_Kids":["Beaches", "Zoos, animal parks, animal sanctuaries","Playgrounds and parks"\
                         ,"Amusement parks","Water parks","Pedal-boating and rowing"\
                            ,"Water sports"],
            "With_Friends":["Museum","Go camping","Art Gallery","Volunteer","Plan a picnic","biking"],
            "Food":["restaurants","food market","Food workshops"],
            "Romantic":["cooking class", "museum","Hike","movie theater","restaurant","camping"],
            "Travel":["hiking","camping","Beaches"]
        }
        list_places = ["Tel Aviv-Yafo","Jerusalem","Sea of Galilee","Herzliya","Haifa","Golan","Eilat","Acre","Zikhron Ya'akov"]   
        #is the data allready exist 
        place = list_places[activeObj["city"]]
        place = place.replace(" ","_")


        print(list_activity[activeObj["activity"]] + "_" + place )
        ask_json = 's3a://my-community/files/'+list_activity[activeObj["activity"]] + '_' +place+'.parquet'
        file_name = list_activity[activeObj["activity"]] + '_' +place
        data = [(ask_json)]
        columns = ["path"]
        resp = self.is_data_exist.producer_msg(file_name)
        
        try:
            is_exist = self.is_data_exist_res.consume_messages()  # Start consuming and processing messages
            print(f"Is data exist: {is_exist}")
            if is_exist == 'exists':
                resp = self.my_community.producer_msg(file_name)
                data_json = self.my_community_res.consume_messages()
                if data_json:
                    print("im here")
                    return {'data_json': data_json}  # Return it in a dictionary format
                else:
                    return {'error': 'No data found'}  # Handle cases where no data is parsed
                
            else:
                print("here - not exist")
                # print(activity_dict[list_activity[activeObj["activity"]]])
                #prepare to ask api for data
                for item in activity_dict[list_activity[activeObj["activity"]]]:
                    search = item +" in "+list_places[activeObj["city"]]+", Israel"
                print("search:"+search)
                querystring = {"query":search,"limit":"20","zoom":"13","language":"en","region":"hb","extract_emails_and_contacts":"false"}
                #from api
                # headers = headers_key()
                # data_api = requests.get(url, headers=headers, params=querystring)
                # data = data_api.json()
                
                # from my json
                with open('DAL/demo.json', 'r') as file:
                    data = json.load(file) 
                print(file_name)
                
                combined_message = {
                    "api_data": data, #json
                    "additional_info": file_name 
                }
                resp = self.my_community.producer_msg(combined_message)
                data_json = self.my_community_res.consume_messages()
                if data_json:
                    # print(data_json)
                    return data_json  # Return it in a dictionary format
                else:
                    return {'error': 'No data found'}  # Handle cases where no data is parsed
               

        except KeyboardInterrupt:
            print("Consumer interrupted by user.")
        finally:
            self.is_data_exist_res.close()
        
        return {}
    