import unittest
import warnings
from babbler import Babbler

class TestMarkovBabbler2(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore")
        self.babbler = Babbler(2)
        self.babbler.add_file('tests/test1.txt')

    def test_starters(self):
        expected = ['a b', 'a b', 'a b', 'a b', 'x y', 'x y']
        actual = self.babbler.get_starters()
        self.assertEqual(sorted(actual), expected)
    

    def test_stoppers(self):
        expected = ['c !', 'c ?', 'd .', 'e .', 'e .', 'z .']
        actual = self.babbler.get_stoppers()
        self.assertEqual(sorted(actual), expected)
    

    def test_ngrams(self):
        expected = ['a b', 'b c', 'c !', 'c ?', 'c d', 'c e', 'c x', 'd .', 'd e', 'e .', 'x y', 'y z', 'z .', 'z a', 'z z']
        actual = self.babbler.get_all_ngrams()
        self.assertEqual(sorted(actual), expected)
    

    def test_next_states(self):
        expected = {'a b': ['c', 'c', 'c', 'c', 'c', 'c'],
	'b c': ['d', 'e', 'd', 'x', '!', '?'],
	'c !': ['EOL'],
	'c ?': ['EOL'],
	'c d': ['.', 'e'],
	'c e': ['.'],
	'c x': ['y'],
	'd .': ['EOL'],
	'd e': ['.'],
	'e .': ['EOL', 'EOL'],
	'x y': ['z', 'z', 'z'],
	'y z': ['.', 'a', 'z'],
	'z .': ['EOL'],
	'z a': ['b', 'b'],
	'z z': ['a']}
        for state in self.babbler.get_all_ngrams():
            actual = sorted(self.babbler.get_successors(state))
            correct = sorted(expected[state])
            self.assertEqual(actual, correct, f"state '{state}' next should be {correct} but instead was {actual}")


class TestMarkovBabbler3(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore")
        self.babbler = Babbler(3)
        self.babbler.add_file('tests/test1.txt')

    def test_starters(self):
        expected = ['a b c', 'a b c', 'a b c', 'a b c', 'x y z', 'x y z']
        actual = self.babbler.get_starters()
        self.assertEqual(sorted(actual), expected)
    

    def test_stoppers(self):
        expected = ['b c !', 'b c ?', 'c d .', 'c e .', 'd e .', 'y z .']
        actual = self.babbler.get_stoppers()
        self.assertEqual(sorted(actual), expected)
    

    def test_ngrams(self):
        expected = ['a b c', 'b c !', 'b c ?', 'b c d', 'b c e', 'b c x', 'c d .', 'c d e', 'c e .', 'c x y', 'd e .', 'x y z', 'y z .', 'y z a', 'y z z', 'z a b', 'z z a']
        actual = self.babbler.get_all_ngrams()
        self.assertEqual(sorted(actual), expected)
    

    def test_next_states(self):
        expected = {'a b c': ['d', 'e', 'd', 'x', '!', '?'],
	'b c !': ['EOL'],
	'b c ?': ['EOL'],
	'b c d': ['.', 'e'],
	'b c e': ['.'],
	'b c x': ['y'],
	'c d .': ['EOL'],
	'c d e': ['.'],
	'c e .': ['EOL'],
	'c x y': ['z'],
	'd e .': ['EOL'],
	'x y z': ['.', 'a', 'z'],
	'y z .': ['EOL'],
	'y z a': ['b'],
	'y z z': ['a'],
	'z a b': ['c', 'c'],
	'z z a': ['b']}
        for state in self.babbler.get_all_ngrams():
            actual = sorted(self.babbler.get_successors(state))
            correct = sorted(expected[state])
            self.assertEqual(actual, correct, f"state '{state}' next should be {correct} but instead was {actual}")

if __name__ == '__main__':
    unittest.main()