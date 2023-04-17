name = ['jenny','ram','shyam']
for i in name:
    print(i)
    if i == 'jenny':
        print('hey, it`s me')
numbers = [2,3,5,-2,10]
squares = []
for l in numbers:
    square = l**2
    squares.append(square)
    print('The list of sqaures is:',squares)

# for else loop
tuple1 = (2,56,34,3,5,-1)
for k in tuple1:
    print(k)
    if k == 5:
        break
    else:
        print('oops you fail')
else:
    print('loop successfully completed and we are in else block now!!')
# print('out of for/else')

# checkout
heights=input('enter all heights separated by a space: ')
height_list = heights.split()
count = 0
for height in height_list:
    count = count+1
print(count)
for a in range(count):
     height_list[a] =int(height_list[a])
print(height_list)
sum = 0
for person in height_list:
    sum = sum + person
avg = sum/count
print(avg)
print('Average height is:',round(avg))

# checkout
numbers = input('enter list of numbers ')
numbers_list = numbers.split()
count=0
for e in numbers_list:
    count +=1
print(f'the length of the list is:{count}')
for w in range(count):
    numbers_list[w] = int(numbers_list[w])
maximum_number = numbers_list[0]
for number in numbers_list:
    if number>maximum_number:
        maximum_number = number
print(f'The Maximum number is: {maximum_number}')







