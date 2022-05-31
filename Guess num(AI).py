import random

def guess2():  
    high = 10
    low = 1
    y = random.randint(1, 10)
    print(f'AI: {y}')
    while True:
        say = input("Too high? Too low ? Correct? ")
        
        if say.lower() == "too high" or say.lower() =="high":
            high = y
            print(f'Your number between {low} and {high}')
            if low == high or low > high or high < low:
                print("You are joking right?")
            else:
                y = random.randint(low, high-1)
                print(f'AI: {y}')
            
        elif say.lower() == "too low" or say.lower() =="low":
            low = y
            print(f'Your number between {low} and {high}')
            if low == high or low > high or high < low:
                print("You are joking right?")
            else:
                y = random.randint(low+1, high)
                print(f'AI: {y}')
            
        elif say.lower() == "correct":
            return False
        
        else:
            print("I don't understand what you say")
            print("Say Too high, Too low or Correct")
    else:
        print("End")

if __name__ == "__main__":
    print("Guess my num stupid AI from 1 to 10")
    x = random.randint(1, 10)
    print(x)
    guess2()
    
    while True:
        say = input("Play again? (Yes/No) ")
        if say.lower() == "yes":
            guess2()
        elif say.lower() == "no":
            print("Thank you for playing")
            break
        else:
            print("Say yes or no idiot")

