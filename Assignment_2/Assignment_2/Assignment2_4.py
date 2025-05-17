def factors(Value):
    
    result = []

    for i in range(1,Value):
        if Value%i == 0:
            result.append(i)
    print(result)

    ans = 0
    for i in range (len(result)):
        ans = ans + result[i]
    return ans







def main():
    print("Enter tHe Number:")
    No = int(input())
    ret = factors(No)
    print("The Addition of the factors is: ",ret)



if __name__ =="__main__":
    main()