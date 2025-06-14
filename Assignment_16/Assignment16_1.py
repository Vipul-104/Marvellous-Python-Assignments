import sys
import os


def CreateFile(Fname):
    fobj = open(Fname, "w")
    ret = os.path.exists(Fname)
    if(ret == True): 
        fobj.write("Gara Barmukh\nNaruto Musale\nKakashi Chavan\n Rachit londhe\nSoham Uzumaki")

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

        else:
            CreateFile(sys.argv[1])
            print("File is created Successfully and Contents Are written")
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