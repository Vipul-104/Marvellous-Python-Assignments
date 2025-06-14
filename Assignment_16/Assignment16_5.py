import sys
import os


def DisplayLines(Fname):
    
   
    fobj = open(Fname, "r")
    lines = fobj.readlines()

    for line in lines:
        line = line.replace("\n","")
        words = line.split(" ")
        count_words = 0
        for word in words:
            count_words = count_words + 1
        if(count_words>=5): 
            print("Line Having More Than 5 words:",line)

    fobj.close()

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
            print("This Program is use to Count Number Of Lines,Words and Characters")

    elif(sys.argv[0]):
            DisplayLines("Students.txt")
            print("File is readed  Successfully and Contents Are Displayed")
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