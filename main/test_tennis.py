# -*- coding: utf-8 -*-
import unittest
#from tennis_game import TennisGame
from tennis_game_multi import TennisGameMulti as TennisGame

test_cases = [
    (0, 0, "Love-All", 'player1', 'player2'),
    (1, 1, "Fifteen-All", 'player1', 'player2'),
    (2, 2, "Thirty-All", 'player1', 'player2'),
    (3, 3, "Deuce", 'player1', 'player2'),
    (4, 4, "Deuce", 'player1', 'player2'),

    (1, 0, "Fifteen-Love", 'player1', 'player2'),
    (0, 1, "Love-Fifteen", 'player1', 'player2'),
    (2, 0, "Thirty-Love", 'player1', 'player2'),
    (0, 2, "Love-Thirty", 'player1', 'player2'),
    (3, 0, "Forty-Love", 'player1', 'player2'),
    (0, 3, "Love-Forty", 'player1', 'player2'),
    (4, 0, "Win for player1", 'player1', 'player2'),
    (0, 4, "Win for player2", 'player1', 'player2'),

    (2, 1, "Thirty-Fifteen", 'player1', 'player2'),
    (1, 2, "Fifteen-Thirty", 'player1', 'player2'),
    (3, 1, "Forty-Fifteen", 'player1', 'player2'),
    (1, 3, "Fifteen-Forty", 'player1', 'player2'),
    (4, 1, "Win for player1", 'player1', 'player2'),
    (1, 4, "Win for player2", 'player1', 'player2'),

    (3, 2, "Forty-Thirty", 'player1', 'player2'),
    (2, 3, "Thirty-Forty", 'player1', 'player2'),
    (4, 2, "Win for player1", 'player1', 'player2'),
    (2, 4, "Win for player2", 'player1', 'player2'),

    (4, 3, "Advantage player1", 'player1', 'player2'),
    (3, 4, "Advantage player2", 'player1', 'player2'),
    (5, 4, "Advantage player1", 'player1', 'player2'),
    (4, 5, "Advantage player2", 'player1', 'player2'),
    (15, 14, "Advantage player1", 'player1', 'player2'),
    (14, 15, "Advantage player2", 'player1', 'player2'),

    (6, 4, 'Win for player1', 'player1', 'player2'),
    (4, 6, 'Win for player2', 'player1', 'player2'),
    (16, 14, 'Win for player1', 'player1', 'player2'),
    (14, 16, 'Win for player2', 'player1', 'player2'),
]

test_cases_fr = [
    (0, 0, "Zero-Partout", 'player1', 'player2'),
    (1, 1, "Quinze-Partout", 'player1', 'player2'),
    (2, 2, "Trente-Partout", 'player1', 'player2'),
    (3, 3, "Egalité", 'player1', 'player2'),
    (4, 4, "Egalité", 'player1', 'player2'),

    (1, 0, "Quinze-Zero", 'player1', 'player2'),
    (0, 1, "Zero-Quinze", 'player1', 'player2'),
    (2, 0, "Trente-Zero", 'player1', 'player2'),
    (0, 2, "Zero-Trente", 'player1', 'player2'),
    (3, 0, "Quarante-Zero", 'player1', 'player2'),
    (0, 3, "Zero-Quarante", 'player1', 'player2'),
    (4, 0, "Victoire joueur1", 'player1', 'player2'),
    (0, 4, "Victoire joueur2", 'player1', 'player2'),

    (2, 1, "Trente-Quinze", 'player1', 'player2'),
    (1, 2, "Quinze-Trente", 'player1', 'player2'),
    (3, 1, "Quarante-Quinze", 'player1', 'player2'),
    (1, 3, "Quinze-Quarante", 'player1', 'player2'),
    (4, 1, "Victoire joueur1", 'player1', 'player2'),
    (1, 4, "Victoire joueur2", 'player1', 'player2'),

    (3, 2, "Quarante-Trente", 'player1', 'player2'),
    (2, 3, "Trente-Quarante", 'player1', 'player2'),
    (4, 2, "Victoire joueur1", 'player1', 'player2'),
    (2, 4, "Victoire joueur2", 'player1', 'player2'),

    (4, 3, "Avantage joueur1", 'player1', 'player2'),
    (3, 4, "Avantage joueur2", 'player1', 'player2'),
    (5, 4, "Avantage joueur1", 'player1', 'player2'),
    (4, 5, "Avantage joueur2", 'player1', 'player2'),
    (15, 14, "Avantage joueur1", 'player1', 'player2'),
    (14, 15, "Avantage joueur2", 'player1', 'player2'),

    (6, 4, "Victoire joueur1", 'player1', 'player2'),
    (4, 6, "Victoire joueur2", 'player1', 'player2'),
    (16, 14, "Victoire joueur1", 'player1', 'player2'),
    (14, 16, "Victoire joueur2", 'player1', 'player2'),
]
def play_game(p1_points, p2_points, p1_name, p2_name):
    game = TennisGame(p1_points, p2_points, p1_name, p2_name)
    return game.get_current_score_display()


class TestTennis(unittest.TestCase):
    def test_Score_Game1(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, p1Name, p2Name) = testcase
            game = play_game(p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(score, game.get_current_score_display())


if __name__ == "__main__":
    unittest.main()
