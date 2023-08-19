# file = open('password.txt', 'w')
# text = 'a2232f2'
#
# file.write(text)
# file.close()

# file  = open('password.txt', 'r')
# print(file.read())

# file = open('password.txt', 'w')
# l = ["This is lago \n", 'This is Python \n',"This is layout \n"]
#
# # file.write(l)
# file.writelines(l)
# file.close()

# ReadLines
# file = open('password.txt', 'r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.read())
# file.close()

# file = open('password.txt', 'w')
# l = "fsdfsdfsfsd"
# file.write(l)
# file.close()

# file = open('password.txt', 'w')
# userinput = input("Enter name:")
# file.write(userinput)
# file.close()

# file = open('password.txt', 'r')
# userinput = input("Enter password:")
# if userinput == file.read(): # userinput ( int ) == file.read() ( str )
#     print("Login successful")
# else:
#     print("Login failed")


from register import  register
from login import login

if __name__ == "__main__":
    while True:
        useranswers = input("Enter what do you want register or login :")
        if useranswers == 'register':
            register()
        elif useranswers == 'login':
            login()
        elif useranswers == 'quit':
            quit()
        else:
            print("invalid")