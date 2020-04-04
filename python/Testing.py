import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import *

stop_words = (stopwords.words('english'))

sentence = "I have a really bad stomach ache"
sentence = sentence.lower()
sentence = sentence.split()
cleansentence = ""
print("have" in stop_words)
for word in sentence:
    if word not in stop_words:
        cleansentence = cleansentence + word + ' '

print(cleansentence)

text = nltk.word_tokenize(str(sentence))

