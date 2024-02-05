from abc import ABC, abstractmethod

class Info(ABC):

    @abstractmethod
    def grade_calculation(self):
        pass

    @abstractmethod
    def display_info(self, hw1, hw2):
        pass

class StudentA(Info):

    def __init__(self):
        self.name = "Jo"
    
    def grade_calculation(self, hw1, hw2):
        self.score = (hw1 + hw2) / 2

    def display_info(self):
        print(self.name, "your average is:", self.score)

class StudentB(Info):

    def __init__(self, name):
        self.name = name
    
    def grade_calculation(self, hw1, hw2 ):
        self.score = (hw1 + hw2) / 2

    def display_info(self):
        print(self.name, "your average is:", self.score)

def main():

    str = "Mara"
    Student = StudentB(str)
    Student.grade_calculation(99, 50)
    Student.display_info()

if __name__=="__main__":
    main()
