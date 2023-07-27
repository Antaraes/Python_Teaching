# num1 = int(input("keying number 1 = "))
# num2 = int(input("keying number 2 = "))

# result = usernumber1 + usernumber2
# print(result)

# operatorFunction = input("Operating Function + or - :")
# if operatorFunction == "+":
#     result = int(usernumber1 + usernumber2)
#     print (result)
#
# elif operatorFunction == "-":
#     result = usernumber1 - usernumber2
#     print(result)
# else:
#     print("invalid operation")

# if usernumber1 > usernumber2:
#     result = "usernumber 1 is greater than usernumber 2"
#     print(f"{usernumber1} is greater than {usernumber2} ")
# elif usernumber1 < usernumber2:
#     result = "usernumber 1 is less than usernumber2"
#     print(f"{usernumber2} is greater than {usernumber1}")

def add( number1, number2):
    return number1 + number2

def subtract( number1,number2):
    return number1 - number2


# def resultFn(f):
#     result = f
#     print(result)
def resultFn(fun,number1,number2):
    result = fun(number1,number2)
    print(result)



# number1 = int(input("keying first number : "))
# number2 = int(input("keying second number : "))

number1 = 1
number2 = 3

operation = str(input("keying operation + or - or * or / : "))

if operation == "+":
    resultFn(add,number1,number2)

elif operation == "-":
    resultFn(subtract,number1,number2)



# elif operation == "*":
#     result = number1 * number2
#     print(f"Result is : {result}")
#
# else:
#     result = number1 / number2
#     print(f"Result is : {result}")


