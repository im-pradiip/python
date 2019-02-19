from File1 import *

def merge(blocksize,f1,f2,f3,f4):

    '''
    OBJECTIVE :  To sort and merge records of f1.txt and f2.txt
    INPUT PARAMETERS :
            blocksize: current blocksize
    OUTPUT :
            None
    '''

    f1 = open(f1, "rb")
    f2 = open(f2, "rb")
    f3 = open(f3, "wb")
    f4 = open(f4, "wb")

    flag = True
    start = True
    
    while start:
        
        if flag == True:
            fil = f3
            flag = False
        else:
            fil = f4
            flag = True

        count1 = count2 = 0

        try :
            ob1 = pickle.load(f1)
        except EOFError:
            ob1 = None
            count1 = blocksize + 1
            start= False
            
        try :
            ob2 = pickle.load(f2)
        except EOFError:
            ob2 = None
            count2 = blocksize + 1
            start = False

        while count1 < blocksize and count2 < blocksize :
            
            if ob1.get_key() <= ob2.get_key() :
                pickle.dump(ob1,fil)
                #print(str(ob1.get_key()) + " pushed: fg1= " + str(fg1) + " * ")                
                count1 += 1
                if count1 < blocksize:
                    try :
                        ob1 = pickle.load(f1)
                    except EOFError:
                        start = False
                        count1 = blocksize + 1
                        break
            else :
                pickle.dump(ob2,fil)
                #print(str(ob2.get_key()) + " pushed: fg2= " + str(fg2) + " * ")
                count2 += 1
                if count2 < blocksize:
                    try :
                        ob2 = pickle.load(f2)
                    except EOFError:
                        start = False
                        count2 = blocksize + 1
                        break

        while count1 < blocksize :
            pickle.dump(ob1,fil)
            #print(str(ob1.get_key()) + " pushed: fg1= " + str(fg1) + " ; ")    
            count1 += 1
            if count1 < blocksize:
                try :
                    ob1 = pickle.load(f1)
                except EOFError:
                    start = False
                    break

        while count2 < blocksize :
            pickle.dump(ob2,fil)
            #print(str(ob2.get_key()) + " pushed: fg2= " + str(fg2) + " ; ")
            count2 += 1
            if count2 < blocksize:
                try :
                    ob2 = pickle.load(f2)
                except EOFError:
                    start = False
                    break

 
    try:
        f1.close()
        f2.close()
        f3.close()
        f4.close()
    except :
       print("Closing Error")

    try:
        os.remove("f1.txt")
        os.remove("f2.txt")
        os.rename("f3.txt", "f1.txt")
        os.rename("f4.txt", "f2.txt")
    except :
        print("Error")

