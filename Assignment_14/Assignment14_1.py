class Employee:
    def __init__(self,A,B,C):
        self.name = A
        self.ID = B
        self.salary = C

    def Display(self):
        print("Name:",self.name,"ID:","Salary:",self.salary)
        
        

def main():

    obj1 = Employee("Rohit",101,5000)
    obj1.Display()

    obj2 = Employee("Vipul",104,40000)
    obj2.Display()



if __name__ == "__main__":
    main()