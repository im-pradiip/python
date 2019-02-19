class Record :
    '''
    DESCRIPTON : To create an object of type 'Record'
    ATTRIBUTES : key, nonkey
    '''

    def __init__(self, key, nonkey):
        '''
        OBJECTIVE : To initialize an Record object
        INPUT PARAMETERS :
                self : (Implicit) Record object
                key : key value of the object Record
                nonkey : value corresponding to that key
        OUTPUT :
                None
        '''

        #Appoach: key = key  & nonkey = nonkey

        self.key = key 
        self.nonkey = nonkey

    def get_key(self):

        '''
        OBJECTIVE: To get key value of the Record object
        INPUT PARAMETERS:
                 self: (Implicit) Record Object
        OUTPUT :
                 None
        '''

        return self.key


    def __str__(self):
        '''
        OBJECTIVE: To return a string of the values of the object Record
        INPUT PARAMETERS :
                self : (Implicit) Record object
        OUTPUT : 
                a string representing the Record object
        '''

        return "Key: "+str(self.key) + "\tnonkey: " + str(self.nonkey)

