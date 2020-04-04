from patient import patient
from Symptom import Symptom
import time
import random
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet, stopwords

ps = PorterStemmer()


class Doctor:
    def __init__(self):

        #Changed symptoms to only be single word
        self.SymptomList = {
            "cough" : 3,
            "congestion" : 2,
            "sneezing" : 1,
            "fever" : 5,
            "stomach" : 3,
            "throat" : 2,
            "nose" : 2,
            "sore body" : 5,
            "insomnia" : 4,
            "tired" : 4,
            "fatigue" : 5,
            "none" : 0,
            "arm" : 2,
            "leg" : 2,
            "head" : 4,
            "cold" : 4,
            "fear" : 3,
            "confused" : 3

        }
        self.genderList = {
            "male",
            "female",
            "other"
        }
        self.physicians = {
            "doctor",
            "dentist"
        }
        self.SymptomList2 = {
            "throat" : 2,
            "tooth" : 3,
            "gums" : 2,
            "breath" : 1,
            "plaque" : 1,
            "none" : 0,
            "yellow" : 2,
            "discolored" : 2,
            "jaw" : 3,
            "teeth" : 2,
            "gap" : 1
        }
        pass

    def greet_user(self):
        print("Hello my name is Dr.310")
        print("I will try to help diagnose your overall health based on your symptoms")

    def get_basic_info(self):
        name = input("What is your name? ")
        while True:
            try:
                age = int(input("Hello " + name + "! How old are you? "))
            except ValueError:
                print("Invalid input for age. Please try again.")
                continue
            else:
                break

        while True:
            gender = str(input("What is your gender? Male, Female or other. "))
            if self.inLexicon(gender, self.genderList):
                break
            print(gender + " is invalid")
            self.spellcheck(gender, self.genderList)

        return patient(name, age, gender)

    def new_symptom(self):
        mistakes = [ "Sorry I do not know that symptom","This is a little embarassing. But what is that?","Are you sure that's a real thing try something else"]
        physician = self.checkDoctor()
        if physician == 'doctor':
            symptomlist = self.SymptomList
        elif physician == 'dentist':
            symptomlist = self.SymptomList2

        while True:
                symptom = str(input(ps.stem("What is a symptom you are experiencing? (say none for no more) "))).lower()

                symptom = self.checkSynonyms(symptom, symptomlist)

                if symptom == "none":
                    return False
                elif self.inLexicon(symptom, symptomlist):
                    break
                else:
                    print(random.choice(mistakes))

    
        duration = int(input("How many days have you had this symptom? "))
        pain = int(input("On a scale from 1 to 10, how much discomfort does this cause you? "))
        tempsymptom = Symptom(symptom)
        tempsymptom.addSeverity(duration*pain)
        return tempsymptom

    #Gets synonums for each word in the sentence that is not a stopword, if a synonym is in our database of symptoms
    #it returns that, else it just returns the original sentance
    def checkSynonyms(self, symptom, symptomlist):
        for word in symptom.split(" "):
            print(word)
            if word in set(stopwords.words("english")):
                pass
            for syns in wordnet.synsets(word):
                for l in syns.lemmas():
                    print(l.name())
                    if self.inLexicon(l.name(), symptomlist):
                        return str(l.name())
        return symptom

    
    def spellcheck(self, input, lexicon):
        if input.lower() not in lexicon:
            for key in lexicon:
                if input[0:2] == str(key)[0:2]:
                    print("Did u mean: " + str(key))

        
    def inLexicon(self, sentence, lexicon):
        sentence = sentence.lower()
        for token in lexicon:
            if ps.stem(token) in sentence:
                return True

        return False

    def checkDoctor(self):
        while True: 
            physician = str(input("Are you looking for a general doctor. Or, a dentist? "))
            physician = physician.lower()
            for i in self.physicians:
                if i in physician:
                    physician = i 
                    return physician
            print("Invalid option. Please try (doctor) or (dentist).")


    def diagnose(self, patient):
        healthRating = 0
        symptoms = patient.getSymptoms()
        for asymptom in symptoms:
            healthRating += int(asymptom.getSeverity()) * int(self.SymptomList[asymptom.getName()])
        healthRating += patient.getAge()

        question = ["This may take a while. Any plans for the weekend?","While my diagnosis is being calculated. How's your week been?"]
        print(random.choice(question)) 
        
        print("Analyzing results...")
        for i in range(1,8):
            time.sleep(.5)
            print("...")

        print("Could be worse I guess \n...\n Well " + patient.getName() + "...")
        if healthRating > 75:
                print("I suggest you go to a real medical professional")
        elif healthRating > 50:
            print("I think you should get some rest and talk to me again tomorrow")
        else:
            print("You seem pretty healthy to me!")
        
        #return healthRating

    # def get_severity():
    #     duration = int(input("How many days have you had this symptom?"))
    #     pain = int(input("On a scale from 1 to 5, how much dicomfort does this cause you?"))
    #     return duration  * pain

    # symptom = get_symptom()
    # severity = get_severity()

    # def diagnose(symp, severity):
    #     return symp * severity