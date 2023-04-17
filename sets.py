set1 = {10,56,89,90,'jenny',True,10,1}
set2 = {}
set3 = set()
# print(set1)
print(type(set1))
print(type(set2))
print(type(set3))
set1.add((99,13,14,15))
set1.remove(10)
print(set1)
print(len(set1))
# set1.clear()
# set1.pop()                      # remove element from set random
# print(set1)
print(set1.pop())
print(set1)

# operations
set1 = {'Rae','Shyam','jenny'}
set2 = {'jenny','jiya','Aakash'}
set3 = {'ankur','Pradeep'}
print(set1.union(set2))
# print(set1 | set2)
# print(set1.union(('mohan','jenny')))
# print(set1 | ('mohan','jenny'))
# print(set1.intersection(set2))
# print(set1.intersection(set2,set3))
# print(set1.intersection(['mohan','shiva']))
# print(set1 & set2)                  # intersection also but only sets
# set1.update(set2)
# set1.update(['Jenny','Mohan'])
# print(set1)
# set1.intersection_update(set2)
# print(set1)
# set1.intersection_update(set2)
# print(set1)
# print(set1)
# print(set2)
# set2.intersection_update(['mohan','shiva'])
# print(set1)
# print(set2)
# print(set1.difference(set2))
# print(set1.difference(set2,set3))
# set1.difference_update(set2)
# print(set1)
# set2.difference_update(set1)
# print(set2)
# print(set1.symmetric_difference(set2))           # union of all element minus intersection and it  does not allowed on multiple elements
# print(set1 ^ set2 ^ set3)
# print(set1.symmetric_difference_update(['mohan','shiva']))
# print(set2)
# print(set1)
set4 = {'ram','shyam','Jenny'}
set5 = {'jiya','Aakash'}
print(set4.isdisjoint(['mohan','shiva','Jenny']))
print(set4.issubset(['mohan','shiva','Jenny','ram']))
print(set1 <= set1)
print(set4.issuperset(['mohan','shiva','Jenny']))
print(set4 >= set5)              # superset
set2.clear()
print(set2)
del set5
print(set5)

