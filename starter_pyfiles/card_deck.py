import random


class CardDeck:
    class Card: # Creates a card in the form of a node
        def __init__(self, value): # Assigns the next pointer and value of the node (the card)
            self.value = value
            self.next = None

        def __repr__(self): # Represents the cards (their values)
            return "{}".format(self.value)

    def __init__(self): # Constructor that initializes the top of the deck to None
        self.top = None

    def shuffle(self): # Shuffles the deck
        card_list = 4 * [x for x in range(2, 12)] + 12 * [10]
        random.shuffle(card_list)

        self.top = None

        for card in card_list: # Adds the cards to the stack
            new_card = self.Card(card)
            new_card.next = self.top
            self.top = new_card

    def __repr__(self): # Represents the deck in the form of a stack of card
        curr = self.top
        out = ""
        card_list = []
        while curr is not None:
            card_list.append(str(curr.value))
            curr = curr.next

        return " ".join(card_list)

    def draw(self): # Draws a card from the top of the stack
        top=self.top # Assigns the top card to top
        if self.top==None: # If there were no cards in the stack, return None
            return None
        else:
            top_value=top.value  # Assigns the value of the top card to top_value
            self.top=top.next # Changes the top card to the card underneath the card which is presently the topmost card
            top.next=None # Draws the card (Remove it from the stack)
            return top_value # Returns the value of the former topmost card


if __name__ == "__main__":
    import doctest
    doctest.testmod()
