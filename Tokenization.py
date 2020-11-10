import csv
from textblob import TextBlob
import nltk

stopwords = nltk.corpus.stopwords.words('english')

with open('Srilak_View_Holiday_Inn-Haputale_Uva_Province.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    def convert(s):
        return ''.join(s).split()

    def remove_stopwords(txt_tokenized):
        txt_clean = [word for word in txt_tokenized if word not in stopwords]
        return txt_clean

    for line in csv_reader:
        # print(line[6])
        blob = TextBlob(line[6])
        for s in blob.sentences:
            if len(s) > 1:
                sentence = convert(s)
                # print(sentence)
                clean_sentence = remove_stopwords(sentence)
                print(clean_sentence)
