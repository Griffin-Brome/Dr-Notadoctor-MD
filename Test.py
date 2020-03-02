from Symptom import *

first = Symptom("Cough")
first.addCat("Lung")
first.addSeverity(8)

print(first.toString())

secondSymptom = Symptom("Pharyngitis")
secondSymptom.addCat("Throat")
secondSymptom.addSeverity(4)

print(secondSymptom.toString())

