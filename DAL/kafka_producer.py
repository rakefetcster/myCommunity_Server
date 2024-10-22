from kafka import KafkaProducer
import json

class ProducerDal:
    def __init__(self,topics):
        self.topics = topics
        self.server = 'localhost:9092'
        self.api_version=(2,8,1)

    def producer_msg(self,msgObj):
        print(msgObj)
        producer = KafkaProducer(bootstrap_servers = self.server, 
                                        api_version=self.api_version, 
                                        max_block_ms=100000,
                                        value_serializer=lambda msgObj: json.dumps(msgObj).encode('utf-8'))
                       
                                 
        
        producer.send(self.topics,msgObj)
        producer.flush()
        print(msgObj)
        producer.close()