import unittest
from word_processor import  convert_to_word_list ,words_longer_than ,words_lengths_map ,letters_count_map ,most_used_character

class test_word(unittest.TestCase):
    def test_convert_to_word_list(self):
        self.assertEqual(convert_to_word_list("These are indeed interesting, an obvious understatement, times. What say you?"),['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you'])

    def test_words_longer_than(self):
        self.assertEqual(words_longer_than(6, "These are indeed interesting, an obvious understatement, times. What say you?"),['indeed', 'interesting', 'obvious', 'understatement'])

    def test_words_lengths_map(self):
        self.assertEqual(words_lengths_map("These are indeed interesting, an obvious understatement, times. What say you?"),{2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1})

    def test_letters_count_map(self):
        self.assertEqual(letters_count_map("These are indeed interesting, an obvious understatement, times. What say you?"),{'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0})

    def test_most_used_character(self):
        self.assertEqual(most_used_character(""),None)
        self.assertEqual(most_used_character("These are indeed interesting, an obvious understatement, times. What say you?"),"e")

if __name__ == "__main__":
    unittest.main()