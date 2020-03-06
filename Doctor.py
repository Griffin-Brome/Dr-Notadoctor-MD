from patient import *

class Doctor:
    def __init__(self):
        pass

    def greet_user(self):
        print("Hello my name is Dr.310")
        print("I will try to help diagnse your symptoms")

    def get_basic_info(self):
        name = input("What is your name? ")
        age = input("How old are you? ")
        gender = input("What is your gender? ")
        return patient(name, age, gender)

    def get_symptom(self):
        symptomname = str(input("What is a symptom you are experiencing? (none for no more)"))
        if symptom == "none":
            return False
        else:
            return symptomname


    def get_severity(self):
        duration = int(input("How many days have you had this symptom?"))
        pain = int(input("On a scale from 1 to 5, how much discomfort does this cause you?"))
        return duration*pain





