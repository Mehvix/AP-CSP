import random


print("I have a number between 1 and 10 - take a guess!")
number = random.randint(1, 10)

while True:
    guess = int(input("Take a guess:\n"))

    if guess == number:
        print("Yay! You got it!")
        exit()

    elif guess > number:
        print("Sorry, your guess is too big!")
    else:
        print("Sorry, your guess is too small!")


