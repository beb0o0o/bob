import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

positive = ["wonderfull" , "good" , "nice" , "awosome" , "happy" , "delight" , "perfect" , "like"]
negative = ["bad" , "misrable" , "ashamed" , "angry" , "sad" , "sick" , "lonely" , "stop"]
neutral  = ["day" , "film" , "chair" , "sister" , "laptop" , "computer" ,"sleep" ,"I","am" ,"is","was","were"]
def Tsets(words):
    return dict([(word,True) for word in words ])
positive_sets=[(Tsets(pos), 'pos') for pos in positive]
negative_sets=[(Tsets(neg), 'neg') for neg in negative]
neutral_sets =[(Tsets(neu), 'neu') for neu in neutral]
train_set = positive_sets + negative_sets + neutral_sets
classifier = NaiveBayesClassifier.train(train_set)
neg = 0
pos = 0
decide = input("Do you want to detect if the sentence is positive or negative (y/n)\n")
if  (decide != 'n' and decide != 'y'):
    decide = input("Do you want to detect if the sentence is positive or negative (y/n)\n")
if (decide == 'n'):
    exit()
while decide == 'y':
    sentence = input("enter the sentence\n") 
    sentence = sentence.lower().strip()
    words = sentence.split(' ')
    print(sentence.split(' '))
    for word in words:
        result = classifier.classify(Tsets(word))
        if result == 'neg':
            neg+=1
        if result == 'pos':
            pos+=1
    ratioP = str(float(pos) / len(words))
    ratioN = str(float(neg) / len(words))
    print('negative\t'+ ratioN)
    print('positive\t'+ ratioP)
    neg = 0 
    pos = 0
    decide = input("Do you want to detect if the sentence is positive or negative (y/n)\n")