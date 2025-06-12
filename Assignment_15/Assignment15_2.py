
import os
def main():
    print("Enter the Filename:")
    Filename = input()

    Ret = os.path.exists(Filename)
    if(Ret == True):
        fobj = open(Filename, "r")
        demo = fobj.read()
        print(demo)

    else:
        print("The File is not Exist In the Current Directory")

   

if __name__ =="__main__":
    main()