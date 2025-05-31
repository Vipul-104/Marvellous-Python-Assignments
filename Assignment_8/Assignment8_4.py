import threading

def CapCount(value):
    count = 0
    for i in value:
        if ("a" <= i <= "z"):
            count = count + 1
    print("the Count of small letters is:",count)


def SmallCount(value):
    count = 0
    for i in value:
        if ("A" <= i <= "Z"):
            count = count + 1
    print("the Count of Capital letters is:",count)



def DigitCount(value):
    count = 0
    for i in value:
        if ("0" <= i <= "9"):
            count = count + 1
    print("the Count of Digits is:",count)


def main():
    print("Enter the Element : ")
    element = input()

    Capital = threading.Thread(target=CapCount, args = (element,))
    Capital.start()
    Capital.join()

    Small = threading.Thread(target=SmallCount, args = (element,))
    Small.start()
    Small.join()

    Digit = threading.Thread(target=DigitCount, args=(element,))
    Digit.start()
    Digit.join()

if __name__ == "__main__":
    main()