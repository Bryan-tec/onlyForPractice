import random

options = ('rock', 'paper', 'scissors')

user_option = input('rock, paper or scissors =>  ')
user_option = user_option.lower()

if not user_option in options:
  print('Esa opcion no es valida...')

computer_option = random.choice(options)

print('User option => ', user_option)
print('Computer option => ', computer_option)

if user_option == computer_option:
  print('  Draw!  ')
elif user_option == 'rock':
  if computer_option == 'scissors':
    print('rock wins scissors')
    print(' **User won** ')
  else:
    print('paper wins rock')
    print('   **Computer won**  ')
elif user_option == 'paper':
  if computer_option == 'rock':
    print('paper wins rock')
    print('  **User won**  ')
  else:
    print('scissors wins paper')
    print('  **Computer won**  ')
elif user_option == 'scissors':
  if computer_option == 'paper':
    print('scissors wins paper')
    print(' **user won**  ')
  else:
    print('rock wind scissors')
    print('  **Computer won**  ')
