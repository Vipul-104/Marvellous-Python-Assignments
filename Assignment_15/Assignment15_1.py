import os
def main():
    print("Enter the Filename:")
    Filename = input()

    Ret = os.path.exists(Filename)
    if(Ret == True):
        print("The File Is Exist In Your Current Directory")

    else:
        print("The File is not Exist In the Current Directory")
if __name__ == "__main__":
    main()