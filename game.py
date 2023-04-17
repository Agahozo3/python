import random
rock = '''
    ________
---'    ____)
        (____)
        (____)
  ---,__(___)
'''
paper = '''
    -------
---'   ____)___
          _____)
          ______)
---,__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
      ___________)
      (____)
---,__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input('enter your choice: Type 0 for Rock, 1 for Page, 2 for Scissors. '))
if user_choice >= 3 or user_choice < 0:
    print('you entered invalid number, you loose')
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print('Computer chose:')
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print('it`s a draw')
    elif computer_choice == 0 and user_choice == 2:
        print('you loose')
    elif user_choice == 0 and computer_choice == 2:
        print('you win')
    elif computer_choice > user_choice:
        print('You loose')
    elif user_choice > computer_choice:
        print('you win')


