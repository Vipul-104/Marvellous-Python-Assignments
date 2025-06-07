class Numbers : 
    def __init__(self):
        print("Enter the number : ")
        self.Value = int(input())
        
    def ChkPrime(self):
        i = 2
        while(i <= int(self.Value/2)):
            if(self.Value % i == 0):
                return False
            i += 1
        return True

    def ChkPerfect(self):
        i = 1
        Perfect = 0
        while(i <= int(self.Value/2)):
            if(self.Value % i == 0):
                Perfect = Perfect + i
            i = i + 1
        
        if(Perfect == self.Value):
            return True
                
        
        return False

    def Factors(self):
        i = 1
        Ans = []
        while(i <= self.Value):
            if(self.Value % i == 0):
                Ans.append(i)
            i += 1
        return Ans

    
    def SumFactors(self):
        Result = Numbers.Factors(self)
        Sum = 0
        for i in Result:
            Sum = Sum + int(i)

        return Sum
    
def main():
    obj = Numbers()
    Ans = obj.ChkPerfect()
    if(Ans):
        print("It is a Perfect Number")
    else:
        print("It is not a Perfect Number")

    Ans = obj.ChkPrime()
    if(Ans):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

    Ans = obj.Factors()
    print("The factors are : ", Ans)

    Ans = obj.SumFactors()
    print("The Sum of the Factors is : ", Ans)


if __name__ == "__main__":
    main()