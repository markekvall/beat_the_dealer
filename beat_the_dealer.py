
from typing import List, Optional
import sys

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}

SAM_TARGET = 17
BLACKJACK = 21
PLAYER_NAME = "sam"
DEALER_NAME = "dealer"
MIN_DECK_SIZE = 20

class BeatTheDealer:

    def calculate_score(self, hand: List[str]) -> int:
        return sum(card_values[card[1:]] for card in hand)


    def deal_cards(self, deck: List[str]) -> List[List[str]]:
        sam_hand, dealer_hand = [], []

        for _ in range(2):
            sam_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

        return sam_hand, dealer_hand


    def play_turn(self, target: int, hand: List[str], deck: List[str]) -> List[str]:
        while self.calculate_score(hand) < target:
            hand.append(deck.pop())
        return hand


    def main(self, deck_file: Optional[str] = None) -> None:
        try:
            if not deck_file:
                raise ValueError("No deck file provided. Usage: python beat_the_dealer.py <deck_file>")

            with open(deck_file) as f:
                deck = f.read().split(', ')

            if len(deck) < MIN_DECK_SIZE:
                raise ValueError(f"Deck must contain at least {MIN_DECK_SIZE} cards")

            sam_hand, dealer_hand = self.deal_cards(deck)
            sam_score = self.calculate_score(sam_hand)
            #dealer_score = self.calculate_score(dealer_hand)

            if sam_score == BLACKJACK:
                winner = PLAYER_NAME
            elif sam_score > BLACKJACK: #case when dealer gets a higher initial hand than 17 ignore
                winner = DEALER_NAME

            else:
                sam_hand = self.play_turn(SAM_TARGET, sam_hand, deck)
                sam_score = self.calculate_score(sam_hand)

                if sam_score > BLACKJACK:
                    winner = DEALER_NAME

                else:
                    dealer_hand = self.play_turn(sam_score, dealer_hand, deck)
                    dealer_score = self.calculate_score(dealer_hand)

                    if dealer_score > BLACKJACK:
                        winner = PLAYER_NAME
                    elif dealer_score > sam_score:
                        winner = DEALER_NAME
                    else:
                        winner = PLAYER_NAME


            print(winner)
            print(f"sam: {', '.join(sam_hand)}")
            print(f"dealer: {', '.join(dealer_hand)}")


        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    BeatTheDealer().main(sys.argv[1] if len(sys.argv) > 1 else None)

