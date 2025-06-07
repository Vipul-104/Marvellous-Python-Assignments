class Rectangle:

    def __init__(self):

        print("Enter the Length of Rectangle:")
        self.length = int(input())
        print("Enter the Breadth of Rectangle:")
        self.breadth = int(input())


    def CalculateArea(self):
        Area = self.length * self.breadth
        print("The Area Of Rectangle Is:",Area)

    def CalculatePeri(self):
        Perimeter = (2 * self.length) + (2 * self.breadth)
        print("The Perimeter Of Rectangle Is:",Perimeter)

def main():
    obj1 = Rectangle()
    obj1.CalculateArea()
    obj1.CalculatePeri()


if __name__ == "__main__":
    main()


