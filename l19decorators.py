# @login
# def functon():
#     print

# Assigning Functions to variables
def fun(number):
    return  number + 1

add_number = fun
# print(add_number)
# print("first"+ str(fun(2)))
# print(add_number(4))

# Functions inside other functions
def parentFun(number):
    def childFun(num):
        return num  + 1

    def child2Fun(num):
        return  num * 6

    result = childFun(number) # 3
    mutiResult = child2Fun(number) # 12

    return  {
        "result":result,
        "mutiResult":mutiResult
    }

print(parentFun(2))

# Passing functions as arguments to other functions
def add_number(number):
    return number + 1

def subtract_number(number):
    return number - 1

def mutiply_number(number):
    return number * 2
def functionCall(function,number):
    return function(number) # add_number(5) -> 6

print(functionCall(add_number,7))


# Functions Returing other functions

def greetingFuntion():
    def englishFuntion():
        return "HI"
    return englishFuntion # HI

# print(greetingFuntion()) return object
hello = greetingFuntion() #HI
print(hello())


# Nested Functions
# try:
#
# except (ValueError) as err:
#     print(err)
def print_message(message):
    def message_render(message):
        print(message + 'This is a value error')

    for i in range(5):
        message_render(message)

print_message("Some mesage")

# Simple Decorator
def lowercase_decorator(fun): #say hi -> store as object
    def wrapper():
        result = fun() #say_hi() -> Hello World
        make_lowercase = result.lower()  # -> helloworld
        return make_lowercase

    return wrapper

def split_string(fun):
    def wrapper():
        result = fun()
        make_split = result.split()
        return make_split
    return wrapper
@split_string
@lowercase_decorator
def say_hi():
    return "Min Bhone Thant is a Developer"

print(say_hi())
# decorate = lowercase_decorator(say_hi)
# print(decorate())

@lowercase_decorator
def say_burger():
    return "BURGER"

# print(say_hi())
# print(say_burger())

def loginCheckingSystem(fun): #login
    def wrapper(password): #pass
        result = fun(password) # login("pass")
        print(result)
        if result == 'pass':
            print("Login Success")
        else:
            print("Login Failure")

    return  wrapper

@loginCheckingSystem
def login(password):
    print(f"Your password is {password}")
    return  password

userinput=input("Enter your password: ")
login(userinput)

# str = "Hello w,Or,ld"
# print(str.split(","))

