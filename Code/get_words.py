import string, re

# HISTOGRAM FUNCTION
def read_file_text(file):
    """Reads from file"""
    with open(file, 'r') as f:
        words = f.read().split()
        words = [text.lower() for text in words]
        new_words = [re.sub("[^a-zA-Z]+", "", word).lower() for word in words]
    return new_words