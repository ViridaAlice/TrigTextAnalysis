Identifying triggering content in literary media
===
Program written, maintained and annotated by Alice Elisabeth Rahn
M-Nr: 122592
Email: elisabeth.alice.rahn@uni-weimar.de
30.09.2022
===
SUMMARY:
This programm can be used to:
	a) Split a given text into sentences
	b) Hand-annotate and categorize a text
	c) Use machine learning to automatically classify
	   a given text into categories based on established groundtruth-data
===
Programming language: Python 3.9
IDE: Visual Studio 2022
Library requirements: 
(pip install)	spacy
		nltk
		classy-classification
===
Executable Files and their Usage:
1) editText.py:

	Input:	"data_to_analyse.txt" (Unformatted text data)

	Output: "split_text_data.txt" (Data split by sentences or
			       	       hand-annotated data)
	
	Usage: 	Split unformatted text into sentences
	        Also facilitates annotation by hand

2) analyzeText.py:

	Input: "split_text.txt" (hand-annotated text data)

	Output: "gt_data/" 	(Eight text files for each category 
				 present in hand annotated data)

	Usage: 	Split previously annotated text into respective 
		categories usable for spacy

3) classifyText.py:

	Input: "gt_data/"	(Eight text files for each category
				 present in hand annotated data)
	       "gt_data/untagged_data.txt" (Un-annotated, split data)

	Output: "spacy/"	(Eight text files for sentences from
				 unannotated data that falls into these
				 respective categories)

	Usage:  Use spacy library to analyze new text on basis of 
		established categories
