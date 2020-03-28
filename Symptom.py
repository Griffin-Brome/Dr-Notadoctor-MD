# Symptom class:
# When a symptom is created it should be passed a string "name"
# When created, the category and severity are set as "undefined" until manually updated

class Symptom:
    def __init__(self, name):
        self.category = "undefined"
        self.severity = "undefined"
        self.name = name

    # addCat() expects a string "category" and updates accordingly
    def addCat(self, category):
        self.category = category

    # addSeverity expects an int/double (TBD) "severity" and updates accordingly
    def addSeverity(self, severity):
        self.severity = severity

    def getSeverity(self):
        return int(self.severity)

    def getName(self):
        return self.name
    # toString() returns a String summarizing the Symptom
    def toString(self):
        return ("Name: " + self.name + ", Severity = " + str(self.severity))



