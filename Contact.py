class Contact:
    
    def __init__(self,fName,lName,emailAddress,phoneNumber):
        self._fName=fName
        self._lName=lName
        self._emailAddress=emailAddress
        self._phoneNumber=phoneNumber

    def set_fName(self,fName):
        self._fName=fName

    def set_lName(self,lName):
        self._lName=lName

    def set_emailAddress(self,emailAddress):
        self._emailAddress=emailAddress

    def set_phoneNumber(self,phoneNumber):
        self._phoneNumber=phoneNumber

    def set_ID(self,ID):
        ID=ID+1
        self._ID=ID

    def get_fName(self):
        return self._fName

    def get_lName(self):
        return self._lName

    def get_emailAddress(self):
        return self._emailAddress

    def get_phoneNumber(self):
        return self._phoneNumber

    def get_ID(self):
        return self._ID


    
        
        

