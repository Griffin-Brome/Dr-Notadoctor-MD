# Patient Class initialised with name, age, gender
# addSymptom expects a symptom object created elsewhere, and adds it to a list of symptoms
# patientInfo() prints out the patient name and each symptom and its info...

class patient:
    def __init__(self, name, age, gender):
        self.name = str(name)
        self.age = int(age)
        self.gender = str(gender)
        self.symptoms = []

    def addSymptom(self, symptom):
        self.symptoms.append(symptom)

    def getSymptoms(self):
        return self.symptoms

    def patientInfo(self):
        print("--------- START OF PATIENT ---------")
        print(("PATIENT INFO: " + "Name: " + self.name + " Age " + str(self.age) + " Gender: " + self.gender))
        for i in self.symptoms:
            print(i.toString())
        print("--------- END OF PATIENT ---------")




