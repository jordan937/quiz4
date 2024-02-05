from typing import Protocol

class Info(Protocol):

    def grade_calculation(self):
        pass

    def display_info(self, hw1, hw2):
        pass

class StudentA:

    def __init__(self):
        self.name = "Jo"
    
    def grade_calculation(self, hw1, hw2):
        self.score = (hw1 + hw2) / 2

    def display_info(self):
        print(self.name, "your average is:", self.score)

class StudentB:

    def __init__(self, name):
        self.name = name
    
    def grade_calculation(self, hw1, hw2 ):
        self.score = (hw1 + hw2) / 2

    def display_info(self):
        print(self.name, "your average is:", self.score)

def main():

    str = "test_Dummy"
    checkInfo : Info = StudentB(str) #<-- Magic
    checkInfo.grade_calculation(99, 100)
    checkInfo.display_info()
    print(checkInfo.name)


if __name__=="__main__":
    main()
