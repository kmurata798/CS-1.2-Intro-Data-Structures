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

        if self.word_list is not None:
            self.word_list = read_file(word_list)

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

        for a in range(len(self.word_list) -  1): 
            #loop through each word in word_list
            words = []
            for b in range(self.order):
                #order --> # of Markov Order
                if a < (len(self.word_list) - self.order):
                    #checks if given words are would be outside the range of word_list
                    words.append(self.word_list[a + b])
            if words == focus_words:
                #If the words inside word_list matches our focus words...
                next_words = []
                for b in range(self.order):
                    #Append next words and combines them into a string
                    next_words.append(self.word_list[a + (b + 1)])
                next_words_string = ' '.join(next_words)
                next_pairs.append(next_words_string)

        dictio[new_words] = Dictogram(next_pairs)
        return dictio

    def order_sample(self):
        """Gathers starting words from sampling to use for higher walk.

        word_list = str
        order = int
        """
        next_words = []
        main_histogram = Dictogram(self.word_list)

        #Collect initial starting words
        next_word = main_histogram.sample()
        next_words.append(next_word)
        chain = self.next_chain(next_word)

        #Chooses additional words based on the Markov order
        for index in range(self.order - 1):
            if len(chain) > 0:
                following_word = chain.sample()
                next_words.append(following_word)
                chain = self.next_chain(following_word)

        sample = ' '.join(next_words)
        return sample

    def higher_walk(self):
        """Starts by using the initial sample words to begin the chain.
        Then it uses the higher order chain to generate a full sentence using the order #.
        Amount with equal the length of the sentence.
        
        word_list = str
        amount = int
        order = int
        """
        sentence = []
        next_words = []

        #Declare and initialize starting sample words.
        words_str = self.order_sample()
        sentence.append(words_str)

        # Create the full sentence given the amount number
        for index in range(self.amount - self.order):
            next_words = []
            chain = self.higher_order(words_str) #Returns n order length of words
            if len(chain[words_str]) > 0:
                words_str = chain[words_str].sample()
                next_words = words_str.split()
                sentence.append(next_words[self.order - 1]) #Only get one item from next words to not repeat center word.

        sentence = " ".join(sentence)
        return sentence
                    
    def next_chain(self, new_word):
        """If the word found is equal to next_word, append the word to the list.
        Create list of following words.

        word_list = list
        new_word = string"""

        markov_list = []
        for index in range(len(self.word_list) - 1):
            if new_word == self.word_list[index]:
                markov_list.append(self.word_list[index + 1])
        chain = Dictogram(markov_list)
        return chain
    
    def make_sentence(self, words):
        """Takes each word in the list and joins them together 
        into a single sentence + period at the end.

        words = list
        """

        split_words = words.split()
        split_words[0] = split_words[0].capitalize()
        f_sentence = ' '.join(split_words) + '.'
        
        return f_sentence
    
    def main(self):
        words = self.higher_walk()
        sentence = self.make_sentence(words)
        return sentence

# def traverse(word_list, amount):
#     """creates a sentence starting with a random word from the first histogram.
#     The function keeps selecting a random word in each new histogram to create a new list of words.
    
#     word_list : list
#     amount : integer"""

#     sentence = []
#     starting_histogram = Dictogram(word_list)
#     next_word = starting_histogram.sample()
#     sentence.append(next_word)
#     for index in range((amount) - 1):
#         chain = next_chain(word_list, next_word)
#         if len(chain) > 0:
#             next_word = chain.sample()
#             sentence.append(next_word)

#     return sentence

if __name__ == '__main__':
    word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'cat']
    markov = Markov(word_list, 20)
    print(markov.main())