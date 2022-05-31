import random

while True:
    y = 0
    a = random.randint(1,9)
    print(a)
    while y < y+1:
        n = int(input("Guess 1 to 9: "))
        y +=1
        if n < a:
            print("Too low")
        elif n > a:
            print("Too high")
        else:
            print("Correct")
            print(f'You have guess: {y} times')
            break
    say = input("Play again? Yes/No ")
    if say.lower() == "no":
        print("Thank You for playing")
        break
    
def guess():
    
    y = random.randint(1, 10)
    print(y)
    while True:
        x = int(input("Guess: "))
        if x > y:
            print("Too high")
        elif x < y:
            print("Too low")
        else:
            print("Correct")
            return True

guess()
