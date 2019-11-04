from analyze_words import read_file, histogram_dict, unique_words
import random
import sys
import pytest

def pick_random_word(histogram):
    """picks a random word"""
    random_index = random.randint(0, len(histogram) - 1)
    key = list(histogram.keys())
    return key[random_index]

def sample_weight(histogram):
    freq_list = []
    for key, value in histogram.items():
        [freq_list.append(key) for index in range(value)]
    rand_num = random.randint(0, len(freq_list) - 1)
    return freq_list[rand_num]
    
def testing_random():
    onecount = 0
    twocount = 0
    fishcount = 0
    bluecount = 0
    redcount = 0
    count = 0
    while count != 100:
        if pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'two':
            twocount += 1
        elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'one':
            onecount += 1
        elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'fish':
            fishcount += 1
        elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'blue':
            bluecount += 1
        elif pick_random_word(histogram_dict("txtdocs/fish.txt")) == 'red':
            redcount += 1
        count += 1
    print(f"ONE: {onecount}\nTWO: {twocount}\nFISH: {fishcount}\nBLUE: {bluecount}\nRED: {redcount}")
        

if __name__ == "__main__":
    # testing_random()
    entry = f"../Code/txtdocs/{sys.argv[1]}"
    texts = histogram_dict(entry)
    print(pick_random_word(texts))
    print(sample_weight(texts))


