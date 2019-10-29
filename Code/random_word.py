import random
import sys

def get_file_lines(filename):
    '''OPEN the FILE _WITHIN_ a function, the you DON'T HAVE TO TYPE file.close()!!!!!'''
    with open(filename, 'r') as file:
        print(file.readlines())
    

    # file = open(filename, 'r')

    # lines = []
    # for line in file:
    #     lines.append(line.strip())

    lines = file.readlines() 
    '''THIS does the above 3 lines of code at once'''
    # clean_lines = []
    # for line in lines:
    #     clean_lines.append(line.strip())
    
    #list comprehension LOOKUP
    # clean_lines = [line.strip() for line in lines] 'THIS does the above three lines of code at once'
    # strip() gets rid of white space at beginning/end
    # file.close()
    return lines

def pick_random_word(word_list):
    index = random.randint(0, len(word_list) - 1)
    # index = random.randint(len(word_list))
    return word_list[index]

def main():
    dictionary_words = get_file_lines('/usr/share/dic/words')
    if len(sys.argv) >= 2:
        num_words = int(sys.argv[1])
        for _ in range(num_words):
            word = pick_random_word(dictionary_words)
            print(word)
    else:
        print("Need argument for number of words to pick")
