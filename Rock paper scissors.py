import random

while True:
    i = input("Rock Paper Scissors: ")
    a = ['rock' , 'paper' , 'scissors']
    for y in a:
        y = random.choice(a)
        print(y)
        if (y == "rock" and i == "paper") or (y == "paper" and i == "scissors") or (y == "scissors" and i == "rock"):
            print("Win")
            break
        elif (y == "rock" and i == "rock") or (y == "paper" and i == "paper") or (y == "scissors" and i == "scissors"):
            print("Draw")
            break
        else:
            print("Lose")
            break
    say = input("Try again? Yes/No : ")
    if say.lower() == "no":
        break
        
print("Thank you for playing")


    
        
