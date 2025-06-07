class Student:
    school_name = "SSVMC Interntional"

    def __init__(self,name, rollNo):
        self.name = name
        self.roll_no = rollNo
    
    def Display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
        print("School Name Is:",Student.school_name)

    def NewSchoolName(self, NewName):
        Student.school_name = NewName
        print("The New School name is:",Student.school_name)

def main():
    obj1 = Student("Vipul",104)
    obj1.Display()

    obj2 = Student("Aayush",105)
    obj2.Display()
    obj2.NewSchoolName("Vidyaniketan")

if __name__ == "__main__":
    main()


        