# lic = {0:{"Email":'min',"Password" : '123'},1:{"Email":'bhone',"Password" : '123'}}
#
# def login():
#     email = input("Enter your email address : ")
#     password = input("Enter your password : ")
#     for i in lic.values():
#         if email == i["Email"]  and password == i["Password"]:
#             print("Welcome admin")
#             break
#         else:
#             print("Try Again")
#             login()
#
# def register():
#     pass
#
#
# while True:
#     userinput = input("Do you want to register or login if registered click 1 and if login click 2 :")
#     if userinput == '1':
#         register()
#     elif userinput == '2':
#         login()


def login():
    file = open(r"E:/password.txt",'r')
    # username = input("Enter your username : ")
    # usernametxt = file.readline().strip()
    # if username == usernametxt:
    #     print("usernmae correct")
    #     password = input("Enter your password : ")
    #     passwordtxt = file.readline().strip()
    #     if password == passwordtxt:
    #         print("password correct")
    #     else:
    #         print("password incorrect")
    # else:
    #     print("username incorrect")
    print(file.readline())



    file.close()


# https://www.geeksforgeeks.org/python-string-strip/
# txt = "Welcome "
# print(txt.strip())
login()