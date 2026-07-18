class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def get_average(self):
        total = 0
        total = sum(self.grade)
        average = total/len(self.grade)
        return average
    def add_grade(self,grade):
        self.grade.append(grade)
s1 = Student("VIGHNESH",[90,78,85])
print(s1.get_average())
s1.add_grade(85)
print(s1.get_average()) 

# suggestion use if else to avoid error of zero division
    