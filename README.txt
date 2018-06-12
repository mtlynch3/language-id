Melissa Lynch
LING 406: Introduction to Computational Linguistics
Spring 2017

Assignment 2: Language models applied to the task of language identification

FILES
bigrams.py
	Given. I modified the file to give unigrams as well as bigrams.

dicts.py
	Given.

hw2.py
	Main file. Makes both unigrams and bigrams for each language (using a training data file). For each line in the test data, the program compares the bigram frequencies of the line to those of the training data bigrams for each language. The language with the highest probibility is chosen. 


To run, use Python 2.7. The program takes 4 arguments; the first is for the English training data file, the second is for the French training data file, the third is for the Italian training data file, and the fourth is for the test data file. The file must be run using one of two options:  "-l" runs the program using letter bigrams, and "-w" runs the program using word bigrams. Using the "-l" option will direct output to the file "output_letter.txt", and using the "-w" will direct output to the file "output_word.txt".

Example: 

	python hw2.py english_train.txt french_train.txt italian_train.txt test_data.txt -l


ANALYSIS
The letter bigrams produced a more accurate output than the word bigrams. The letter bigrams got one incorrect (line 22) and the word bigrams got three incorrect (line 44, line 244, line 262). More than 86% of the English word bigrams have a frequency less than 3; compare this to only 22% of the English letter bigrams. The frequencies for the letter bigrams are therefore going to be a better representation of their frequencies in the language as a whole. For example, it's very possible that in our data, the bigram ('speak', 'English') has a frequency of 1; the bigram ('green', 'elephant') could also have a frequency of 1. This would also mean that the probility of ('speak', 'English') occuring is the same as the probility of ('green', 'elephant') occuring. However, for English in general, the bigram ('speak', 'English') is significantly more likely than ('green', 'elephant'). 

