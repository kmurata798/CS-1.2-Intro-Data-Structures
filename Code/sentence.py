from Code.sample_word import sample_weight

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