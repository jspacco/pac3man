from babbler import Babbler

def maketestcode(classname, n, filename, starters, stoppers, ngrams, next_states):
    return """
class %s(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore")
        self.babbler = Babbler(%d)
        self.babbler.add_file('%s')

    def test_starters(self):
        expected = %s
        actual = self.babbler.get_starters()
        self.assertEqual(sorted(actual), expected)
    

    def test_stoppers(self):
        expected = %s
        actual = self.babbler.get_stoppers()
        self.assertEqual(sorted(actual), expected)
    

    def test_ngrams(self):
        expected = %s
        actual = self.babbler.get_all_ngrams()
        self.assertEqual(sorted(actual), expected)
    

    def test_next_states(self):
        expected = %s
        for state in self.babbler.get_all_ngrams():
            actual = sorted(self.babbler.get_successors(state))
            correct = sorted(expected[state])
            self.assertEqual(actual, correct, f"state '{state}' next should be {correct} but instead was {actual}")
""" % (classname, n, filename, starters, stoppers, ngrams, next_states)

def maketest(n, testcases):
    babbler = Babbler(n)
    babbler.add_file(testcases)
    starters = str(sorted(babbler.get_starters()))
    stoppers = str(sorted(babbler.get_stoppers()))
    ngrams = str(sorted(babbler.get_all_ngrams()))
    next_states = {}
    for state in sorted(babbler.get_all_ngrams()):
        next_states[state] = babbler.get_successors(state)
    next_states = str(next_states).replace('], ', '],\n\t')
    return maketestcode(f'TestMarkovBabbler{n}', n, testcases, starters, stoppers,
        ngrams, next_states)
    
if __name__ == '__main__':
    print(maketest(2, 'tests/test1.txt'))
    print(maketest(3, 'tests/test1.txt'))
    
