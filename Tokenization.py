import csv
from textblob import TextBlob
import nltk
import re
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

stopwords = nltk.corpus.stopwords.words('english')
wnl = nltk.WordNetLemmatizer()
# lemmatizer = WordNetLemmatizer()

# with open('Srilak_View_Holiday_Inn-Haputale_Uva_Province.csv', 'r') as csv_file:
with open('98_Acres_Resort_and_Spa-Ella_Uva_Province.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)



	def lower_case(txt_tokenized):
		lowerCased = [doc.lower() for doc in txt_tokenized]
		return lowerCased

	def break_sentences(s):
		return ''.join(s).split()

	def remove_stopwords(txt_tokenized_1):
		txt_clean = [word for word in txt_tokenized_1 if word not in stopwords]
		return txt_clean

	def remove_punctuation(txt_tokenized_2):
		txt_no_punctuations = str.maketrans("", "", string.punctuation)
		stripped = [w.translate(txt_no_punctuations) for w in txt_tokenized_2]
		return stripped

	def pos_tagging(txt_tokenized_3):
		txt_pos = nltk.pos_tag(txt_tokenized_3)
		return txt_pos

	def lemmatization(txt_tokenized_4):
		text_lemm = [wnl.lemmatize(word) for word in txt_tokenized_4]
		return text_lemm


# with open("test.csv", "w", newline='') as f: 
# 	my_csvwriter = csv.writer(f)

# 	my_csvwriter.writerow(['Sentence'])
	sentenceArry = []
	# next(csv_reader)
	for line in csv_reader:
		# print(line[6])
		blob = TextBlob(line[6])
		for s in blob.sentences:
			if len(s) > 1:
				sentence = break_sentences(s)
				# print(sentence)
				lowerC_sentence = lower_case(sentence)
				clean_sentence = remove_stopwords(lowerC_sentence)
				# print(clean_sentence)
				clean_sentence2 = remove_punctuation(clean_sentence)
				# print(clean_sentence2)
				# pos_sentence3 = pos_tagging(clean_sentence2)
				# print(pos_sentence3)
				lemm_sentence4 = lemmatization(clean_sentence2)
				# print(lemm_sentence4)
				sentenceArry.append(lemm_sentence4)
				# my_csvwriter.writerow(lemm_sentence4)
				# leematize_2 = lemma_2(clean_sentence)
				# print([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(clean_sentence2)])
		# print()
	print(sentenceArry)



