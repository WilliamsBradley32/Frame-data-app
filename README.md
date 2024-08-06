This readME is for the Microservice A.

Events can be requested for validation by using zeroMQ on port 5678 on the local address and passing a json formatted object.
EXAMPLE (using python):
"""
context = zmq.Context()

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5678")

message = json.dumps({"name": "Winter Trip",  "tripStartDate": "08/08/2024", "tripEndDate": "08/08/2024",
                          "startDate": "08/07/2024", "endDate": "08/08/2024", "startTime": "12:30",
                           "endTime": "12:45", "description": ""})

socket.send_string(message)

"""

The user then receives the message by using socket.recv_json()

EXAMPLE:
"""
received_message = socket.recv_json()
"""

