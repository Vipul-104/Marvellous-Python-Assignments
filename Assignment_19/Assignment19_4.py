import os
import sys
import time
import shutil  # Use to copy the files into the another Directory


def DirectoryWatcher(DirectoryName, DestinationDirectoryName,Extention):
    if(os.path.isabs(DirectoryName) == False):
          DirectoryName = os.path.abspath(DirectoryName)

    if(os.path.exists(DirectoryName) == False):
         print("Path is Invalid")
         exit()

    if(os.path.isdir(DirectoryName) == False):
         print("Path is Valid But it's not a Directory")

    os.mkdir(DestinationDirectoryName)

    for FolderName,SubFolderNames,FileNames in os.walk(DirectoryName):
         for fname in FileNames:
              count = 0
              SourceDirectorypath = os.path.join(FolderName,fname)
              NewDirectoryath = os.path.join(DestinationDirectoryName,fname)
              if(fname.endswith(Extention)):
                   shutil.copy(SourceDirectorypath, NewDirectoryath )
                   count = count + 1
    if(count == 0):
            print("No files With Such Extension")
    else:
         print("The Files Are Successfully Copied Into",sys.argv[2],"Folder!!")


def  main():
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
            print("ScripName.py NameOfDirectory NameOfSecondDirectory ")
            print("Pleease Provide Valid Absolute path")

    elif(len(sys.argv)== 4): 
            DirectoryWatcher(sys.argv[1],sys.argv[2],sys.argv[3])
           
            
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