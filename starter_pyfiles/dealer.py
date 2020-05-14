from player import Player
from card_deck import CardDeck


class Dealer(Player):

    def __init__(self): # Constructor to initalize the dealer info and ensure that Player class' (the base class) constructor is invoked as necessary
        super().__init__("Dealer",self) # Invokes the Player class' constructor
        self.deck=CardDeck() # Creates a new CardDeck object
        self.natural_blackjack_dflag=0

    def shuffle_deck(self): # The dealer uses the Cardeck Object to shuffle the deck
        self.deck.shuffle() # Shuffles the deck

    def signal_hit(self, player): # Used to request a card after which, the dealer picks up a card from the top of the pile and gives it to the person who requested the card
        player.deal_to(self.deck.draw()) # The dealer draws the topmost card from the deck

    def play_round(self): # Simulates the dealer playing a round of blackjack
        if self.card_sum<17: # The dealer hits as long his card sum is less than 17
            self.deal_to(self.deck.draw()) # The dealer hits (draws a car from the top of the deck)
            self.play_round() # Recursively calls play round till the dealer's card sum is more than 16 after which, the dealer stands


if __name__ == "__main__":
    import doctest
    doctest.testmod()
