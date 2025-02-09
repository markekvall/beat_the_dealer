# Beat the Dealer

This is a Python implementation of a simplified Blackjack-style card game called "Beat the Dealer". The game is played between two players: Sam and the Dealer, using a single deck of cards.

## Game Rules

1. The game uses a standard deck of 52 playing cards.
2. Number cards are worth their face value, face cards (J, Q, K) are worth 10, and Aces are worth 11.
3. Initially, both players are dealt two cards.
4. If either player has a Blackjack (an Ace and a 10-value card) with their initial hand, they win the game.
5. If both players have Blackjack, the non-dealer (Sam) wins.
6. If neither player has Blackjack, Sam will draw cards until their hand reaches a value of 17 or higher.
7. If Sam doesn't bust, the Dealer draws cards until their hand value exceeds Sam's.
8. The player with the higher hand value wins, unless they've exceeded 21, in which case they lose.

## Requirements

- Python 3.6 or higher

## Usage

1. Prepare a text file with a deck of cards. Each card should be represented by its value and suit (e.g., "CA" for Ace of Clubs, "H10" for 10 of Hearts), separated by commas and spaces.

   Example: `CA, D5, H9, HQ, S8, ...`

2. Run the script from the command line, providing the path to your deck file:

    Example: ` python3 beat_the_dealer.py deck-of-cards.txt`

3. Deck is ordered bottom to top, and cards are picked from the top



## Logical improvements

1. **Allowing Aces to be Both 1 or 11:**

   The following code ensures that Aces are counted as either 1 or 11, depending on the total score:

   ```python
   def calculate_score(self, hand: List[str]) -> int:
       score = 0
       aces = 0
       for card in hand:
           rank = card[1:]
           score += card_values[rank]
           if rank == "A":
               aces += 1

       while score > 21 and aces:
           score -= 10
           aces -= 1

       return score

2. **Make Sam chase a higher score if dealers initial hand is above 17.**
   
   As the instructions implies, sam will stop drawing cards when he has reached a score of 17 or higher. However, when the dealers initial hand is above 17 and not bust, there is no reason for Sam not to draw an extra card. A simple solution to this would be to adjust the sam_target to dealer score if this case happens.

   ```python
   sam_hand, dealer_hand = self.deal_cards(deck)
   sam_score = self.calculate_score(sam_hand)
   dealer_score = self.calculate_score(dealer_hand)

   if sam_score == BLACKJACK:
       winner = PLAYER_NAME
   elif sam_score > BLACKJACK:
       winner = DEALER_NAME
   elif dealer_score > sam_score and dealer_score <= BLACKJACK
       sam_target = dealer_score

