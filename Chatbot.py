from Symptom import Symptom
from patient import patient
from Doctor import Doctor

Doctor = Doctor()

Doctor.greet_user()
patient = Doctor.get_basic_info()


symptom = Symptom(str(Doctor.get_symptom()))
symptom.addSeverity(Doctor.get_severity())
patient.addSymptom(symptom)

symptom = Symptom(Doctor.get_symptom())
symptom.addSeverity(Doctor.get_severity())
patient.addSymptom(symptom)



print(patient.patientInfo())