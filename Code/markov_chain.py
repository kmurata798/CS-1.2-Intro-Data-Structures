from .dictogram import Dictogram, read_file
import random

class Markov():
    """Generate sentence in different orders with a given amount"""

    def __init__(self, word_list, amount, order=2):
        """Initialize class variables
        
        word_list = str
        new_words = str
        order = int
        """
        self.word_list = word_list
        self.amount = amount
        self.order = order

    def higher_order(self, new_words):
        """Traverse through list of words, combining them into a string. The number of words in the string
        depends on the order number. If the string matches new_words string, add new_words to a list and
        combine it into a string.
        
        new_words = str
        """

        dictio = dict()
        focus_words = new_words.split()
        words = []
        next_words = []
        next_pairs = []

        for a in range(len(self.word_list)-1): 
            """loop through each word in word_list"""
            words.clear()
            for b in range(self.order):
                """order --> # of Markov Order"""
                if a < (len(self.word_list) - self.order):
                    """checks if given words are would be outside the range of word_list"""
                    words.append(self.word_list[a + b])
            if words == focus_words:
                """If the words inside word_list matches our focus words..."""
                next_words.clear()
                for b in range(self.order):
                    """Append next words and combines them into a string"""
                    next_words.append(self.word_list[a + (b + 1)])
                next_words_string = ' '.join(next_words)
                next_pairs.append(next_words_string)

        dictio[new_words] = Dictogram(next_pairs)
        return dictio

    def order_sample(self):
        """Gathers starting words from sampling to use for higher walk.

        word_list = str
        order = int

                    

def next_chain(word_list, new_word):
    """If the word found is equal to next_word, append the word to the list.
    Create list of following words.

    word_list : list
    new_word : string"""

    markov_list = []
    for index in range(len(word_list) - 1):
        if new_word == word_list[index]:
            markov_list.append(word_list[index + 1])
    
    chain = Dictogram(markov_list)
    return chain

def traverse(word_list, amount):
    """creates a sentence starting with a random word from the first histogram.
    The function keeps selecting a random word in each new histogram to create a new list of words.
    
    word_list : list
    amount : integer"""

    sentence = []
    starting_histogram = Dictogram(word_list)
    next_word = starting_histogram.sample()
    sentence.append(next_word)
    for index in range((amount) - 1):
        chain = next_chain(word_list, next_word)
        if len(chain) > 0:
            next_word = chain.sample()
            sentence.append(next_word)

    return sentence

def make_sentence(word_list):
    """Takes each word in the list and joins them together into a single sentence + period at the end.

    word_list : list"""

    word_list[0] = word_list[0].capitalize()
    final_sentence = ' '.join(word_list) + '.'
    return final_sentence

if __name__ == '__main__':
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'cat']
    print(make_sentence(traverse(word_list, 15)))