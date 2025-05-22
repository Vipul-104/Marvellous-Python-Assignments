def main():
    fact = 1
    print("Enter the number")
    no = int(input())


    for i in range(1, no+1):
        
        fact = fact * i

    print("The factorial of no is: ",fact)





if __name__ == "__main__":
    main()