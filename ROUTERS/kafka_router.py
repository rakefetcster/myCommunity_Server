from flask import Blueprint,jsonify, request, make_response
from BLL.kafka_bl import KafkaBL


kafka = Blueprint('tokafka', __name__)
kafka_bl = KafkaBL()


@kafka.route("/", methods=['POST'])
def post_user():
    usrObj=request.json
    try: 
        result = kafka_bl.send_msg_to_kafka(usrObj)
        if result:
            return jsonify(result)
        else:
            return jsonify({'error': 'No data found'}), 400
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500   
