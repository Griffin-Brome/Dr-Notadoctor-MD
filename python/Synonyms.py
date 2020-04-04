import nltk
from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets("congestion"):
        for l in syn.lemmas():
            synonyms.append(l.name())

print(set(synonyms))
