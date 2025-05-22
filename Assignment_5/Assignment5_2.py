
def CheckChar(value):
    if (value=="a" or value=="e" or value=="e" or value=="o" or value=="u"): 
        return True


def main():
    print("Enter the Character: ")
    char = input()

    Ret = CheckChar(char)
    if Ret == True:
        print(char,"is a Vowel")

    else:
        print(char,"is a Consonent")


if __name__ == "__main__":
    main()