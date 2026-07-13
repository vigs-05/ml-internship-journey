

class Student:
    # This is a special method that runs automatically when you create a student
    def __init__(self, name, branch, year):
        self.name = name        # Saving the name
        self.branch = branch    # Saving the branch
        self.year = year        # Saving the year
        
    # This is a normal function inside a class (called a method)
    def introduce(self):
        print(f"Hi! I am {self.name}, studying {self.branch} in {self.year} year.")
        
    def goal(self):
        print("My goal is to get an ML Internship in 3rd Year!")

# --- MAIN PROGRAM ---

# Creating a student object (You are the student!)
vignesh = Student("Vignesh Jadhav", "AIML", "Second")

# Calling the functions
vignesh.introduce()
vignesh.goal()

print("\nDay 1 Task Completed! ✅")