class BookStore:
    NoOfBooks = 0
    def __init__(self):

        print("Enter the name of Book :")
        self.Name = input()
        print("Enter the Auther Name :")
        self.Author = input()

        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.Name,"by",self.Author)
        print("Number of Books :",BookStore.NoOfBooks)

def main():
    obj1 = BookStore()
    obj1.Display()

    obj2 = BookStore()
    obj2.Display()
        
if __name__ == "__main__":
    main()        