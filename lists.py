numbers=[10,0,-1,7,8,10,-67]
names=['jenny','krishn','agahozo']
mix_list=[1,'jenny',True,10,10]
print(len(numbers))
print(numbers[-2])
print(numbers[0:4])         # extended slicing
print(numbers[0:])          # extended slicing
print(numbers[:])           # extended slicing
print(numbers[0:5:3])       # extended slicing
print(numbers[0::3])
numbers.sort()
print(numbers)
print(numbers.sort())
numbers.reverse()
print(numbers)
numbers.extend([45,46,47,48])
print(numbers)
print(max(numbers))
print(names[2])
print(mix_list[2])
numbers.append(45)              # append one number at time
print(numbers)
numbers.insert(2,45)
print(numbers)
numbers[1]=3
print(numbers)
numbers[1:4]=[7,4,5]             # replace numbers in list
print(numbers)
numbers.remove(0)
print(numbers)
print(numbers.pop())
print(numbers)
print(numbers.pop(0))             # remove numbers at the first of list and print  the numbers that where removed
print(numbers)

# nested list
list1=[10,34,90,[45,78,-3],89]
print(len(list1))
print(list1[3])
print(list1[3][-1])
print(list1[3][-2])
print(list1[3][2])
print(list1[len(list1)-1])
print(list1[len(list1)-2])
print(list1[3][0:3])       # 0:3,3 means the length of index
print(list1[3][::])
print(list1[3][:2])

list2=[10,34,90,['mohan','shyam','Ram'],89]
print(list2[3][1:3])
print(list2[3][2:3])

# checkout
row1 = ['😀', '😀', '😀']
row2 = ['😀', '😀', '😀']
row3 = ['😀', '😀', '😀']

matrix=[row1,row2,row3]
print(f'{row1} \n {row2} \n {row3}')
position=input('enter the position where you want to hide money ')

#32
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]='x'
print(f'{row1} \n {row2} \n {row3}')





