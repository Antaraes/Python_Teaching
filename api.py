# import json

# userinput = {
#     'name':'min bhone thant'
# }
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# y = json.dumps(userinput)
#
# loads = json.loads(x)
# print(loads)
# https://realpython.com/python-json/
# with open("data.json",'r') as f:
#     data = json.load(f)
#     print(data)

# with open("data.json",'w') as f:
#     userinput = {
#         "data":{
#             0:{
#                 'name':"Min Bhone Thant"
#             },
#             1:{
#                 'name':"Kyaw "
#             }
#         }
#     }
#     json.dump(userinput,f)

# import requests
#
# data = requests.get("https://jsonplaceholder.typicode.com/posts")
# real_data = json.loads(data.text)
# print(real_data)
#
#
#
# # Blog Website
# data = {"name":"min "}
# def read():
#     with open("data.json", 'r') as f:
#         print(json.load(f))
#
# def write():
#     with open("data.json", 'w') as f:
#         json.dump(data,f)
# write()


import json
JSON_FILE = "data.json"

def load_user_data():
    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)


    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return  data

def save_user_data(data):
    with open(JSON_FILE,'w') as f:
        json.dump(data,f)
def create_user():
    username = input("Username:")
    email = input("Email:")
    phonenumber = input("Phonenumber:")
    user_data = load_user_data()
    user_data[username] = {"data":{"email": email, "phonenumber": phonenumber}}
    save_user_data(user_data)

def read_user_data(username):
    user_data = load_user_data()

    if username in user_data:
        return user_data[username]['data']
    else:
        return "User not found"

def delete_user_data():
    user_data = load_user_data()
    username = input("Username:")
    if username in user_data:
        del user_data[username]
        save_user_data(user_data)
        print("User deleted")
    else:
        print("User not found")
create_user()
# data = True
# try:
#     if data:
#         print("Success")
# except (ValueError):
#     print("Fill correct number")




