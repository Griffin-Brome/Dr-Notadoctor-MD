from patient import patient
from Doctor import Doctor

Doctor = Doctor()

#greets patient and creates patient object
Doctor.greet_user()
patient = Doctor.get_basic_info()


#Loop to get symptoms, right now breaks on "none"
while True:
    symptom = Doctor.new_symptom()
    if(symptom == False):
        break
    patient.addSymptom(symptom)
    print("Okay, ill remember that...")

<<<<<<< HEAD:Chatbot.py
Doctor.diagnose(patient)
=======
        Doctor.diagnose(patient)
>>>>>>> 2317ad6ac54479044454aa972c70fe5b7d256ffd:python/Chatbot.py
