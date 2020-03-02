from Symptom import *
from patient import *

first = Symptom("Cough")
first.addCat("Lung")
first.addSeverity(8)

#print(first.toString())

secondSymptom = Symptom("Pharyngitis")
secondSymptom.addCat("Throat")
secondSymptom.addSeverity(4)

#print(secondSymptom.toString())


patient1 = patient("Bob", 29, "Male")
patient1.addSymptom(first)
patient1.addSymptom(secondSymptom)

patient1.patientInfo()

patient2 = patient("Joe", 29, "Male")
patient2.addSymptom(first)
third = Symptom("Fatigue")
third.addCat("neurological")
third.addSeverity(10)
patient2.addSymptom(third)

patient2.patientInfo()

