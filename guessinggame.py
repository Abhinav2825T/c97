import random
number=random.randint(1,9)
chances=0
print("guess number between 1 to 9")
while chances<5:
    guess=int(input("enter your number:"))
    if guess==number:
        print("congratulation")
    elif guess<number:
        print("guess if low",guess)
    else: 
        print("your guess was high",guess)
    chances+=1

if not chances<5:
    print("you loose. the number is:"number)
