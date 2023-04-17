# a = range(2,15,3)
# a = range(10,0)
# a = range(10,0,-1)
# a = range(-1,-10,-1)      # i=-1, j=i+j, k=i-k
# a = range(1,10)
# a = range(10)
total=0
for i in range(1,100):
    total += i
print(total)
# checkout
sum = 0
# for a in range(2,101,2):
#     sum += a
# print(f'the summation of even numbers is: {sum}')
# another way
for c in range(1,101):
    if c%2==0:
        sum += c
print(f'the summation of even numbers is: {sum}')
# checkout
for number in range(1,101):
    if number%3==0 and number%5==0:
        print('fizzbuzz')
    elif number%3==0:
        print('fizz')
    elif number%5==0:
        print('buzz')
    else:
        print(number)
