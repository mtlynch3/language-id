import math
import sys
import bigrams
import dicts

#accepts a unigram, bigram, and two chars/words
def addOneSmoothing(u, b, w1, w2):
	V = len(b.keys()) #vocab size
	bigram_count = b[w1][w2]
	unigram_count = u[w1]
	return (bigram_count + 1.) / (unigram_count + V)

ENGLISH_FILENAME = sys.argv[1]
FRENCH_FILENAME = sys.argv[2]
ITALIAN_FILENAME = sys.argv[3]
TEST_FILENAME = sys.argv[4]
OPTION = sys.argv[5]

if OPTION == "-l":

	########## QUESTION 1 ##########
	######## letter bigrams ########

	letter_out = open('output_letter.txt', 'w')

	english_bigrams = bigrams.file2bigrams_letter(ENGLISH_FILENAME)
	french_bigrams = bigrams.file2bigrams_letter(FRENCH_FILENAME)
	italian_bigrams = bigrams.file2bigrams_letter(ITALIAN_FILENAME)

	english_unigrams = bigrams.file2unigrams_letter(ENGLISH_FILENAME)
	french_unigrams = bigrams.file2unigrams_letter(FRENCH_FILENAME)
	italian_unigrams = bigrams.file2unigrams_letter(ITALIAN_FILENAME)

	for i, line in enumerate(open(TEST_FILENAME).read().split('\n')):
		if line == '':
			continue
		chars = list(line)
		max_prob = float("-Inf")
		max_language = ""
		lang = ""
		unigram = {}
		bigram = {}
		for j in range(0,3):
			prob = 0.0
			if j == 0:
				lang = "English"
				unigram = english_unigrams
				bigram = english_bigrams
			elif j == 1:
				lang = "French"
				unigram = french_unigrams
				bigram = french_bigrams
			else:
				lang = "Italian"
				unigram = italian_unigrams
				bigram = italian_bigrams

			for (w1, w2) in zip([None] + chars, chars + [None]):
				if w1 != None and w2 != None:
					prob += math.log(addOneSmoothing(unigram, bigram, w1, w2))
			if prob > max_prob:
				max_prob = prob
				max_language = lang

		letter_out.write(str(i + 1) + " " + max_language + "\n")

else:

	########## QUESTION 2 ##########
	######## word bigrams ########

	word_out = open('output_word.txt', 'w')

	english_bigrams = bigrams.file2bigrams_word(ENGLISH_FILENAME)
	french_bigrams = bigrams.file2bigrams_word(FRENCH_FILENAME)
	italian_bigrams = bigrams.file2bigrams_word(ITALIAN_FILENAME)

	english_unigrams = bigrams.file2unigrams_word(ENGLISH_FILENAME)
	french_unigrams = bigrams.file2unigrams_word(FRENCH_FILENAME)
	italian_unigrams = bigrams.file2unigrams_word(ITALIAN_FILENAME)

	for i, line in enumerate(open(TEST_FILENAME).read().split('\n')):
		if line == '':
			continue
		words = line.split()
		max_prob = float("-Inf")
		max_language = ""
		lang = ""
		unigram = {}
		bigram = {}
		for j in range(0,3):
			prob = 0.0
			if j == 0:
				lang = "English"
				unigram = english_unigrams
				bigram = english_bigrams
			elif j == 1:
				lang = "French"
				unigram = french_unigrams
				bigram = french_bigrams
			else:
				lang = "Italian"
				unigram = italian_unigrams
				bigram = italian_bigrams

			for (w1, w2) in zip([None] + words, words + [None]):
				if w1 != None and w2 != None:
					prob += math.log(addOneSmoothing(unigram, bigram, w1, w2))
			if prob > max_prob:
				max_prob = prob
				max_language = lang

		word_out.write(str(i + 1) + " " + max_language + "\n")
