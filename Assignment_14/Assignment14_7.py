class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.Salary = salary
        self.Subject = subject

def main():
    obj = Teacher("Vipul",20,"Automation",1000000)
    print(f"{obj.Name}\n{obj.Age}\n{obj.Subject}\n{obj.Salary}")

if __name__ == "__main__":
    main()
   
        