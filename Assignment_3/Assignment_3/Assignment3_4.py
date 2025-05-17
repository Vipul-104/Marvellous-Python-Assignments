def ChkFrq(nos,key):
   count = 0
   for i in range(len(nos)):
        
        if(nos[i] == key):
            count = count+1
        
   return count



def main():
    print("Enter the Size:")
    size = int(input())

    data = list()

    print("Enter the Elements: ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)


    print("Enter the Element That you want to search : ")
    value = int(input())
    

    ret = ChkFrq(data,value)
    print("Frequency of the number is : ",ret)



if __name__ == "__main__":
    main()