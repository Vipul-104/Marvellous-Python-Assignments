class Employee:
    def __init__(self,salary,department,name):
        self.__salary = salary
        self._Department = department
        self.Name = name

    def Display(self):
        print("salary:",self.__salary)
        print("departmet:",self._Department)
        print("Name:",self.Name)


def  main():
    obj = Employee(50000,"AIDS","Vipul")
    obj.Display()

    #print(obj.__salary)   Not Accesible
    print(obj._Department)
    print(obj.Name)

if __name__ == "__main__":
    main()