import random


def get_guess():
    try:
        guess = list(input("Enter your guesses (4 numbers, no spaces, 0 through 3)\n"))
        if len(guess) != 4:
            print("You didn't enter 4 numbers")
            return get_guess()
        else:
            return guess
    except (KeyboardInterrupt, IndexError, ValueError):
        print("Invalid input!")
        return get_guess()


def game():
    time = 1
    lst = list(map(str, [random.randint(0, 3) for _ in range(4)]))
    # print(lst)

    guess = [""] * 4
    while guess != lst:
        guess = get_guess()
        if guess == lst:
            print("Congrats! You got it correct after {} attempt(s)!".format(time))
            exit()

        correct = 0
        for pos in range(4):
            if guess[pos] == lst[pos]:
                correct += 1
        print("Incorrect, you got {} correct".format(correct))
        if time % 4 == 0:
            resp = input("Would you like a hint? (Y/N)\n")
            if str(resp[0]).upper() == "Y":
                loc = random.randint(0, 3)
                print("Position {} is {}".format(loc, lst[loc]))
        time += 1


if __name__ == '__main__':
    game()
