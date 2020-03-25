text = input("input text")
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
tokenized_text  =sent_tokenize(text)
tokenized_word  =word_tokenize(text)
fdist = FreqDist(tokenized_word)
print(tokenized_text)
print(tokenized_word)
print(fdist)
print(fdist.most_common(2))
