import random

print('ROCK PAPPER SCISSOR')
# Player and computer choose their move
players_move = input('Choose your move Rock(r), Papper(p), Scissor(s):')
computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_move = 'r'
elif computer_choice == 2:
    computer_move = 'p'
else:
    computer_move = 's'

computer_move = computer_move.upper()
players_move = players_move.upper()

# Results
if players_move == 'R' and computer_move == 'P':
    print('You lost')
elif players_move == 'R' and computer_move == 'S':
    print('You won')
elif players_move == 'P' and computer_move == 'R':
    print('You won')
elif players_move == 'P' and computer_move == 'S':
    print('You lost')
elif players_move == 'S' and computer_move == 'R':
    print('You lost')
elif players_move == 'S' and computer_move == 'P':
    print('You won')
elif players_move == 'S' and computer_move == 'S':
    print('Tie')
elif players_move == 'P' and computer_move == 'P':
    print('Tie')
elif players_move == 'R' and computer_move == 'R':
    print('Tie')
else:
    print('Your input is wrong')
