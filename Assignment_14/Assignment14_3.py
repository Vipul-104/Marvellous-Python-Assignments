class Book:
    def __init__(self,price):
        self.__price = price

    def setPrice(self,price):
        self.__price = price

    def Display(self):
        print("The price of Book is :",self.__price)


def main():
    obj1 = Book(1000)
    obj1.Display()
    obj2 = Book(2000)
    obj2.Display()
    obj1.__price=5000   #Cananot work becoz price is private
    obj1.Display()
if __name__ == "__main__":
    main()







