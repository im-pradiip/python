import pickle, os
import random
from classrecord import *
##import timeit

N = 100000



def writeRecord():

    '''
    OBJECTIVE :  To write records in file1
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''

    #Approach: Dump Record object in file.txt 

    f = open("file1.txt", "wb")
    keyList = []
    i = 1

    
    while i <= N:
        key = random.randint(10000000, 20000000)
        if key not in keyList:
            keyList.append(key)
            val = str(key) * 3 #random.randint(100,200)
            i = i+1
            if i%10000==0:
                print(str(i)+"records ")

            ob = Record(key, val)
            pickle.dump(ob, f)

                
    f.close()
    

def display(lower,upper):

    '''
    OBJECTIVE :  To display records of origional file "file1.txt" given lower and upper range
    INPUT PARAMETERS :
            lower: lower limit for the range to display records
            upper: upper limit for the range to display records
    OUTPUT :
            None
    '''

    f1 = open("file1.txt", "rb")

    ob = pickle.load(f1)

    size = f1.tell()

    i = lower

    f1.seek( size * (lower-1) )

    print("File1:")
    
    while i <= upper:
        ob = pickle.load(f1)
        print("\nRecord Number: " + str(i) + ":")
        print(ob)
        i += 1

    f1.close()


def main() :

    writeRecord()

    while True :
    
        lower= int(input("Enter lower limit: "))
        upper = int(input("Enter Upper limit: "))

        if lower<= N and upper<= N:
            display(lower, upper)
        else :
            print("Out of Range")
            continue

        more = input("\nEnter 'Y' to see more else Enter 'N': ")
        if more == 'n' or more == 'N' :
            break

if __name__ == "__main__":
       main()

   

