# name=input('what is your name? ')
# length=len(name)
# print(length)
#
# a=1
# b='vanilla'
#
# swappping numbers
# print('before swapping:')
# a=input('enter value of a= ')
# b=input('enter value of b= ')
# temp=a
# a=b
# b=temp
# print('after swapping:')
# print('a='+ a)
# print('b='+ b)

# datatypes(primitive)

# print(0b11)
var1=123456789035
print(var1 + 1)

var1=123
var2=10.1
print(var1 + var2)

var1=0o123
var2=0x123
var3=123
print(var1)
print(var2)
print(var3)
# print(type(var2))
# print(type(var3))

name='agahozo crelia'
print(name[8])

var4=True
print(var4)
print(type(var4))

number=input('enter two digits number: ')
first_digit=number[0]
second_digit=number[1]
print(int(first_digit) + int(second_digit))

# arithmetic operators
print(5+2)
print(4**2)
print(4/2)
print(4//2)
print(5%2)
print(5 + 2 * 3 -1 + 10 / 5)
a= 5
b = 2
print(a / b)

# calculate_BMI
weight = input('enter the weight in kilograms: ')
height = input('enter the height in metres: ')
# BMI = int(weight)/(float(height ** 2))
# print('BMI is:'+str(BMI))
# print(int(weight)/(float(height ** height)))

# other way t
BMI=int(weight)/float(height) ** 2
# print(BMI)
print(int(BMI))
print(BMI)

# comparison operators
# a,b,c=5,6,7
a,b=5,6
c=a+b
a+=2
c//=a
print(c)
# relation operators
a=5
print(a==5)
print(a<=5)
print(a<5)
print(a != 6)
print(a>=5)
print((a+1) != 6)

a,b=1,2
c=a+b
#print(c)
c%=b
print(c)
c+=a
# print(c)
c//=a
print(c)

# logical operators
a,b=5,4
print(a>4 and b<10)  # will return true if both statement are true
print(a>4 or b<3)    # will return true if one of statement is true
print(not(a))        # reverse the result or negate the result
c=True
print(not(c))
print(a<4 or c)

print(5 and 4)       # will return Smallest number
# print(0 and 4)     # Smallest number
print( 0 or 4)       # Will return Largest number

# bitwise operator(&, | ,^ ,~ ,<< ,>>)
a,b=5,4
print(a & b)
print(~a)
print(a << 2)
print(a >> 2)
print(a | b)
print(a ^ b)
print(26 & 23)
print(17 | 24)
print(17 ^ 24)
print(~45)
print(68<<2)
print(56>>3)

# identify operators(is, is not)
a=5
b='5'
# print(a is b)
print(id(a))
print(id(b))
print(a is not b)
a=6
print(id(a))
print(a is a)

# membership operators
str='crelia agahozo'
print('creliaagahozo' in str)
L1=[2,67,0,-7,45]
print(10 in L1)
print(20 not in L1)

# checkout






























