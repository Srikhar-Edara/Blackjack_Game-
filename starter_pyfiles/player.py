import random


class Player:

    def __init__(self, name, dealer): # Constructor to initialize the player information
        self.name=name 
        self.dealer=dealer 
        self.games_won=0 
        self.games_lost=0 
        self.games_tied=0 
        self.hand=[] 
        self.natural_blackjack_flag=0 

    def decide_hit(self): # Determines whether a player is going to hit or not
        # DO NOT MODIFY
        return random.choice([True, True, False]) # Retuns True if the player hits else returns False

    def deal_to(self, card_value): # Deals a card to a player and adds it to his hand
        self.hand.append(card_value) # Adds a card to the player's hand

    @property
    def card_sum(self): # Figures out what the sum of the cards in the player's hand is
        Card_sum=0 # Initializes the card sum to zero
        for element in self.hand: # Traverses through the player's hand and adds the value of each card to the card sum
            Card_sum+=element
        return Card_sum # Returns the card sum

    def play_round(self): # Simulates the player playing a round of blackjack
        choice=self.decide_hit() # Assigns choice to True if a player is going to hit else False
        if choice==True and self.card_sum<21: # Checks if choice is True and the player's card sum is less than 21
            self.dealer.signal_hit(self) # Asks the dealer for a card
            self.play_round() # Recursively calls play_round till the player stands or goes bust

    def discard_hand(self): # Discards the player's hand
        self.hand=[] # Empties the player's hand

    @property
    def wins(self): # Returns the number of games the player has won
        return self.games_won

    @property
    def ties(self): # Returns the number of games the player has tied
        return self.games_tied

    @property
    def losses(self): # Returns the number of games the player has lost
        return self.games_lost

    def record_win(self): # Records and adds a win to the players tally
        self.games_won+=1 # Increments the games won by the player by 1

    def record_loss(self): # Records and adds a loss to the players tally
        self.games_lost+=1 # Increments the games lost by the player by 1

    def record_tie(self): # Records and adds a tie to the players tally
        self.games_tied+=1 # Increments the games tied by the player by 1

    def reset_stats(self): # Resets the player's stats
        self.games_won=0 # Resets the player's games won to zero
        self.games_tied=0 # Resets the player's games tied to zero
        self.games_lost=0 # Resets the player's games lost to zero

    def __repr__(self): # Represents the player's stats in a user friendly manner
        return "{}: {} {}/{}/{}".format(self.name,self.hand,self.games_won,self.games_tied,self.games_lost)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
