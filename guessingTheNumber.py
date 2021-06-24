import random

number=random.randint(1,9)
chances=0
print("Guess the number between 1 to 10")

while chances<5:

    pocketMoney= int(input("Guessing the number: "))
    if pocketMoney==number:
        print("Congrats you won")
        break
    elif pocketMoney<number:
        print("Your guess was too low,guess a higher number than ",pocketMoney)
    else:
        print("Your guess was too high,guess a lower number than ",pocketMoney)

    chances +=1

if not chances<5:
    print("You lose,the number is " ,number)  
