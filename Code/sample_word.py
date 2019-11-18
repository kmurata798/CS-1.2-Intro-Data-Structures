from get_words import read_file_text
from word_count import histogram_dict, unique_words
import random
import sys
import pytest

# def pick_random_word(histogram):
#     """picks a random word"""
#     total_weight = 0
#     for item in histogram:
#         total_weight += item[1]
#     return total_weight

    # random_index = random.randint(0, len(histogram) - 1)
    # key = list(histogram.keys())
    # return key[random_index]

def sample_weight(histogram):
    """Uses the histogram dictionary to add each of its keys 
    to a new list based on the keys' value"""
    freq_list = []
    for key, value in histogram.items():
        [freq_list.append(key) for index in range(value)]
    rand_num = random.randint(0, len(freq_list) - 1)
    return freq_list[rand_num]
    # tot_weight = pick_random_word(histogram)
    # random_weight = random.randint(0, tot_weight)
    # for word in histogram:
    #     random_weight = random_weight - word[1]
    #     if random_weight <= 0:
    #         return word[0]

def get_sentence(histogram, amount=15):
    '''Uses the sample_weight function to get weighted words and
    combine them in a sentence
    PARAMETERS:
    histogram: Dictionary
    amount: int (default = 15 words)'''
    words = []
    for i in range(amount):
        words.append(sample_weight(histogram))
    sentence = ' '.join(words)
    return sentence
    
def test_sample_weight():
    """Test sample_weight function"""
    freq_dict = {}
    words = histogram_dict('../Code/txtdocs/test.txt')
    for i in range(10000):
        sample_word = sample_weight(words)
        if sample_word in freq_dict:
            freq_dict[sample_word] += 1
        else:
            freq_dict[sample_word] = 1
    """output key words and their probability percentages"""
    for i in freq_dict:
        # print(i, frequency_dict[i])
        print(i, freq_dict[i] / 10000)

    return freq_dict

# def testing_random():
#     onecount = 0
#     twocount = 0
#     fishcount = 0
#     bluecount = 0
#     redcount = 0
#     count = 0
#     while count != 100:
#         if pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'two':
#             twocount += 1
#         elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'one':
#             onecount += 1
#         elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'fish':
#             fishcount += 1
#         elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'blue':
#             bluecount += 1
#         elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'red':
#             redcount += 1
#         count += 1
#     print(f"ONE: {onecount}\nTWO: {twocount}\nFISH: {fishcount}\nBLUE: {bluecount}\nRED: {redcount}")
        

if __name__ == "__main__":
    entry = "../Code/txtdocs/{}".format(sys.argv[1])
    texts = histogram_dict(entry)
    print(get_sentence(texts, 20))

    # print(pick_random_word(texts))
    # print(sample_weight(texts))
    # test_sample_weight()
    # testing_random()

