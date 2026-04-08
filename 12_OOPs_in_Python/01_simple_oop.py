# Define a class
class Student:
    
    # Constructor (initializer)
    def __init__(self, name):
        self.name = name
        self.grades = (90, 90, 93, 78, 90)
    
    # Method to calculate average grade
    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# Create object (instance)
student = Student("Bob")

# Access attributes
print(student.name)

# Call method
print(student.average_grade())