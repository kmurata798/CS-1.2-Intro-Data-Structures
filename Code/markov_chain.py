from dictogram import Dictogram, read_file
import random

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