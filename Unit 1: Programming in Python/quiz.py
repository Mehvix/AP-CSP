print("Welcome to a quiz that will find out if you're Aidan Moriarty!\n")
score = 0

if input("What year where you born?\n") == "2003":
    print("Correct!\n")
    score += 1
else:
    print("Nope!\n")

if input("What gender are you?\n") == "male":
    score += 1
    print("Same as Aidan\n")
else:
    print("That's not the same as Aidan\n")

if "oreo" in input("What's your favorite snack food?\n").lower():
    score += 3
    print("Aidan loves oreos\n")
else:
    print("Aidan would never eat that!\n")

if "row" in input("What's the your favorite sport?\n").lower():
    score += 4
    print("Yessir")
else:
    print("Nope, Aidan rows!")

if "chiv" in input("What's better: Chivalry or Mordhau?\n").lower():
    score += 2
    print("Yes, Aidan just spins in circles")
else:
    print("Nope Aidan is actually bad at Mordhau and hates it lol")

if "8" in input("What iPhone do you have?\n").lower():
    score += 1
    print("Correct")
else:
    print("Aidan actually hates that phone, stupid")

if score > 10:
    print("You're Aidan!")
else:
    print("Sorry, you're not Aidan :(")
