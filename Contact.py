class Contact:
    
    def __init__(self, fName, lName, emailAddress, phoneNumber, ID):
        self._fName = fName
        self._lName = lName
        self._emailAddress = emailAddress
        self._phoneNumber = phoneNumber
        self._ID = ID

    def __str__(self):
       return '{} {} {} {}'.format(self._ID, self._fName, self._lName, self._emailAddress, self._phoneNumber)

   


    
        
        

