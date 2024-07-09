# spam = True 

# if spam != True:
#     print("this means it's working")
# else:
#     print("No true")



# name = input("Tell me your name ")
# pws = input("let's see your password ")

# if name == "Camy":
#     print("Hello, ",name, "you're my girl")
#     if pws == "papujota":
#         print("we're clear")
#     else:
#         print("common dwag, you need to do better")


import sys, random 

print("ROCKET, PAPER, SCISSOR")

wins = 0
losses = 0
ties = 0

while True: #The main game loop 
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))

    while True: #the player input loop
        playerMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        if playerMove == 'q':
            sys.exit() #Quit the program 
        
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break the loop

        print('Type one of the r, p, s, q')

     # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

     # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

     # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1




