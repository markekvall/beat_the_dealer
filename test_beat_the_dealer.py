import unittest
from unittest.mock import patch, mock_open
from beat_the_dealer import BeatTheDealer
import sys
import io

class TestBeatTheDealer(unittest.TestCase):
    def setUp(self):
        self.beat_the_dealer = BeatTheDealer()

    def test_calculate_score(self):
        self.assertEqual(self.beat_the_dealer.calculate_score(['CA', 'H10']), 21)
        self.assertEqual(self.beat_the_dealer.calculate_score(['CA', 'HA']), 22)
        self.assertEqual(self.beat_the_dealer.calculate_score(['C2', 'H3', 'S4']), 9)

    def test_deal_cards(self):
        deck = ['CA', 'D5', 'H9', 'S7', 'D2', 'H3']
        sam_hand, dealer_hand = self.beat_the_dealer.deal_cards(deck)
        self.assertEqual(sam_hand, ['H3', 'S7'])
        self.assertEqual(dealer_hand, ['D2', 'H9'])
        self.assertEqual(deck, ['CA', 'D5'])

    def test_play_turn(self):
        hand = ['D5', 'S7']
        deck = ['H3', 'C9', 'D10']
        result = self.beat_the_dealer.play_turn(17, hand, deck)
        self.assertEqual(result, ['D5', 'S7', 'D10'])
        self.assertEqual(deck, ['H3', 'C9'])

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_game_with_deck_file(self, mock_stdout):
        deck_file = "deck-of-cards.txt"
        with patch("sys.argv", ["beat_the_dealer.py", deck_file]):
            self.beat_the_dealer.main(deck_file)

        output = mock_stdout.getvalue().strip()

        expected_output = "sam\nsam: D9, H4, H5\ndealer: SA, C6, D6"

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

