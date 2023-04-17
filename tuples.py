tuple1 = (10,5,7,-10,51,5)
tuple2 = ('0.5','DSA')
tuple3 = (tuple1,tuple2)
list1 = [78,90,89]
print(list1)
print(tuple(list1))
print(tuple('jenny'))
print(tuple1.index(7))
print(tuple1[3])
tuple4 = (12,6,-8,'jenny',True)
print(tuple4)
print(tuple4[1])
print(tuple4[:4])
print(tuple4[::2])
print(type(tuple4))
tuple6=(45,67,90)
# tuple4[0]=13                   # you cannot change value once it is created because it is immutable
print(tuple6)
print(tuple3)
print(tuple3[1])
print(len(tuple3))
tuple4=tuple1+tuple2
print(tuple4)
# print(max(tuple4))
print(max(tuple2))
print(min(tuple6))
tuple7=(10,)*5
print(tuple7)





