import random
# a=random.randint(1,7)        # a and b are included a<=x<=b
# a=random.randrange(1,3)      # a are included but is not a<=x<b
# a = random.random()          # return random number btn 0.0<=x<1.0
# a=random.uniform(1,3)
l = [2,5,90,-5.89,12,56]
a=random.choice(l)
print(a)
random.shuffle(l)
print(l)

# checkout
side=random.randint(0,1)
print(side)
if side == 1:
    print('Head')
else:
    print('Tails')

# checkout
text="welcome to jenny`s lectures"
splited_text=text.split('e')
print(splited_text)

# checkout
names=input('enter everybody`s name separated by coma: ')
names_list=names.split(',')
print(names_list)
length = len(names_list)
# random_choice=random.randint(0,length-1)
person_selected=random.choice(names_list)
print(F'{person_selected} will pay the bill')
# print(F'{names_list[random_choice]} will pay the bill')



