from patient import patient
from Symptom import Symptom
import time
import random
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()


class Doctor:
    def __init__(self):
        self.SymptomList = {
            "cough" : 3,
            "congestion" : 2,
            "sneezing" : 1,
            "fever" : 5,
            "stomach ache" : 3,
            "sore throat" : 2,
            "runny nose" : 2,
            "sore body" : 5,
            "insomnia" : 4,
            "tired" : 4,
            "fatigue" : 5,
            "none" : 0
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
            "sore throat" : 2,
            "sore tooth" : 3,
            "bleeding gums" : 2,
            "bad breath" : 1,
            "plaque" : 1,
            "none" : 0
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
            print("Invalid gender. Please try again.")
        return patient(name, age, gender)

    def new_symptom(self):
        mistakes = [ "Sorry I do not know that symptom","This is a little embarassing. But what is that?","Are you sure that's a real thing try something else"]

        while True:
            physician = str(input("Are you looking for a general doctor. Or, a dentist?"))
            physician = physician.lower()
            for i in self.physicians:
                if i in physician:
                    physician = i
            print("Invalid option. Please try (doctor) or (dentist).")

        while True:
            if physician == 'doctor':
                symptom = str(input(ps.stem("What is a symptom you are experiencing? (say none for no more) "))).lower()
                if symptom == "none":
                    return False
                if symptom not in self.SymptomList:
                    print(random.choice(mistakes))
                if symptom in self.SymptomList:
                    break

            if physician == 'dentist':
                symptom = str(input("What is a symptom you are experiencing? (say none for no more) ")).lower()
                if symptom == "none":
                    return False
                if symptom not in self.SymptomList2:
                    print(random.choice(mistakes))
                if symptom in self.SymptomList2:
                    break

        duration = int(input("How many days have you had this symptom? "))
        pain = int(input("On a scale from 1 to 10, how much discomfort does this cause you? "))
        tempsymptom = Symptom(symptom)
        tempsymptom.addSeverity(duration*pain)
        return tempsymptom
        
    def inLexicon(self, sentence, lexicon):
        sentence = sentence.lower()
        words = word_tokenize(sentence)
        important = [ps.stem(word) for word in words] # remove common words that we don't care about
        s = " ".join(important)
        for token in lexicon:
            if ps.stem(token) in s:
                return True
        return False

    def diagnose(self, patient):
        healthRating = 0
        symptoms = patient.getSymptoms()
        for asymptom in symptoms:
            healthRating += int(asymptom.getSeverity()) * int(self.SymptomList[asymptom.getName()])
        healthRating += patient.getAge()

        print("Analyzing results...")
        for i in range(1,8):
            time.sleep(.5)
            print("...")

        question = ["This may take a while. Any plans for the weekend?","While my diagnosis is being calculated. How's your week been?"]
        answer = input(random.choice(question)) 

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