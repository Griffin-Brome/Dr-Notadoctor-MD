from Symptom import *
from patient import *

#Creating first Symptom
first = Symptom("Cough")
first.addCat("Lung")
first.addSeverity(8)

# Creating Second Symptom
secondSymptom = Symptom("Pharyngitis")
secondSymptom.addCat("Throat")
secondSymptom.addSeverity(4)

# Creating first patient
patient1 = patient("Bob", 29, "Male")
# Adding symptom objects to Patient
patient1.addSymptom(first)
patient1.addSymptom(secondSymptom)
# Get patient info(Auto prints)
patient1.patientInfo()

# Creating Second Patient
patient2 = patient("Joe", 29, "Male")

# Adding symptom object to patient
patient2.addSymptom(first)
# Creating third Symptom
third = Symptom("Fatigue")
third.addCat("neurological")
third.addSeverity(10)
# Adding symptom to patient
patient2.addSymptom(third)

# Get patient info(Auto prints)
patient2.patientInfo()

