class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
    def __str__(self):
        return self.value + self.suit

def top(card_pile)

# The type of suit
suits = ['C', 'D', 'H', 'S']

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

# The card value
cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13}

# The deck of cards - List of Objects
deck = []

# Loop for every type of suit
for suit in suits:

    # Loop for every type of card in a suit
    for card in cards:

        # Adding the card to the deck
        deck.append(Card(suit, card))
        deck.append(Card(suit, card))

stacks = []
for i in range(10):
    stack = []
    for j in range(4):
        stack.append(deck.pop())
    stacks.append(stack)
    
target_piles = []
for i in range(8):
    pile = []
    target_piles.append(pile)



while True:
    print(str(deck[-1]) + "    " + " ".join([(p[-1].str() + " ") for p in target_piles]))
    print("a  b  c  d  e  f  g  h  i  j")
    max_stack = len(max(stacks, key=lambda s: len(s)))
    for i in range(max_stack):
        line = ""
        for stack in stacks:
            if (len(stack) > i):
                line= line + str(stack[i]) + " "
            else:
                line = line + "   "
        print(line)
    move = input()
    from_stack = ord(move[0]) - 97
    to_stack = ord(move[1]) - 97
    stacks[to_stack].append(stacks[from_stack].pop())
    