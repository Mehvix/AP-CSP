import random


"""
Programmers: Max and Aidan
"""

'''
this program simulates what we are doing with our 8 card in class. I only used numeric values
from 1 to 10 in the cards for class, so this program will illustrate that.
'''
deck = []  # This list will be a deck of cards numbered 1-10
team_cards = []  # This list will be the 8 cards that the team has in front of them


# which came from the 1-10 valued cards.

def create_deck(num_vals=52):
    """creates a deck of 10 cards"""
    global deck  # use the global version of deck

    for i in range(1, num_vals + 1):  # creates however many cards num_vals is
        deck += [random.choice(range(1, 11))]  # place each value from 1-10


def generate_cards(num=8):
    """generates 8 cards from the above deck, unless a number is specified other than 8 """
    create_deck()  # create a deck of 10 cards unless a number is placed in the paramters
    global team_cards  # allows me to use team_cards in any function
    for i in range(num):  # simulates dealing out num (8 by default) carPython 2.7 (AP-CSP)ds
        team_cards += [random.choice(deck)]
    return team_cards  # returns the list of cards


def reset():
    """resets the team_cards to a blank list"""
    global team_cards
    team_cards = []


def find(card):
    """looks through the team_cards list for card
        return the indexed position of where the 1st card
        match is found, -1 or 'None' if the card is not found"""
    reset()
    global team_cards
    generate_cards()
    print(team_cards)
    for i in range(len(team_cards)):
        if card == team_cards[i]:
            return i
    return 'not found'


def deal_card():
    global deck
    random.shuffle(deck)
    temp = deck[0]
    deck = deck.remove[deck[0]]
    return temp


'''
1.  How many functions does this program have?
What are the names of each function?
4; create_deck, generate_cards, reset, find

2.  How do you run this program? hint: you only need to run one
function to make it work.
find()

3.  Using your algorithm or mine above, test the find function 
under a variety of situations
Done

4.  Why did I write a reset function?  
So that if you where to run the program twice it would start with a new list

5.  What if I wanted to generate 20 cards, what would I 
have to change in this program? 
Change the 11 to 21 in deck += [random.choice(range(1, 11))]


6.  What is the purpose of the keyword 'global'?
So that the variable can be accessed from any method


7. What if I wanted to generate a standard deck of cards (where instead of 
just a numeric value there is a numeric value and a suit).  Write a method that will
do this. Call your method create_standard_deck()
def create_standard_deck():
    cards = []
    global deck = []
    suit = ["hearts", "diamonds", "clubs", "spades"]
    
    for value in range(1,14)
        for s in suit:
        card = [value]+[s]
        deck += [card]
    return deck


8.  What would you have to do to shuffle the deck you just created?
Luckily the random class has a function we can use!! guess what the function is called!?!
random.shuffle(name_of_list)

9.  Use this function to shuffle your deck and deal out 5 cards to a player.
    a. which function allows you to 'deal 5 cards to a player' ?
    for _ in range(5):
        deal_card()

    b. Normally when I deal cards, I remove them from the deck! Create a function
    called dealCards that will take the number of cards to deal, get them from the deck,
    remove them from the deck while simultaneously adding them to the player hand
    def dealCards(n = 5):  #5 cards will be dealt by default unless otherwise specified
        
    TEST YOUR FUNCTIONS BY PRINTING OUT THE HANDS
    Can you deal cards to another player?
    



'''
