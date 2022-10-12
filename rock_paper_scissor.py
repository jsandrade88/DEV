import random

selection = ['rock', 'paper', 'scissors']

user_choice = input('Would you like rock, paper or scissors: ')
computer_choice = random.choice(selection)

print(f'\nYou selected {user_choice}, the computer selected {computer_choice}.\n;')


if user_choice == computer_choice:
    print(f'\nYou both selected the same thing - it is a tie!')

elif user_choice == 'rock':
    if computer_choice == 'scissors':
        print('Rock smashes scissors! You win!')

    else:
        print('Paper covers rock! You lose!')

elif user_choice == 'paper':
    if computer_choice == 'rock':
        print('Paper covers rock! You win!')
    
    else:
        print('Scissors cut paper! You lose!')
elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print('scissors cuts paper! You win.')
    else: 
        print('Rock smashes scissors! You lose!')
else: 
    print('Invalid selection. Try again.')