# https://developers.google.com/edu/python/regular-expressions
import re
NamePage = " John is 22 and Cansy is 35 Leader is 40 Suu is 45"
Dict = {
    'John':22,
    'Cansy':35
}
ages = re.findall(r'\d{1,3}',NamePage)
names = re.findall(r'[A-Z][a-z][a-z]*',NamePage)
ageDict = {}
x = 0

for eachname in names:
    ageDict[eachname] = ages[x] #22
    x +=1
    print(ageDict)

# if re.search("we","we need to drive car to go with them and we dont have cars"):
#     print("There is we")

# weFound =  re.findall("we","we need to drive car to go with them and we dont have cars")
# for i in weFound:
#     print(i)

import requests

data = requests.get("https://jsonplaceholder.typicode.com/users")
nameFound = re.findall('dfssdf',data.text)
if nameFound:
    print("username found")