import nltk
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
sentence = """corona virus is so scary. 5200 people till now were infected from corona. so, we have to take care from corona"""
tokenized_sentences = word_tokenize(sentence)
stop_words = set(stopwords.words('english'))
filtered = []
#for filtering words
for Eword in tokenized_sentences:
    if Eword not in  stop_words :
        filtered.append(Eword)
print (filtered)


#for stem the words 
for word in tokenized_sentences : 
    print(PorterStemmer().stem(word))