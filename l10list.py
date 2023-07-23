        # [0,1,2]
myList = ["apple",2,True]
print(myList)

#add value
myList.append("bannana")
print(myList)

#remove value
myList.remove("apple")
print(myList)

print(myList.count("apple"))

#add value with index
myList.insert(1, "apple")
print(myList)

#remove with index
myList.pop(3)
print(myList)

#sorting
numberArray = ["BA","AB","Captain","General","Car","Football"]
numberArray2 = [1,4,6,55,43,23]
# numberArray2.sort(reverse=True)
# numberArray.sort()
print(numberArray)


myList.extend(numberArray)
print(myList)
myList.remove("BA")
print(myList)

#clear
# myList.clear()
# print(myList)





