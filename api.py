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
import re
import uuid
JSON_FILE = "data.json"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def load_user_data():
    try:
        with open(JSON_FILE, 'r') as f:
            data = json.load(f)


    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return  data

def save_user_data(data):
    with open(JSON_FILE,'w') as f:
        json.dump(data,f,indent=4)
def create_user():
    username = input("Username:")
    while True:
        email = input("Email:")

        if (re.fullmatch(regex, email)):

            phonenumber = input("Phonenumber:")
            password = input("Password:")
            user_data = load_user_data()
            user_data[username] = {"data": {"email": email, "phonenumber": phonenumber,"password":password},"posts":[]}
            save_user_data(user_data)
            break
        else:
            continue
    print("User created successfully")


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

def login():
    username = input("Username:")
    user_data = load_user_data()
    if username in user_data:
        while True:
            password = input("Password:")
            if password in user_data[username]['data']['password']:
                print("User successfully logged in")
                break
            else:
                print("Password incorrect")
                continue

    else:
        print("User not found")
        login()
    userOption = input("Enter 1: Create post")
    if userOption == "1":
        createPost(username)

def createPost(username):
    try:
        user_data = load_user_data()
        id = str(uuid.uuid4())
        title = input("Title:")
        body = input("Body:")
        url = input("URL:")
        post = {'id': id, 'title': title, 'body': body, 'url': url}
        user_data[username]['posts'].append(post)
        save_user_data(user_data)
        print("Post successfully created")
    except:
        print("Error")

samePosts = {}
def deletePost(username):
    user_data = load_user_data()
    if username in user_data:
        posts = user_data[username]['posts']
        for post in posts:
            print(f"{post['title']} \n")
        userinput = input("Fill which post to delete: ")
        index = 1
        for post in posts:
            if post['title'] == userinput:

                samePosts.update({index:post})
                index = index + 1
        for key,post in samePosts.items():

            print(f"ID : {key} Title : {post['title']} Body: {post['body']} URL: {post['url']} \n ")

        for key, post in samePosts.items():
            userinput = int(input("Which post do you want to delete: "))
            if key == userinput:
                print(post)
                posts.remove(post)
                save_user_data(user_data)
                print("Post successfully deleted")
                break
            else:
                continue

deletePost("min")

# userinput = "Test1"
# hasnotor = True just variable
# loop posts to check if has same title => if has same title return True, else return False
# if Test1 has 2 posts , send data to samePosts
# else Test1 has been deleted
# if hasnotOr:
#     samePosts
# else:
#     delePosts



# def printString(number):
#
#     for i in range(number+1):
#         print('*',end="")
#
# for i in range(5):
#     for j in range(5):
#         printString(i)
#     print()

# *
#
# **
# **
#
# ***
# ***
# ***
#
# ****
# ****
# ****
# ****

# print("Letter","Source","List",sep='_')



# data = True
# try:
#     if data:
#         print("Success")
# except (ValueError):
#     print("Fill correct number")
#https://www.digitalocean.com/community/tutorials/python-print
# def print_pattern(rows):
#     for i in range(1 , rows + 1):
#         for j in range(i):
#             for k in range(j):
#
#         print()



