from Symptom import Symptom
from patient import patient
from Doctor import Doctor

Doctor = Doctor()

#greets patient and creates patient object
Doctor.greet_user()
patient = Doctor.get_basic_info()


#Loop to get symptoms, right now breaks on "none"
while True:
    symptomname = Doctor.get_symptom()
    if not symptomname:
        break

    symptom = Symptom(symptomname)
    symptom.addSeverity(Doctor.get_severity())
    patient.addSymptom(symptom)

#creates list of symptom objects
mysymptoms = patient.getSymptoms()

print(mysymptoms[0].toString())

print(patient.patientInfo())