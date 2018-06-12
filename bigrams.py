from dicts import DefaultDict

# Given a list of chars or words, returns a dictionary of dictionaries,
# containing occurrence counts of bigrams.
def bigrams(LIST):
    d = DefaultDict(DefaultDict(0))
    for (w1, w2) in zip([None] + LIST, LIST + [None]):
        d[w1][w2] += 1
    return d

# returns a dictionary containing the count for each char/word (unigram) in the file
def unigrams(LIST):
	d = DefaultDict(0)
	for item in LIST:
		d[item] += 1
	return d

def file2bigrams_letter(filename):
    return bigrams(list(open(filename).read()))

def file2unigrams_letter(filename):
	return unigrams(list(open(filename).read()))

def file2bigrams_word(filename):
    return bigrams(open(filename).read().split())

def file2unigrams_word(filename):
	return unigrams(open(filename).read().split())


