import psutil
import os
import time

def CreateLog(Data):
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace(" /","_")

    Filename = ("Marvellous%s.log"%(timestamp))

    fobj = open(Filename,"w")

    border = '*'*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosystems Process Log\n")
    fobj.write("\t\tlog File Is Created At:"+time.ctime()+"\n")
    fobj.write(border)

    for value in Data:
        fobj.write("%s \n"%value)
        fobj.write("\n")

    fobj.write(border)
    fobj.close()

def ProcessDisplay():

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs = ['pid','name']) #tells it to include only the process ID (pid) and name in the dictionary.
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(info)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
   Arr =  ProcessDisplay()
   CreateLog(Arr)

   print("Log file is  Creates Successfully with all the running Files!!")

if __name__ == "__main__":
    main()