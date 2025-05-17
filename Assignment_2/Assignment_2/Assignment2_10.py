def AddDig(Value):
    ans = 0
    for i in range(len(Value)):
        ans = ans + int(Value[i])
    return ans




def main():
    print("Enter the No:")
    No = (input())


    ret = AddDig(No)
    print("The  Addition of Digits is:",ret)


if __name__ == "__main__":
    main()