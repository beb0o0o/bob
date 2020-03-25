import nltk
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.probability import FreqDist
text = """Egypt faces many problems like arid areas and urban congestion and many other challenges.
From these challenges, are the pollution problem and increasing the recycling products and opportunities."""
tokenized_word  =word_tokenize(text)
fdist = FreqDist(tokenized_word)
print(tokenized_word)
print(fdist)
print(fdist.most_common(2))
#for tagging 
data =nltk.pos_tag(tokenized_word)

#for filtering tags
for tag in data :
    if 'NNS' in tag :
        print(tag)
        print("\n")