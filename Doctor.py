class Doctor:
    
    def greet_user():
        print("Hello my name is Dr.310")
        print("I will try to help diagnose your symptoms")

    def get_basic_info():
        name = input("What is your name?")
        age = input("How old are you?")
        gender = input("What is your gender?")
        medicalHistory = input("Do you have any prior medical conditions?")

    def get_symptom():
        symptom = input("What is a symptom you are experiencing?")
        rating = 0
        symptom.lower()
<<<<<<< HEAD

        if ("cough" in symptom):
            rating = 2
        elif ("sore throat" in symptom):
            rating = 3
        elif("headache" in symptom):
            rating = 1
        elif("fever" in symtom):
            rating = 4
        elif("rash" in symptom):
            rating = 2
        else:
            print("Symptom was not recognized")

        print(rating)
        return rating

    def get_severity():
        duration = int(input("How many days have you had this symptom?"))
        pain = int(input("On a scale from 1 to 5, how much dicomfort does this cause you?"))
        return duration  * pain

    def diagnose():
        return sympt * severity
=======

        if ("cough" in symptom):
            rating = 2
        elif ("sore throat" in symptom):
            rating = 3
        elif("headache" in symptom):
            rating = 1
        elif("fever" in symtom):
            rating = 4
        elif("rash" in symptom):
            rating = 2
        else:
            print("Symptom was not recognized")

        print(rating)
        return rating

    def get_severity():
        duration = int(input("How many days have you had this symptom?"))
        pain = int(input("On a scale from 1 to 5, how much dicomfort does this cause you?"))
        return duration  * pain



    def diagnose():
        
        return sympt * severity

>>>>>>> Patrick's

    diagnose()