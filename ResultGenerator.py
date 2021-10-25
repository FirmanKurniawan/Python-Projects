from prettytable import PrettyTable
# creating a class called student
class Student:
    # constructor is setting values to the respective variables
    def __init__(self,name1,maths, chem, phy, computer, english):
        self.name = name1
        self.maths = maths
        self.chem = chem
        self.computer = computer
        self.phy = phy
        self.english = english

    def check_status(self):
        # this method checks the the grade of student and marks him accordingly
        percentage = ((self.maths + self.english + self.chem + self.phy + self.computer)*100)/500
        total=(self.maths + self.english + self.chem + self.phy + self.computer)
        if (self.phy and self.chem and self.maths and self.computer and self.english) > 33 and percentage > 90 and percentage < 100:
            table.add_row([self.name,self.maths,self.phy,self.chem,self.computer,self.english,total,percentage,'Passed','A+'])
        elif self.phy > 33 and self.chem > 33 and self.maths > 33 and self.computer > 33 and self.english > 33 and percentage > 80 and percentage < 90:
            table.add_row([self.name,self.maths,self.phy,self.chem,self.computer,self.english,total,percentage,'Passed','A'])
        elif self.phy > 33 and self.chem > 33 and self.maths > 33 and self.computer > 33 and self.english > 33 and percentage > 70 and percentage < 80:
            table.add_row([self.name,self.maths,self.phy,self.chem,self.computer,self.english,total,percentage,'Passed','B'])
        elif self.phy > 33 and self.chem > 33 and self.maths > 33 and self.computer > 33 and self.english > 33 and percentage > 60 and percentage < 70:
            table.add_row([self.name,self.maths,self.phy,self.chem,self.computer,self.english,total,percentage,'Passed','C'])
        else:
            table.add_row([self.name,self.maths,self.phy,self.chem,self.computer,self.english,total,percentage,'Failed','F'])

if __name__ == '__main__':
    # creating object of the class PrettyTable
    table = PrettyTable(['Name','Maths', 'Physics', 'Chemistry', 'Computer', 'English', 'Total', 'Percentage', 'Status','Grade'])
    # setting variable for iterating while loop, its value is '1' by default, user will overwrite it according to his need
    choice=1
    # asking the user number of students that he wants to enter the marks for
    students=int(input("How many students do you want to enter?\n"))
    while choice <= students:
        # inputting data for generating result
        name = input("Enter student name of Student:\n")
        name1=name
        mth = int(input("MATHS MARKS: "))
        phy = int(input("PHY MARKS: "))
        chem = int(input("CHEM MARKS: "))
        com = int(input("COMPUTER MARKS: "))
        eng = int(input("ENGLISH MARKS: "))
        name= Student(name1,mth,chem,phy,com,eng)
        name.check_status()
        choice+=1
    # printing the result of each student
    print(table)

