import string

def largest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        word = word.strip(string.punctuation)

        if len(word) > len(longest):
            longest = word

    return longest