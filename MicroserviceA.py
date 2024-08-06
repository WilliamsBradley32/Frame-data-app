# {"name": "",  "tripStartDate": "", "tripEndDate": "", "startDate": "",
#  "endDate": "", "startTime": "", "endTime": "", "description": ""}

import json
import zmq
import datetime
import ast

# ZeroMQ setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5678")


def date_validate(date):
    try:
        datetime.datetime.strptime(date, '%m/%d/%Y')
        return True

    except ValueError:
        print(f'Date is not in the correct format.')
        return False


def hour_validate(time):
    try:
        datetime.datetime.strptime(time, '%H:%M')
        return True

    except ValueError:
        print(f'Time is not in the correct format')
        return False


while True:
    to_validate_receive = socket.recv().decode()
    if len(to_validate_receive) > 1:
        to_validate = json.loads(to_validate_receive)

        validate_results = {"validDate": True, "validTime": True, "startEndWithin": True, "startBeforeEnd": True}

        if not date_validate(to_validate['startDate']):
            validate_results["validDate"] = False

        if not date_validate(to_validate['endDate']):
            validate_results['validDate'] = False

        if not hour_validate(to_validate['startTime']):
            validate_results['validTime'] = False

        if not hour_validate(to_validate['endTime']):
            validate_results['validTime'] = False

        if (to_validate['startDate'] < to_validate['tripStartDate']
                or to_validate['endDate'] > to_validate['tripEndDate']):
            validate_results['startEndWithin'] = False

        if to_validate['startDate'] > to_validate['endDate'] or to_validate['startTime'] > to_validate['endTime']:
            validate_results['startBeforeEnd'] = False

        send_message = json.dumps(validate_results, indent=4)
        socket.send_json(send_message)

        break

context.destroy()

