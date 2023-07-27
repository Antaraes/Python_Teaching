# information = {1:'Minbhone', 'description':"developer"}
# list = [1,2,3,4,5]
# # print(information[1])
#
# dict = {}
# dict['name'] = 'min'
# dict[1] = '2342432'
# dict[2] = 'fsdfsfs'
# dict['setofnumber'] = [2,3,5]
# print(dict)


# complexDict = {'name':'mgmg','job':{'main':['frontend','backend','cloud enginner'],'site':'manageer','professional':'basketball player'},'hobby':['reading','listening']}

# print(complexDict['job']['main'][2])

#copy
# dict2 = complexDict.copy()
# print(dict2)
#
#update
# dict2.update({'Address':'New York'})
# print(f"dict2 is {dict2}")
#
# dict3 = complexDict
# print(f"dict3 is {dict3}")
#
# dict3.update({'wakeup':'7am'})
# print(f"update dict3 is {dict3}")
# print(f"update complexDict is {complexDict}")
# dict3.clear()
# print(dict3)
# print(complexDict)
# print(dict2)


#user information
# range = 0
# while range < 3:
#     fristname = input("What is your first name: ")
#     secondname = input("What is your second name: ")
# # address = input("What is your address: ")
# # phonenumber = input("What is your phone number: ")
# # charge_money = input("What is your money: ")
# #     userInformation = {'firstname':fristname,'secndname':secondname}
#
#     if range == 0:
#         userInformation1 = {'firstname':fristname,'secndname':secondname}
#     elif range == 1:
#         userInformation2 = {'firstname':fristname,'secndname':secondname}
#     elif range  == 2:
#         userInformation3 = {'firstname': fristname, 'secndname': secondname}


#     print(f"{userInformation['firstname']} {userInformation['secndname']}")

#store as list
# range = 0
# userInformation = []
# userDict = {}
# # print(len(userInformation))
# for i in range(3):
#     fristname = input("What is your first name: ")
#     secondname = input("What is your second name: ")
#     userDict = {'firstname':fristname,'secondname':secondname}
#     print(f"userDict length is : {len(userDict)}")
#     userInformation.append(userDict)
#     print(f"userInformation length is : {len(userInformation)}")
# #
# # #
# # #
# print(userInformation)
# for i in userInformation:
#     print(f"{i['firstname']} {i['secondname']}")

# [{first:'min',second'bhone'},{},{}]

# store as dict
# range = 0
# userInformation = {}
# # get infomation
# while range < 3:
#     fristname = input("What is your first name: ")
#     secondname = input("What is your second name: ")
#     userDict = {'first':fristname,'second':secondname}
#     print("prevent" , userInformation)
#
#     userInformation.update({range:userDict})
#
#     print('update',userInformation)
#     range += 1
#
# print('update',userInformation)
#
# print(f"{userInformation[0]['first']} {userInformation[0]['second']}")

#read information
# {0: {'first': 'min', 'second': 'bhone'}}
# for key in userInformation:
#     userinput = input("enter what you want to see: country,number,currency,")
#     if userinput == 'country':
#
#         print(f"{userInformation[key]['name']} live in {userInformation[key]['country']}")
#     elif userinput == 'number':


dict1  = dict(name = "John", age = 36, country = "Norway")
print(dict1)
dict1.pop('name')

print(dict1)



# Country = input("Bank country")
# Number = input("Routing Number")
# Currency = input("Bank Currency")
# Holder = input("Account Holder Name")
# Money = float(input("Amount"))
# Value = Money * 1.2

while True:
    password = input("Enter Password:")
    comfrim_password = input("Enter Password:")
    if password == comfrim_password:
        break