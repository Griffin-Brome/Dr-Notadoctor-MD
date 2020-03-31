from patient import patient
from Symptom import Symptom
import time

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
        pass

    def greet_user(self):
        print("Hello my name is Dr.310")
        print("I will try to help diagnose your overall health based on your symptoms")

    def get_basic_info(self):
        name = input("What is your name? ")
        age = input("Hello " + name + "! How old are you? ")
        gender = input("What is your gender? ")
        return patient(name, age, gender)

    def new_symptom(self):
        while True:
            symptom = str(input("What is a symptom you are experiencing? (say none for no more) ")).lower()
            if symptom == "none":
                return False
            if symptom not in self.SymptomList:
                print("Sorry, I don't recognise " + symptom)
            if symptom in self.SymptomList:
                break
        duration = int(input("How many days have you had this symptom? "))
        pain = int(input("On a scale from 1 to 10, how much discomfort does this cause you? "))
        tempsymptom = Symptom(symptom)
        tempsymptom.addSeverity(duration*pain)
        return tempsymptom

    def diagnose(self, patient):
        healthRating = 0
        symptoms = patient.getSymptoms()
        for asymptom in symptoms:
            healthRating += int(asymptom.getSeverity()) * int(self.SymptomList[asymptom.getName()])
        healthRating += patient.getAge()

        print("Analyzing symptoms...")

        for asymptom in symptoms:
            print(asymptom.getName())
            time.sleep(.5)
            print("...")
            time.sleep(.5)



        print("Well " + patient.getName() + "...")
        if healthRating > 75:
            print("I suggest you go to a real doctor")
        elif healthRating > 50:
            print("I think you should get some rest and talk to me again tomorrow")
        else:
            print("You seem pretty healthy to me!")









