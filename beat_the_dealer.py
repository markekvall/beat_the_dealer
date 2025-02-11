
from typing import List, Optional
import sys
import random


card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}

SAM_TARGET = 17
BLACKJACK = 21
PLAYER_NAME = "sam"
DEALER_NAME = "dealer"
MIN_DECK_SIZE = 15 #for simplicity, should be 52
VALID_SUITS = {"H", "D", "C", "S"}

class BeatTheDealer:

    def generate_shuffled_deck(self) -> List[str]:
        deck = [suit + value for suit in VALID_SUITS for value in card_values.keys()]
        random.shuffle(deck)
        return deck


    def evaluate_deck(self, deck: List[str]) -> None:
        if len(deck) < MIN_DECK_SIZE:
            raise ValueError(f"Deck must contain at least {MIN_DECK_SIZE} cards, it now contains {len(deck)}")

        seen_cards = set()

        for card in deck:
            if card in seen_cards:
                raise ValueError(f"Duplicate card found in deck: {card}")
            seen_cards.add(card)

            if len(card) < 2 or len(card) > 3:
                raise ValueError(f"Invalid card format: {card}")

            suit, value = card[0], card[1:]

            if suit not in VALID_SUITS:
                raise ValueError(f"Invalid suit '{suit}' in card: {card}")

            if value not in card_values:
                raise ValueError(f"Invalid value '{value}' in card: {card}")


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


    def display_results(self, winner: str, player_hand: List[str], dealer_hand: List[str]) -> None:
        print(winner)
        print(f"{PLAYER_NAME}: {', '.join(player_hand)}")
        print(f"dealer: {', '.join(dealer_hand)}")


    def main(self, deck_file: Optional[str] = None) -> None:
        try:
            if deck_file:
                with open(deck_file) as f:
                    deck = f.read().split(', ')
                self.evaluate_deck(deck)

            else:
                deck = self.generate_shuffled_deck()
                print("No deck file provided. Using a newly shuffled deck.")

            player_hand, dealer_hand = self.deal_cards(deck)
            player_score = self.calculate_score(player_hand)

            if player_score == BLACKJACK:
                winner = PLAYER_NAME
            elif player_score > BLACKJACK:
                winner = DEALER_NAME

            else:
                player_hand = self.play_turn(SAM_TARGET, player_hand, deck)
                player_score = self.calculate_score(player_hand)

                if player_score > BLACKJACK:
                    winner = DEALER_NAME

                else:
                    dealer_hand = self.play_turn(player_score, dealer_hand, deck)
                    dealer_score = self.calculate_score(dealer_hand)

                    if dealer_score > BLACKJACK:
                        winner = PLAYER_NAME
                    elif dealer_score > player_score:
                        winner = DEALER_NAME
                    else:
                        winner = PLAYER_NAME

            self.display_results(winner, player_hand, dealer_hand)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    BeatTheDealer().main(sys.argv[1] if len(sys.argv) > 1 else None)

