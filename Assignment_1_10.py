def getLength(data):

    for i in range(len(data)):
       
        i = 1 + i
        return i



def main():

    print("ENter the name : ")
    name = input()

    ret = getLength(name)

    print("The length of Name is : ",ret)

    
      


if __name__ == "__main__":
    main()