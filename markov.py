"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    

    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    original_text = open(file_path).read()
    return original_text
    
def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # your code goes here
    words = text_string.split()
    for i in range(len(words)-2):
        key = (words[i],words[i+1])
        values = words[i+2]
        if key not in chains:
            chains[key] = [] # we add the first key to the chain and define its value as an empty list that we can start putting values in
        chains[key].append(values) # step to put values into the []
    
    print(chains)

def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.key())) #picking a random pair of keys in the original dictionary to start
    words = [key[0], key[1]] # create a new list of words that start collecting the random words that we are generating
    word = choice(chains[key]) # random word pulled from the value(which is a list) at the current key
    # your code goes here

    while word is not None:
        key = (key[1], word) # once we used this key(which was randomly chosen), we update the new key with the second word, and a random word that comes after it.
        words.append(word) # we add the random word to the words list so that we can build the paragrah
        word = choice(chains[key]) # we generate a new random word now because the key is updated as well with the new pair

    return ' '.join(words) # we put all the words in the list into a complete text


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
