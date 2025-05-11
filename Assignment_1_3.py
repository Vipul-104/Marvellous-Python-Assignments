def Addition(Value1, Value2):
    Ans = Value1 + Value2
    return Ans



def main():
    print("Enter the First No: ")
    No1 = int(input())

    print("Enter the Second No: ")
    No2 = int(input())

    result = Addition(No1,No2)

    print("The Addition Of Two Numbers is : ",result)


if __name__ == "__main__":
    main()