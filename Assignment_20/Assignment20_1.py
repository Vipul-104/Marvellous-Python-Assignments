import os
import sys
import time
import hashlib


def CalculateCheckSum(path, BlockSize = 1024):
    fobj = open(path,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0 ):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
     
     flag = os.path.isabs(DirectoryName)

     if(flag == False):
         DirectoryName = os.path.abspath(DirectoryName)

     flag = os.path.exists(DirectoryName)
     
     if(flag == False):
         print("The path is Invalid ")
         exit()

     flag = os.path.isdir(DirectoryName)

     if(flag == False):
         print("The path is valid but not Directory")
         exit()


     for FolderName , SubFolderNames,  Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateCheckSum(fname)     
            print("File name is",fname)
            print("Checksum is:",checksum)  
            print()     

     


def main():
    Border = "-"*52
    print(Border)
    print("--------------Marvellous Automation-----------------")
    print(Border)
   
    if(len(sys.argv)== 2): 
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application Is Used To Perform directory Cleaning")
            print("This Is The Directory Automation Script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use The given Script as:")
            print("ScripName.py NameOfDirectory")
            print("Pleease Provide Valid Absolute path")

        else:
            DirectoryWatcher(sys.argv[1])
           
            
    else:
        print("Invalid Number of Command line Arguments")
        print("Use the Given Flag As :")
        print("--h : Used to display help")
        print("--u : Used to display usage")

    print(Border)
    print("------------ Thank You For Using Our Script---------")
    print("--------------Marvellous Infosystems----------------")
    print(Border)


if __name__ == "__main__":
    main()