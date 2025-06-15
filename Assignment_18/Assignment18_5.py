import os
import sys


def CountFrequency(FileName, keyword):
    count = 0
    fobj =open(FileName, "r") 
    lineList = fobj.readlines()
    for line in lineList :
        wordlist = line.split(" ")
        for word in  wordlist:
            if(word == keyword):
                count = count + 1
    return count

        

def main():


    Border = "-"*52
    print(Border)
    print("--------------Marvellous Automation-----------------")
    print(Border)

    if (len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("Welcome To help Section")
            print("Scripting FileName  Argument1 Argument2")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Welcome To Usege Section")
            print("This File Is Use To Count Frequency Of the Keyword Given")

    elif(len(sys.argv) == 3):
        ret = CountFrequency((sys.argv[1]),(sys.argv[2]))
        print("The frequency of",sys.argv[2],"in file",sys.argv[1],"is",ret)

    else :
        print("Invalid Arguments")
        print("use --h for help")
        print("use --u for usage")
    
    print(Border)
    print("------------ Thank You For Using Our Script---------")
    print("--------------Marvellous Infosystems----------------")
    print(Border)


if __name__ == "__main__":
    main()