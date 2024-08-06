
import json
import zmq


context = zmq.Context()

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5678")

input('Press Enter to send event!')

send_message = {"name": "Winter Trip",  "tripStartDate": "08/05/2024", "tripEndDate": "08/08/2024",
                "startDate": "08/0/2024", "endDate": "08/08/2024", "startTime": "11:30",
                "endTime": "12:45", "description": ""}

socket.send_json(send_message)

message = socket.recv_json()

print(f"Server sent back: {message}")

