import random
import sys

def get_file_lines(filename):
    '''OPEN the FILE _WITHIN_ a function, the you DON'T HAVE TO TYPE file.close()!!!!!'''
    with open(filename, "r") as f:
        lines = f.readlines() 
        strip_line = [word.strip() for word in lines]
    return strip_line
        # print(f.readlines())
    

    # file = open(filename, 'r')

    # lines = []
    # for line in file:
    #     lines.append(line.strip())

    # '''THIS does the above 3 lines of code at once'''
    # clean_lines = []
    # for line in lines:
    #     clean_lines.append(line.strip())
    
    #list comprehension LOOKUP
    # clean_lines = [line.strip() for line in lines] 'THIS does the above three lines of code at once'
    # strip() gets rid of white space at beginning/end
    # file.close()

def pick_random_word():
    lines = get_file_lines("/usr/share/dict/words")
    word_list = []
    for index in range(number_of_words):
        word_list.append(random.choice(lines))
    return(' '.join(word_list))
    # index = random.randint(0, len(word_list) - 1)
    # # index = random.randint(len(word_list))
    # return word_list[index]

if __name__ == "__main__":
    number_of_words = int(sys.argv[1])
    print(pick_random_word())