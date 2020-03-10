from patient import patient
from Doctor import Doctor

Doctor = Doctor()


class Chatbot:
    def startChat(self):
        # greets patient and creates patient object
        Doctor.greet_user()
        patient = Doctor.get_basic_info()

        # Loop to get symptoms, right now breaks on "none"
        while True:
            symptom = Doctor.new_symptom()
            if (symptom == False):
                break
            patient.addSymptom(symptom)
            print("Okay, I will remember that...")

        Doctor.diagnose(patient)
