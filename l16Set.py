set_dir = {'Anomaly Detection', 'Sales Forecasting', 'Image Classification'}
set_dir.update("A")
set_dir.update("b")
print(set_dir)

set_dir2 = set(['Anomaly Detection', 'Sales Forecasting', 'Image Classification'])
print(set_dir2)

set_dri3 = set([1,1,1,1,1,2,2,2,2,4,4,4,4])
print(set_dri3)

list = [1,2,3,4]
set_dri3.remove(1)
print(list) # mutable
print(set_dri3) # immutable

# issubset
s1 = {1,2,3,4,5,6,7,8,9,10,11,12,13}
s2  = {2,3}
print(s2.issubset(s1))

# clear
# s1.clear()
# print(s1)


s1.pop()
s1.remove(10)
print(s1)

