from File1 import *
from File_Part3 import *

blocksize = 1000

def sortMerge(filename):

    '''
    OBJECTIVE :  To sort records of file1 and store them in f1.txt file
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''

    #APPROACH: sort and merge records of f1 & f2 in a group of blocksize and repeat until f2 is empty

    global blocksize

    f = open(filename, "rb")
    f1 = open("f1.txt", "wb")
    f2 = open("f2.txt", "wb")



    Loop = True
    while Loop:
        fkey1 = []
        fkey2 = []
        for i in range (0, blocksize):
            try :
                ob = pickle.load(f)
                fkey1.append(ob)
            except EOFError :
                Loop = False
            
        fkey1.sort(key = lambda Record : Record.get_key())
        for el in fkey1 :
            pickle.dump(el, f1)

        for i in range (0, blocksize):
            try :
                ob = pickle.load(f)
                fkey2.append(ob)
            except EOFError :
                Loop = False 
    
        fkey2.sort(key = lambda Record : Record.get_key())
        for el in fkey2 :
            pickle.dump(el, f2)
                
    f.close()
    f1.close()
    f2.close()


    
    while True:

        merge(blocksize,"f1.txt","f2.txt","f3.txt","f4.txt")
        if os.path.getsize("f2.txt") == 0:  # check if f2.txt is empty
            break
        blocksize *= 2

def display2() :

    '''
    OBJECTIVE :  To display records of f1 and f2 files
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''

    f1 = open("f1.txt", "rb")
    f2 = open("f2.txt", "rb")

    i = 1
    while True:
        try:
            ob = pickle.load(f1)
            print(str(i) + " f1")
            print(ob)
            i+=1
        except EOFError:
            break
    i=1
    while True:
        try:
            ob = pickle.load(f2)
            print(str(i) + " f2")
            print(ob)
            i+=1
        except EOFError:
            break

    f1.close()
    f2.close()


def display_sortRe(lower,upper):

    '''
    OBJECTIVE :  To display records of sorted file "f1.txt" given lower and upper range
    INPUT PARAMETERS :
            lower: lower limit for the range to display records
            upper: upper limit for the range to display records
    OUTPUT :
            None
    '''

    f1 = open("f1.txt", "rb")

    ob = pickle.load(f1)

    size = f1.tell()

    i = lower

    f1.seek( size * (lower-1) )

    print("Sorted:")
    
    while i <= upper:
        ob = pickle.load(f1)
        print("\nRecord Number: " + str(i) + ":")
        print(ob)
        i += 1

    f1.close()
   


def main() :

    writeRecord()

    sortMerge("file1.txt")

    while True :
    
        l = int(input("Enter lower limit: "))
        u = int(input("Enter Upper limit: "))

        if l <= N and u <= N:
            display_sortRe(l, u)
        else :
            print("Out of Range")
            continue

        check=int(input("enter 1 to see more else enter 0 : "))
        if check==0:
            break


if __name__ == "__main__":
       main()

   
    

              
