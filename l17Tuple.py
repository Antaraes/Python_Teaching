# We can find items in a tuple since finding any item does not make changes in the tuple.
# One cannot add items to a tuple once it is created.
# Tuples cannot be appended or extended.
# We cannot remove items from a tuple once it is created.

list = [1,'one',True,'one']
tuple1  = tuple(list)
print(type(tuple1))

tuple2 = tuple("min")
print(type(tuple2))

tuple3 = ("min" , )
print(type(tuple3))

tuple4 = 'min',2
print(type(tuple4))

print(tuple1.count('one'))

print(tuple1[1])

#slice
print(tuple1[:2])

#concantinate
tuple5 =('max','min','bone',4,6)
tuple6 = 2,2,3
print(tuple5 + tuple6)
print(tuple5[0] + str(tuple6[0]))

list1 = [1,2,3]
list2 = [1,2,3]
print(list1[0] + list2[0])

print((tuple5,(tuple6)))

#unpacking  or destructing
# (a,b,c) = [1,2,3]
# (a,b,c) = "XYZ"
(a,b,c) = {1:'one',2:'two',3:'three'}
print(a)
print(b)
print(c)

#extendend unpacking
# (a,*b) = [1,2,3,4,67,68,69,70,]
(a,*b) = (1,2,3,4,67,68,69,70,)
print(a)
print(b)