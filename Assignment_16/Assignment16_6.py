import sys
import os


def CopyContent(Source, Destination):
    if(os.path.exists(Source)):
        Sobj = open(Source,"r")
        data = Sobj.read()
        Sobj.close()
    else:
        print("The SourceFile Is Not Exist")

    if(os.path.exists(Destination)):
        Dobj = open(Destination,"w")
        Dobj.write(data)
        print("Contents Are Copied Successfully!!")
        Dobj.close()
    else:
        print("The DestinationFile is Not Exist")
       

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
            print("This Program is use to Copy The Contents Of One Into Another")

    elif(len(sys.argv) == 3):
        CopyContent(sys.argv[1],sys.argv[2])
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