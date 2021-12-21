import random
number = random.randint(1,9)
chances = 0
while chances <5:
    guess=int(input("enter your guess: "))
    if guess==number:
        print("congratulations your guess is correct")
    elif guess<number:
        print("your guess is too low guess a number higher than that")
    else:
        print("your guess is too high guess a number lower than that")
    chances+=1
if not chances<5:
    print("you didnt guess a number")
    