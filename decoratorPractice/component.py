import json
def load_user_data(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)


    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return  data

def save_user_data(data,file):
    with open(file,'w') as f:
        json.dump(data,f,indent=4)