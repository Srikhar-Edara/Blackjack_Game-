from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names): # Constructor that initializes the game information(the player_list,round data, round number etc.)
        self.player_list=[] # Initializes the list of player objects to an empty list at first 
        self.dealer=Dealer() # Creates a dealer object
        for element in player_names: # Traverses through the list of player names and creates a list of Player Objects
            self.player_list.append(Player(element,self.dealer))
        self.Round_data="" # Assigns the Round Data to an empty string
        self.round_number=0 # Assigns the round number and round start flag to zero
        self.round_start_flag=0

    def shuffle_and_deal(self): # Shuffles and deals two cards each to the players and dealer (deals one card to the players and then one card to the dealer and so on)
        self.dealer.shuffle_deck() # Shuffles the deck
        for item in range(2): # A for loop which deals 2 cards to the players and the dealer
            for element in range(len(self.player_list)):
                self.player_list[element].deal_to(self.dealer.deck.draw()) # Deals a card to the players
            self.dealer.deal_to(self.dealer.deck.draw()) # Deals a card to the dealer

    def natural_blackjack_dealer_alert(self): # Checks if the dealer has gotten a natural blackjack and if so, checks if the other players have gotten one too and if not, awards losses to the players
        if self.dealer.card_sum==21: # Checks if the dealer's card sum is 21
            for element in self.player_list: # Traverses through the player list and checks if any of the players got a natural blackjack too
                if element.card_sum!=21: # If not, awards a loss to the player
                    element.record_loss()
                else:
                    element.record_tie() # If so, awards a tie to the player
            self.dealer.natural_blackjack_dflag=1 # Assings the dealer natural blackjack flag to 1

    def natural_blackjack_player_alert(self): # Checks if the player has gotten a natural blackjack and if so, awards the player a win
        for element in self.player_list: # Traverses through the player list
            if element.card_sum==21: # Checks if the player's card sum is 21
                element.record_win() # If so, awards a win to the player
                element.natural_blackjack_flag=1 # Assigns the player natural blackjack flag to 1

    def playing_the_hand(self): # Plays each player's and the dealer's hand in which the player decides to hit or stand and the dealer plays in a preordered fashion
        for element in range(len(self.player_list)): # Traverses through the player list
            self.player_list[element].play_round() # The player plays the round by either choosing to hit (the player might go bust in the process) or stand
        self.dealer.play_round() # The dealer plays in a preordered fashion

    def settling_the_hand(self): # After each person (as well as the dealer) has played, tallies wins/ties/losses
        if self.dealer.card_sum<=21: # Checks if the dealer has not gone bust
            for element in self.player_list: # If so, traverses through the player list
                if element.natural_blackjack_flag!=1: # Checks if the player has not gotten a natural blackjack
                    if element.card_sum>21: # If so, checks if the player has gone bust
                        element.record_loss() # If the player has gone bust, awards a loss to the player
                    elif element.card_sum==self.dealer.card_sum: # If the player has not gone bust and has the same card sum as the dealer's card sum, the player is awarded a tie
                        element.record_tie()
                    elif element.card_sum<self.dealer.card_sum: # If the player has not gone bust and has a card sum less than the dealer's card sum, the player is awarded a loss
                        element.record_loss()
                    elif element.card_sum>self.dealer.card_sum: # If the player has not gone bust and has a card sum greater than the dealer's card sum, the player is awarded a win
                        element.record_win()
        else:
            for element in self.player_list: # If the dealer has gone bust, traverses through the player list and checks for players who have not gone bust
                if element.natural_blackjack_flag!=1: # Checks if the player has not gotten a natural blackjack
                    if element.card_sum<=21: # If so, checks if the player has not gone bust
                        element.record_win() # If so, awards the player a win
                    else:
                        element.record_loss() # If not, awards the player a loss

    def round_representation(self): # Represents the results of the round in the form of a string
        Player_representation="" # Assigns each player's representation to an empty string
        for element in range(len(self.player_list)):  # Traverses through the player list
            if element!=len(self.player_list)-1: # Checks if the player is not the last player in the list
                Player_representation+="{}".format(self.player_list[element])+"\n" # Adds the player info to the string
            else:
                Player_representation+="{}".format(self.player_list[element]) # Adds the player info to the string

        self.round_number+=1 # Increments the round number
        if self.round_start_flag==0: # Checks if this is the first round
            self.Round_data+="Round {}".format(self.round_number)+"\n"+"{}".format(self.dealer)+"\n"+Player_representation # Represents the Round info in a string called round data
            self.round_start_flag+=1
        else:
            self.Round_data+="\n"+"Round {}".format(self.round_number)+"\n"+"{}".format(self.dealer)+"\n"+Player_representation # Represents the Round info in a string called round data

    def end_round_and_prepare_for_the_next(self): # After setting the hand, empties each player's hand and assigns the natural blackjack flags to zero
        for element in self.player_list: # Traverses through the player list
            element.discard_hand() # Discards each player's hand
            element.natural_blackjack_flag=0 # Sets all the player's natural blackjack flag to zero
        self.dealer.discard_hand() # Discards the dealer's hand
        self.dealer.natural_blackjack_dflag=0 # Sets the dealer's natural blackjack flag to zero


    def play_rounds(self, num_rounds=1): # Plays a number of rounds of blackjack
        if self.Round_data!="": # Checks if the round_data is not empty and if not empty, empties it
            self.Round_data=""

        number_of_rounds=num_rounds # Assigns num_rounds to number_of_rounds
        while number_of_rounds>0: # While loop to play out a specific number of rounds
            self.shuffle_and_deal() # Shuffles and deals the cards to the players and the dealer
            self.natural_blackjack_dealer_alert() # Checks if the dealer has gotten a natural blackjack and assigns ties/losses accordingly
            if self.dealer.natural_blackjack_dflag!=1: # Checks if the dealer's blackjack flag is not equal to one
                self.natural_blackjack_player_alert() # If so, checks if any of the player's have gotten a natural blackjack and assigns wins accordingly
                self.playing_the_hand() # The dealer and the players play their hand till each player has decided what to do (the dealer plays according to a preordered fashion)
                self.settling_the_hand() # Settles the hand, and tallies wins/ties/losses accordingly
                self.round_representation() # Represents the round information
                self.end_round_and_prepare_for_the_next() # Discards the player's and dealer's hand and resets the natural blackjack flags
                number_of_rounds-=1 # Reduces the number of rounds to be played by one
            else:
                self.round_representation() # Represents the round information (if the dealer has gotten a natural blackjack)
                self.end_round_and_prepare_for_the_next() # Discards the player's and dealer's hand and resets the natural blackjack flags
                number_of_rounds-=1 # Reduces the number of rounds to be played by one

        self.Player_representation="" # Assigns the player representation to an empty string
        self.round_start_flag=0 # Assigns the round start flag to zero
        self.round_number=0 # Assigns the round number to zero (Resets if after every call to play_rounds)

        return self.Round_data # Returns the round data

    def reset_game(self): # Used to reset the stats of all the players and empty the players' and dealer's hand
        for element in self.player_list: # Traverses through the player list
            element.reset_stats() # Resets a player's stats
            element.discard_hand() # Discards the player's hand
        self.dealer.discard_hand() # Discards the dealer's hand


if __name__ == "__main__":
    import doctest
    doctest.testmod()

