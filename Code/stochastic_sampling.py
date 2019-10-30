from analyze_words import histogram, unique_words
import random

def pick_random_word(histogram):
    for i in range(len(histogram)):
        freq = histogram[i][1]
        text = histogram[i][0]
        if freq > 1:
            for i in range(1, freq):
                histogram.append([text, freq])

    random_num = random.randint(0, unique_words(histogram))
    random_word = histogram[random_num][0]
    return random_word

if __name__ == "__main__":
    pick_random_word(histogram)
