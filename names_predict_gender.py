#importing packages
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

#creating feature sets and train the machine
def predict(word):
    return {'last_char' : word[-1]}
labeled_names = ([(name, 'male') for name in names.words('male.txt')]+
            [(name, 'female') for name in names.words('female.txt')])
featuresets = [(predict(n), g) for (n,g) in labeled_names] 
classifier = NaiveBayesClassifier.train(featuresets)


#predict first name
nameE = input ("input the name you want to specicify its gender : ")
print(classifier.classify(predict(nameE)))
more = input("input another name y/n")

#ask for more
while (more == 'y') :
    nameE = input ("input the name you want to specicify its gender : ")
    print(classifier.classify(predict(nameE)))
    more = input("another name y/n")
