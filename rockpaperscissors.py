import random,time

playerScore=0
compScore=0

choices=["r","p","s"]

round=1

while True:
    print("round",round)
    playerChoice=input("what do you pick (r)ock,(p)aper,(s)cissors?")
    compChoice=random.choice(choices)
    print("computer chose", compChoice)

    if len(compChoice)==0:
        print("Invalid input, Try again")
        time.sleep(1)
        continue
    if playerChoice[0].lower()==compChoice:
        print("Draw!")
        time.sleep(1)
        continue
    elif playerChoice[0].lower()=='r' and compChoice=='s':
        print("player wins the round!")
        time.sleep(1)
        playerScore=playerScore+1

    elif playerChoice[0].lower()=='r' and compChoice=='p':
        print("Computer wins the round!")
        time.sleep(1)
        compScore=compScore+1

    elif playerChoice[0].lower()=='s' and compChoice=='p':
        print("player wins the round!")
        time.sleep(1)
        playerScore=playerScore+1

    elif playerChoice[0].lower()=='s' and compChoice=='r':
        print("Computer wins the round!")
        time.sleep(1)
        compScore=compScore+1

    elif playerChoice[0].lower()=='p' and compChoice=='s':
        print("Computer wins the round!")
        time.sleep(1)
        compScore=compScore+1
        
    elif playerChoice[0].lower()=='p' and compChoice=='r':
        print("player wins the round!")
        time.sleep(1)
        playerScore=playerScore+1
    else:
         print("Invalid answer, Try again")
         continue

    round=round+1
    if round==6:
        break

print("Player wins: ", playerScore)
print("computer wins: ", compScore)

if playerScore>compScore:
    print("The player wins the game!")
elif compScore>playerScore:
    print("The computer wins the game!")
else:
    print("Draw")

     



    
