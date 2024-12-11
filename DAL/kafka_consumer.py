import json
from kafka import KafkaConsumer


class KafkaStringConsumer:
    def __init__(self, topic, kafka_server='localhost:9092'):
        self.topic = topic
        self.kafka_server = kafka_server
        
        # Initialize Kafka Consumer
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.kafka_server,
            auto_offset_reset='latest',
            value_deserializer=lambda x: x.decode('utf-8')  # Deserialize to string
        )

    def consume_messages(self):
        """Consume messages from Kafka and process them."""
        print(f"Starting to consume messages from topic: {self.topic}")
        result = []  # List to accumulate parsed data
        
        for message in self.consumer:
            # print(f"Received message: {message.value}")

            # Try to process the message as JSON
            try:
                json_message = json.loads(message.value)
                # print("Processed JSON message:", json_message)

                # Extract the "API Data" field (which is a list of strings)
                api_data_str = json_message.get('api_data', [])
                additional_info = json_message.get('additional_info', None)  # Get additional_info if available

                # Parse the stringified JSON objects inside "API Data"
                for data_str in api_data_str:
                    try:
                        data_json = json.loads(data_str)
                        # print("Parsed restaurant info:", data_json)
                        if additional_info:
                            data_json['additional_info'] = additional_info
                        # Add the parsed restaurant_info to result list
                        result.append(data_json)
                        # print(result)
                    except json.JSONDecodeError:
                        print(f"Error decoding restaurant info: {data_str}")
                # print(json.dumps(result, indent=4))
                print('return result')
                return result
            except json.JSONDecodeError:
                #response is string and not json
                return(self.process_string_message(message.value))        
        # Return accumulated results at the end of processing all messages
        return result  # Return it in a dictionary format

    # def send_to_client(self, data):
    #     """Send the parsed data to your client (API or other destination)."""
    #     # Example of sending data to a client API using requests
    #     import requests
        
    #     client_api_url = "http://your-client-api-endpoint.com/data"
        
    #     try:
    #         response = requests.post(client_api_url, json=data)
    #         print(f"Sent data to client: {response.status_code}, {response.text}")
    #     except requests.exceptions.RequestException as e:
    #         print(f"Error sending data to client: {e}")
    def process_string_message(self, message):
        """Process the plain string message."""
        # Example of processing - simply print the string message
        print(f"Processed string message: {message}")

    def close(self):
        """Close the Kafka consumer connection."""
        self.consumer.close()
        print("Kafka consumer connection closed.")
