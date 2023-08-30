# @login
# def functon():
#     print

# Assigning Functions to variables
def fun(number):
    return  number + 1

add_number = fun
print(add_number)

# Functions inside other functions
def parentFun(number):
    def childFun(number):
        return number + 1
    result = childFun(number)
    return  result

print(parentFun(2))

# Passing functions as arguments to other functions
def add_number(number):
    return number + 1

def subtract_number(number):
    return number - 1

def mutiply_number(number):
    return number * 2
def functionCall(function):
    number = 5
    return function(number)

print(functionCall(add_number))


# Functions Returing other functions

def greetingFuntion():
    def englishFuntion():
        return "HI"
    return englishFuntion

# print(greetingFuntion()) return object
hello = greetingFuntion()
print(hello())


# Nested Functions
# try:
#
# except (ValueError) as err:
#     print(err)
def print_message(message):
    def message_render(message):
        print(message + 'This is a value error')

    message_render(message)

print_message("Some mesage")

# Simple Decorator
def lowercase_decorator(fun):
    def wrapper():
        func = fun()
        make_lowercase = func.lower()
        return make_lowercase
    return wrapper

def say_hi():
    return "Hello WORLD"

decorate = lowercase_decorator(say_hi)
print(decorate())

@lowercase_decorator
def say_burger():
    return "BURGER"

print(say_burger())