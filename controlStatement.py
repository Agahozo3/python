height=int(input('enter height in feet: ' ))
if height == 3:
    print('Buy Token')
    print('Now You can board the metro')
else:
    print('No Token required')
# print('out of if block')

# checkout
number=int(input('enter the number:'))
if number % 2 == 0:
    print(f'{number} is  even number')
else:
    print(f'{number} is odd number')

# nested if else
if height>=3:
    print('you can ride')
    age=int(input('what is your age? '))
    if age <12:
        print('pay 150 Rs')
    elif age<18:
        print('pay 250 Rs')
    else:
        print('pay 500 Rs')
else:
    print('you cannot ride')
    print('bye')

# another one
a=51
if a%2==0:
    print('even')
    if a>30:
        print('number is greater than 30..great!!')
print('bye')

# checkout
year=int(input('enter the year to check '))

if year % 4 == 0:
 if year % 100 == 0:
  if year % 400 == 0:
     print(f'{year} is a leap year')
  else:
      print(f'{year} is not leap year')
 else:
    print(f'{year}  is not leap year')
else:
    print(f'{year} is not leap year')

# multiple if statement
height=int(input('what is your height '))
bill=0
if(height>=3):
    print('can ride')
    age=int(input('what is your age '))
    if age<12:
        bill=150
        print('Ticket Price is 150 Rs.')
    elif age<=18:
        bill=250
        print('Ticket Price is 250 Rs.')
    else:
        bill=500
        print('TICKET Price is 500 Rs')

    want_photo = input('do you want photo(Y/N) ')
    if want_photo == 'y' or want_photo == 'Y':
        bill = bill + 50
    print(f'your total bill is {bill}')
else:
    print('can`t ride')
print('bye')

# checkout
print('pizza order program:')
size=input('what size of pizza you want(S/M/L) ')
bill=0
if size=='S' or size=='s':
    bill +=100
    print('small Pizza price is 100 Rs.')
elif size =='M' or size=='m':
    bill +=200
    print('Medium Pizza price is 200 Rs.')
else:
    bill +=300
    print('Large Pizza price is 300.Rs')

add_pepperoni=input('do you want pepperoni(Y/N) ')
if add_pepperoni =='Y' or add_pepperoni=='y':
    size=input('what size of pepperoni you want(S/M/L) ')
    if size =='S' or size== 's':
        bill +=30
    else:
        bill +=50
extra_cheese=input('do you want extra cheese(Y/N) ')
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill +=20
print(f'your final bill {bill}')

# checkout
name1 = input('what is your name? ')
name2 = input('what is his/her name? ')
combine = name1+name2
lower_case_string = combine.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e

love_score =int(str(true)) + int(str(love))
if love_score < 10  or love_score > 90 :
    print(f'your score is {love_score} and you go together like coke and mentos')
elif love_score >= 40 and love_score <=50 :
    print(f'your score is {love_score} and you are alright together')
else:
    print(f'{love_score}')




















