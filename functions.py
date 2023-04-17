# round()
print(7)
print(round(7,2))
print(round(7.61))
print(round(2.6666,2))
print(round(2.6657,0))
print(round(7.5))    # tie breaking case so even nearest number is 8
print(round(6.5))
print(round(7.41))
print(round(11.5))
print(round(12.5))
print(round(665,-1))
print(round(675,-1))
print(round(674,-4))
print(round(674,0))
print(round(674,-3))
print(round(-8/3))
print(round(-15))
print(round(-8/3,2))
print(round(670.102,-1))
print(round(670.102,1))
print(round(-2.5))

# f-strings()
name='cyuzuzo'
age=27
height=70.0
# print('my name is:',name,'I am ',age,'years old','My height is ',height,'centimeter')
print(f'my name is: {name}. I am {age} years old. My height is {height} centimeter')
print(f'cyuzuzo`s father is {age*2+18} years old.')
print(f"{2*5}")

# checkout
age=int(input('your current age please? '))
years_left=90-age
days_left=years_left*365
months_left=years_left*12
print(f'you have {days_left} days, weeks and {months_left} months left')

