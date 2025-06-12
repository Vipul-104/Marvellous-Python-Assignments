import sys
import os
import filecmp

def CompareFile(File1,File2):
    if(os.path.isabs(File1) == False):
        File1 = os.path.abspath(File1)

    if(os.path.isabs(File2) == False):
        File1 = os.path.abspath(File2)

    if(os.path.exists(File1) == False):
        exit()
    if(os.path.exists(File2) == False):
        exit()

    if(os.path.isfile(File1) == False):
        print("Path Is Valid but its not a file")

    if(os.path.isfile(File2) == False):
        print("Path Is Valid but its not a file")

    ret = filecmp.cmp(File1,File2)
    return ret

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

    elif(len(sys.argv) == 3):
        ret = CompareFile((sys.argv[1]),(sys.argv[2]))
        if(ret == True):
            print("The File Content is same")
        else:
            print("The File Contelnt is not same")

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