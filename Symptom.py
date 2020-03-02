class Symptom:
    def __init__(self, name):
        self.category = "undefined"
        self.severity = "undefined"
        self.name = name

    def addCat(self, category):
        self.category = category

    def addSeverity(self, severity):
        self.severity = severity

    def toString(self):
        print("Name: " + self.name + ", Severity = " + str(self.severity) + ", Category: " + self.category)



