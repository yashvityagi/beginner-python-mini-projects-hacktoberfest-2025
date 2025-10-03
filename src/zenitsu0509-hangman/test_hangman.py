import unittest
from main import HangmanGame, pick_word, draw_gallows


class TestHangman(unittest.TestCase):
    def test_masked_word_progress(self):
        g = HangmanGame(secret_word="code", max_mistakes=6)
        self.assertEqual(g.masked_word().replace(" ", ""), "____")
        g.guess("c")
        self.assertIn("c", g.guessed)
        self.assertEqual(g.masked_word().replace(" ", ""), "c___")
        g.guess("o")
        self.assertEqual(g.masked_word().replace(" ", ""), "co__")

    def test_guess_validation(self):
        g = HangmanGame(secret_word="abc")
        with self.assertRaises(ValueError):
            g.guess("")
        with self.assertRaises(ValueError):
            g.guess("ab")
        with self.assertRaises(ValueError):
            g.guess("1")

    def test_win_and_loss(self):
        g = HangmanGame(secret_word="hi", max_mistakes=2)
        g.guess("h")
        g.guess("i")
        self.assertTrue(g.won())
        self.assertFalse(g.lost())

        g2 = HangmanGame(secret_word="hi", max_mistakes=1)
        g2.guess("x")
        self.assertTrue(g2.lost())

    def test_draw_gallows_bounds(self):
        first = draw_gallows(0)
        last = draw_gallows(100)
        self.assertIsInstance(first, list)
        self.assertIsInstance(last, list)
        self.assertGreaterEqual(len(last), 1)


if __name__ == "__main__":
    unittest.main()
