import sys
import os


def DisplayContent(Fname):
    fobj = open(Fname, "r")
    ret = os.path.exists(Fname)
    if(ret == True): 
        data = fobj.read()
        print(data)
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
            print("This Program is use to Create The File and Write the contents")

    elif(sys.argv[0] == "Assignment16_2.py"):
            DisplayContent("data.txt")
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