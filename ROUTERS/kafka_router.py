from flask import Blueprint,jsonify, request, make_response
from BLL.kafka_bl import KafkaBL


kafka = Blueprint('tokafka', __name__)
kafka_bl = KafkaBL()


@kafka.route("/", methods=['POST'])
def post_user():
    usrObj=request.json
    result = kafka_bl.send_msg_to_kafka(usrObj)
    print(result)  
    return jsonify(result)   
