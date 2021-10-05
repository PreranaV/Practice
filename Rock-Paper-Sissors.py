# importing the random module
import random

options = ['Rock', 'Paper', 'Sissors']
player1 = random.choice(options)
player2 = random.choice(options)

print("Player1: " + player1)
print("Player2: " + player2)

if (player1 == player2):
    print ("It's a tie!")

elif (player1 == 'Rock'): 
    if (player2 == 'Sissors'):
        print ("Player1 wins")
    else: 
        print ("Player2 wins")

elif (player1 == 'Paper'):
    if (player2 == 'Rock'):
        print ("Player1 wins")
    else: 
        print ('Player2 wins')

elif (player1 == 'Sissors'):
    if (player2 == 'Paper'):
        print ('Player1 wins')
    else:
        print ('Player2 wins')

else: 
    print ("Invalid")