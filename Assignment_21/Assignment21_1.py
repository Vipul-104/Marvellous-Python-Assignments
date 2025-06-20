import psutil

def ProcessDisplay():
    Border = "*" * 52
    print(Border,"\n")
    print("Information of current Running Processes \n")
    print(Border)

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs = ['pid','name']) #tells it to include only the process ID (pid) and name in the dictionary.
            print(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
   Arr =  ProcessDisplay()
   for value in Arr:
       print(value)

if __name__ == "__main__":
    main()