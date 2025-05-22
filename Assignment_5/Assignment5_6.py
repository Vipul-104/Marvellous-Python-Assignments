def TempConvertor(value):
    result = (value * 9/5) + 32
    return result

def main():
    print("Enter the Temperature In Celcius : ")
    temp = int(input())

    ret = TempConvertor(temp)

    print("The Temperature in Fahrenheit:",ret)
    
if __name__ == "__main__":
        main()