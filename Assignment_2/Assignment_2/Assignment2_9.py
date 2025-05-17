def CountDig(Value):
    for i in range(len(Value)):
        count = i + 1
    return count




def main():
    print("Enter the No:")
    No = (input())


    ret = CountDig(No)
    print("The Digit Cout is:",ret)


if __name__ == "__main__":
    main()