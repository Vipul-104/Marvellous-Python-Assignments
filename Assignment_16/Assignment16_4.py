import sys
import os

def NumFile(num,Filename):
    fobj = open(Filename,"w")
    for i in num:
        fobj.write((i)+"\n")

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
            print("This Program is use to Write The Numbers Into thr Files")

    elif(sys.argv[0]):
        data = []
        print("Enter The File Name:")
        Fname = input()

        print("Enter 10 Numbers:")
        for no in range(10):
            no1 = input()
            data.append(no1)
            
        print("Entered Numbers Are:",data)
        NumFile(data,Fname)
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