def CheckPrime(Value):
    count = 0
    for i in range(1,Value+1):
        if (Value % i) == 0:
            count = count+1
    if count > 2:
        return False
    else:
        return True
