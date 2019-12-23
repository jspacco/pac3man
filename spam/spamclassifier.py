from os import listdir
from os.path import isfile, join
import sys
import string


class Classifier:
    def __init__(self):
        pass


    def process_spam_folder(self, folder):
        """
        Read all of the files in the given folder.
        Assume they are all spam files.
        This basically calls the read_spam_file() method for each file.
        """
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
        for filename in [join(folder, f) for f in listdir(folder)]:
            # print(filename)
            self.read_spam_file(filename)


    def process_ham_folder(self, path):
        """
        Read all of the files in the given folder.
        Assume they are all ham files.
        This basically calls the read_ham_file() method for each file.
        """
        for filename in [join(path, f) for f in listdir(path)]:
            # print(filename)
            self.read_ham_file(filename)


    def read_spam_file(self, filename):
        """
        Read the words from the file with the given filename.
        Assume that the file is a spam message.
        Remember that we only care that a word occurs,
        not how many times it occurs!
        """
        pass


    def read_ham_file(self, filename):
        """
        Read the words from the file with the given filename.
        Assume that the file is a ham message.
        Remember that we only care that a word occurs,
        not how many times it occurs!
        """
        pass
    
    
    def num_ham_messages(self):
        """
        Return total number of ham messages seen by this classifier.
        """
        pass

    
    def num_spam_messages(self):
        """
        Return total number of spam messages seen by this classifier.
        """
        pass


    def num_messages(self):
        """
        Return total number of messages seem, i.e. # spam msgs + # ham msgs
        """
        pass


    def prob_spam(self):
        """
        Overall probability of a message being spam, assuming we know
        nothing else about the the message. Hint: This is just 
        (# spam msgs / # total msgs)
        """
        pass


    def prob_ham(self):
        """
        Overall probability of a message being ham, assuming we know
        nothing else about the the message. Hint: This is just
        (# ham msgs / # total msgs)
        """
        pass


    def num_occurrences_spam(self, word):
        """
        Number of spam messages containing the given word
        """
        pass


    def num_occurrences_ham(self, word):
        """
        Number of ham messages containing the given word
        """
        pass


    def prob_word(self, word):
        """
        Probability that a given word occurs in any message, spam or ham
        """
        pass


    def prob_word_given_spam(self, word):
        """
        Probability that a word occurs in a spam message.
        """
        pass
    

    def prob_word_given_ham(self, word):
        """
        Probability that a word occurs in a ham message
        """
        pass


    def prob_spam_given_word(self, word):
        """
        Probability that a message is spam, given that it contains the given word
P(S|W) = P(W|S) * P(S)
         -------------
              P(W)
        """
        pass


    def prob_ham_given_word(self, word):
        """
        Probablity that a message is ham (i.e. not spam) given 
        that it contains the given word. We can compute this 
        directly, or simplify it to:
        1 - P(S|W)
        """
        pass
    




    def prob_spam_message(self, words):
        """
        Probability that a sequences of words is a spam message.
        Use the formula below. It assumes that words are independent events,
        which is not a good assumption in general for the English language,
        but works well in practice for spam classification.

          x
        -------
        (x + y)
            where x = p_1 * p_2 * ... * p_n
            and y = (1 - p_1) * (1 - p_2) * ... * (1 - p_n)
        """
        pass


    def prob_spam_message_log(self, words):
        """
        Probability that a sequences of words is a spam message.
        Use the formula that uses natural logs in order to prevent
        floating point underflow.

        https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering

        We rewrite our formula like this:

         1          (1-p1) * (1-p2) * ... * (1-pn)
        ---  - 1 =  ------------------------------
         p           p1 * p2 * ... * pn

        Then we take the natural log of both sides:

            1               (1-p1) * (1-p2) * ... * (1-pn)
        ln( --- ) - 1 = ln( ------------------------------ )
            p               p1 * p2 * ... * pn
        
        This basically turns into this (check Wikipedia for the algebra):

        1 / (e^A + 1)

        where A is:
        
        sum, i=1 to n, of (ln(1-p_i) - ln(p_i))

        where p_i is P(spam | word) for the i-th word
        """
        pass


    def most_common_words(self, n=1, ignore_words=set(), alpha_only=False):
        """
        Return a list of tuples for the n most common words. The tuple should
        contain the word and the number of times that it occurs. 
        
        If no value for n is given, use the default value of 1.
        
        ignore_words is an optional set of words that should be ignored
        (i.e. if a word is in the ignore_words set, do not include it
        in the return value for this function). This makes it easier to
        ignore a set of common words like 'the', 'that', 'and', etc.
        
        alpha_only is an optional boolean parameter. When it is true,
        the results should only include words containing letters,
        not numbers or punctuation. Hint: Python strings have an 
        isalpha() method.
        """
        pass


    def most_common_words_spam(self, n=1, ignore_words=set(), alpha_only=False):
        """
        Return a list of tuples for the n most common words in spam messages. 
        The tuple should contain the word and the number of times that it occurs. 
        
        If no value for n is given, use the value of 1.

        ignore_words is an optional set of words that should be ignored
        (i.e. if a word is in the ignore_words set, do not include it
        in the return value for this function). This makes it easier to
        ignore a set of common words like 'the', 'that', 'and', etc.
        
        alpha_only is an optional boolean parameter. When it is true,
        the results should only include words containing letters,
        not numbers or punctuation. Hint: Python strings have an 
        isalpha() method.
        """
        pass


    def most_common_words_ham(self, n=1, ignore_words=set(), alpha_only=False):
        """
        Return a list of tuples for the n most common words in ham messages. 
        The tuple should contain the word and the number of times that it occurs. 
        
        If no value for n is given, use the value of 1.

        ignore_words is an optional set of words that should be ignored
        (i.e. if a word is in the ignore_words set, do not include it
        in the return value for this function). This makes it easier to
        ignore a set of common words like 'the', 'that', 'and', etc.
        
        alpha_only is an optional boolean parameter. When it is true,
        the results should only include words containing letters,
        not numbers or punctuation. Hint: Python strings have an 
        isalpha() method.
        """
        pass



def check(classifier, word):
    """
    For checking that your code works.
    """
    s = classifier.num_occurrences_spam(word)
    h = classifier.num_occurrences_ham(word)
    print(f"# ham/spam for {word}: {s}, {h}")


def main():
    """
    Simple test driver.
    """
    #path = 'docs/basictest'
    #path = 'docs/enron1'
    path = 'docs/enron2'

    classifier = Classifier()

    classifier.process_spam_folder(path + '/spam')
    classifier.process_ham_folder(path + '/ham')

    print(f"# messages {classifier.num_messages()}")
    check(classifier, 'legitimate')
    check(classifier, 'please')
    check(classifier, 'buy')
    check(classifier, 'foo')

    print(f"prob spam message: {classifier.prob_spam_message('please buy viagara email online want money')}")

    # stopwords are common, uninteresting words in English
    # list of stopwords comes from nltk (natural language toolkit)
    stopwords = set([w.rstrip().lower() for w in open('stopwords.txt', errors='ignore').readlines()])
    print("\nSPAM")
    for tup in classifier.most_common_words_spam(20, stopwords, True):
        print(f"{tup[0]} {tup[1]}")
    print("\nHAM")
    for tup in classifier.most_common_words_ham(20, stopwords, True):
        print(f"{tup[0]} {tup[1]}")

main()