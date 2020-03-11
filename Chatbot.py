from patient import patient
from Doctor import Doctor

Doctor = Doctor()

#greets patient and creates patient object
Doctor.greet_user()
patient = Doctor.get_basic_info()


#Loop to get symptoms, right now breaks on "none"
while True:
    symptom = Doctor.new_symptom()
    if not symptom:
        break
    patient.addSymptom(symptom)
    print("Okay, ill remember that...")

Doctor.diagnose(patient)
