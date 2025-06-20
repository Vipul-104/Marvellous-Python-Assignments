import psutil

def DisplayInfo(Name):
    Border = "*" * 52
    print(Border,"\n")
    print("Information of current Running Processes \n")
    print(Border)

    
    for proc in psutil.process_iter(['name']):
        try:
            if(proc.info['name'] == Name ):
                info = proc.as_dict(attrs=['pid','name'])
                print(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        

def main():
   print("Enter The Process Name")
   Pname = input()

   DisplayInfo(Pname)

if __name__ == "__main__":
    main()