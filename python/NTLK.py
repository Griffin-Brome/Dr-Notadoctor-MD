import nltk
from nltk.corpus import wordnet
import ssl

#BELOW CODE IS USED TO INSTALL SELECTED CORPUS'S, GET STOPWORDS AND SYNONEMS

#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()

SymptomList = {
            "cough" : 3,
            "congestion" : 2,
            "sneezing" : 1,
            "fever" : 5,
            "stomach" : 3,
            "throat" : 2,
            "nose" : 2,
            "body" : 5,
            "insomnia" : 4,
            "fatigue" : 5,
            "none" : 0
        }

synonymdict = {}

# for symptom in SymptomList:
#     synonymdict[symptom] = []
#     for word in wordnet.synsets(symptom, pos=wordnet.NOUN):
#         for l in word.lemmas():
#             synonymdict[symptom].append(l.name())
#     print(set(synonymdict[symptom]))

for word in wordnet.synsets("confused", pos=wordnet.NOUN):
    for l in word.lemmas():
        print(l.name())



