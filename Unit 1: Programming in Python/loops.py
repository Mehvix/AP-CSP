"""
Programmer: Max Vogel
The 1.3.8 lesson on doing loops and stuff.
"""

import random


def grades():
    """
    Asks the user to enter grades, and it will find the average, total number of grades, and the best grade entered
    """

    count = 0
    grade = 0
    max = 0
    sum = 0

    while grade != -1:
        grade = int(input("Enter a grade, or -1 to quit\n"))

        if grade == -1:
            break

        sum += grade
        count += 1
        average = sum / count

        # checks to find the best grade as the grades are entered
        if grade > max:
            max = grade

        print("Number entered: {}\n"
              "Average: {}\n"
              "Best: {}".format(count, average, max))


grades()


# ---

def hamman():
    """
    Checks if letter is in hangman
    """
    guess = '1'
    answer = 'hangman word'

    while guess not in answer:
        guess = input("Name a letter in " + answer + "\n")

    print("Good job!")


hamman()


# ---


def choose_winner():
    """
    Randomly chooses a winner and has the user guess who
    """
    players = ("Aydan", "Aiden", "Adam", "Aidan")

    winner = "Adam"

    while winner == "Adam":
        random.choice(players)  # because adam shouldn't win, duh

    print("Guess which of these players won:\n{}".format(players))

    total_guesses = 1

    while input() != winner:
        print("Sorry, guess again!\n")
        total_guesses += 1

    return total_guesses


print("Good job! You guessed in ", choose_winner(), "guess(es)")


# ---

def findLargest(numbers=(1, 2, 3)):
    largest = 0

    for i in range(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
