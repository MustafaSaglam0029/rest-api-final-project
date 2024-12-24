import json

def get_status(json_data):
    data = json.loads(json_data)
    data = list(data.values())
    status = data[0]
    return status