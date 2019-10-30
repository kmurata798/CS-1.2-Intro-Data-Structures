# HISTOGRAM FUNCTION
def read_file(file):
    """Reads from file"""
    with open(file, 'r') as f:
        words = f.read().split()
        words = [text.lower() for text in words]
    return words


def histogram(file):
    """return a histogram data structure [list] that stores each unique word
    along with the number of times the word appears in the source text.
    !!!TAKES VERY LONG TO LOAD!!!"""

    text = read_file(file)
    histogram = []

    for word in text:
        exists = False
        for hWord in histogram:
            if hWord[0] == word:
                hWord[1] += 1
                exists = True
        if exists == False:
            histogram.append([word, 1])
    return histogram


def histogram_dict(file):
    """return a histogram data structure that stores each unique word 
    along with the number of times the word appears in the source text"""

    words = read_file(file)
    histogram = {}
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

# UNIQUE WORDS FUNCTION

def histogram_tuple(file):
    """return a histogram data structure that stores each unique word
     along with the number of times the word appears in the source text"""
    # words = []
    # content = read_file(file)
    # words = content.split()
    words = read_file(file)
    histogram = []
    for word in words:
        exists = False
        for tWord in range(len(histogram)):
            if tWord == histogram[tWord][0]:
                histogram[tWord] = (word, histogram[tWord][1] + 1)
                exists = True
        if exists == False:
            histogram.append((word, 1))
    return histogram
             


def unique_words(histogram):
    """returns the total count of unique words with dictionary"""
    return len(histogram)

# #FREQUENCY FUNCTION

def frequency(word, histogram):
    """returns the number of times that word appears in a text LIST AND TUPLE"""
    for word in histogram:
        if word[0] == word:
            return word[1]

def frequency_dict(word, histogram):
    """returns the number of times that word appears in a text. DICTIONARY"""

    for key, value in histogram.items():
        if key == word:
            return value

if __name__ == "__main__":
    histogram_list = histogram_dict("txtdocs/sherlock.txt")
    # histogram = histogram("txtdocs/sherlock.txt")
    # histogram = histogram_tuple("txtdocs/sherlock.txt")

    unique_words = unique_words(histogram)
    word = 'mystery'

    # word_frequency = frequency(word, histogram)
    word_frequency = frequency_dict(word, histogram)

    print(histogram_list)
    print(f'Unique word count: {unique_words}')
    print(f"Number of times '{word}' appeared in the text: {word_frequency}")

