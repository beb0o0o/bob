import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

def predict(word):
    return {'last_char' : word[-1]}
names = ([(name,'male') for name in names.words('male.txt')] + 
     [(name,'female') for name in names.words('female.txt')])
featuresets = [(predict(n), g) for (n,g) in names]
train_set = featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set)
name = input ("input the name you want to specicify its gender : ")
print(classifier.classify(predict(name)))
more ='y'# input("input another name y/n")
while (more == 'y') :
    name = input ("input the name you want to specicify its gender : ")
    print(classifier.classify(predict(name)))
    #more = input("another name y/n")