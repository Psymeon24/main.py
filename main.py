# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
# from typing import List


def read_file_content() -> str:
    """

    :rtype: object
    """
    # [assignment] Add your code here
    f = open('story.txt', 'r')
    file = f.read()
    print(file)
    return "Hello World"


def count_words():
    read_file_content()


# [assignment] Add your code here
text = open('story.txt', 'rt')
data = text.read()
words: list[str] = data.split()
print(len(words), 'Number of words in a text file:')
