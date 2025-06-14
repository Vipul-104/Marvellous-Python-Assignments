import sys
import os


def DisplayCounting(Fname):
   
    fobj = open(Fname, "r")
    lines = fobj.readlines()

    count_words = 0
    count_char = 0
    for line in lines:
        count_char = count_char + len(line)
        words = line.split(" ")
        for word in words:
            count_words = count_words + 1

    print("Number Of Lines",len(lines))
    print("Number Of Words",count_words)
    print("Number Of Characters",count_words)

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
            DisplayCounting("Students.txt")
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