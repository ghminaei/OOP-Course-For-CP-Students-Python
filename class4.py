class Student:
    gardes = None

    def __init__(self, n, i):
        self.name = n
        self.id = i
    
    def setGrades(self, gradeList):
        self.gardes = gradeList

    def getGpa(self):
        allSum = 0
        for i in self.gardes:
            allSum += i
        allSum = allSum / len(self.gardes)
        return allSum

s1 = Student("Maryam", "810296274")
s2 = Student("Ali", "810196683")
s1.setGrades([80, 90, 20])
s2.setGrades([40, 70, 20])
print(s1.gardes)
print(s2.gardes)
print(s1.name, end = " ")
print(s1.getGpa())
print(s2.name, end = " ")
print(s2.getGpa())
