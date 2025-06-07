class Product:
    def __init__(self,name,price):
        self.Name = name
        self.Price = price

    def __eq__(self, value):
        if(self.Price == value.Price):
            return True
        
        else:
            return False
        


def main():
    obj1 = Product("Book",50)
    obj2 = Product("Chair",500)
    obj3 = Product("Colors",50)

    print(obj1 == obj2)
    print(obj2 == obj3)
    print(obj1 == obj3)


if __name__ == "__main__":
    main()