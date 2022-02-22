#Number guessing game
import random
import math
lower = int(input("Enter the lower bound:"))
upper = int(input("Enter the higher bound:"))
x = random.randint(lower, upper)
print("You can guess only", round(math.log(upper - lower + 1, 2)),"times")
count = 0
while count < math.log(upper - lower + 1,2):
    count = count + 1
    guess = int(input("Guess a number"))

    if x == guess:
        print("Congratulations!, you did it in",count,"try")

        break
    elif x < guess:
        print("Try again, you guessed too high")

    elif x > guess:
        print("Try again, you guessed too low")

if count > math.log(upper - lower + 1, 2):
    print("The number is ",x)
    print("Better luck next time")