import sys
import os
import sys

def FileCopy(Fname):
    fobj1 = open("Demo.txt", "w")
    fobj2 = open("ABC.txt","r")
    demo = fobj2.read()
    fobj1.write(demo) 


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
            print("This File Is use to copy the content of one file to the another")

        else:
            FileCopy(sys.argv[1])
            print("Contents are Copied Successfully")
    else :
        print("Invalid Arguments")
        print("use --h for help")
        print("use --u for usage")
    
    print(Border)
    print("------------ Thank You For Using Our Script---------")
    print("--------------Marvellous Infosystems----------------")
    print(Border)



        

if __name__ =="__main__":
    main()