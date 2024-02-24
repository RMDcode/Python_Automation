from sys import *
import os
import hashlib
import time

def DeleteFiles(dict1):
    reults = list(filter(lambda X : len(x)>1,dict1.values()))

    icnt=0
    iFound=0

    if len(results>0):
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
                    iFound+=1
            icnt = 0
        print("")
    else:
        print("No Duplicates files found.")

def hashfile(path, blocksize=1024):
    fd = open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf=fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists = os.path.isdir(path)

    dups={}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is :"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        
        return dups
    else:
        print("Invalid Path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x : len(x)>1,dict.values()))

    if len(results) > 0:
        print("Duplicates Found :")

        print("The following files are identical.")

        icnt=0
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)               
    else:
        print("No duplicate file found.")

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr={}
        startTime = time.time()
        arr=FindDuplicate(argv[1])
        PrintDuplicate(arr)
        DeleteFiles(arr)
        endTime=time.time()

        print('Took %s second to evaluate.'% (endTime-startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()
