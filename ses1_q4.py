# Write a program in Python that defines the following classes: Student, Test, and Sport.
# The Student class should contain attributes for the student's name and age,
# and a method to display this information.

# The Test class should inherit from the Student class and add attributes for the
# test name and test score, along with a method to display the test results.

# The Sport class should be independent of Student and should store attributes
# for the sport name and sport score, along with a method to display the sport results.

# The Result class should inherit from both Test and Sport, combining the
# functionalities of both parents. This class should display the student's
# information, test results, and sports results using the appropriate methods.
# Use super() for calling the parent class constructors and ensure that the
# program works correctly when creating an instance of the Result class.


class Student:
    def __init__(self, s_name, age):
        self.s_name = s_name
        self.age = age
    def display_student_info(self):
        print(f"Student Name: {self.s_name}")
        print(f"Student Age: {self.age}")

class Test(Student):
    def __init__(self, s_name, age, test_name, test_score):
        super().__init__(s_name, age)
        self.test_name = test_name
        self.test_score = test_score
    def display_test_result(self):
        print(f"Test Name: {self.test_name}")
        print(f"Test Score: {self.test_score}")
    
class Sport:
    def __init__(self, sport_name, sport_score):
        self.sport_name = sport_name
        self.sport_score = sport_score
    def display_sport_result(self):
        print(f"Sport Name: {self.sport_name}")
        print(f"Sport Score: {self.sport_score}")

class Result(Test, Sport):
    def __init__(self, s_name, age, test_name, test_score, sport_name, sport_score):
        super().__init__(s_name, age, test_name, test_score)
        Sport.__init__(self, sport_name, sport_score)
    def display_result(self):
        self.display_student_info()
        self.display_test_result()
        self.display_sport_result()

student1 = Result("Jeet", 23, "Sess 1", 48, "BGMI", 98)
student1.display_result()