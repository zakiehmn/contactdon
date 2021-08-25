from Contact import Contact
import string
import random
class Contactdon:
    
    def __init__(self,contactList):
        self.contactList=contactList


    def add_contact(self,fName,lName,emailAddress,phoneNumber,id):
        newContact=Contact(fName,lName,emailAddress,phoneNumber,id)
        self.contactList.append(newContact)
        print("command ok")
        # self.printlist()
        # self.printdata(fName,lName,emailAddress,phoneNumber)

    def command(self):
        splitCommand=[]
        inputCommand=input()
        splitCommand=inputCommand.split(" ")
        n=splitCommand.count("")
        for i in range(n):
            splitCommand.remove("")
        self.add_command(splitCommand)
        self.search_command(splitCommand)
        self.delete_command(splitCommand)
        self.update_command(splitCommand)
        self.other_command(splitCommand)
        self.command()
        
        
    def add_command(self,splitCommand):
        existF=False
        existL=False
        existE=False
        existP=False
        if(splitCommand[0]=="add"):
            id=self.generate_id()
            for x in range(len(splitCommand)):
                if(splitCommand[x]=="-f"):
                    fname=splitCommand[x+1]
                    existF=True
                if(splitCommand[x]=="-l"):
                    lname=splitCommand[x+1]
                    existL=True
                if(splitCommand[x]=="-e"):
                    emailaddress=splitCommand[x+1]
                    existE=True
                if(splitCommand[x]=="-p"):
                    phonenumber=splitCommand[x+1]
                    existP=True
            if(self.checkFLEP(existF, existL, existE, existP)):
                if(self.check_unique(fname, lname, emailaddress, phonenumber) and self.check_correctPhoneNum(phonenumber) and self.check_correctEmail(emailaddress) ):
                    self.add_contact(fname, lname, emailaddress, phonenumber,id)
            else:
                print("command failed")

    def checkFLEP(self,existF,existL,existE,existP):
        if(existF and existL and existE and existP):
            return True
        else:
            return False

    

    def generate_id(self):
        unique=True
        n=len(self.contactList)
        letters=string.digits
        id=''.join(random.choice(letters) for i in range(5))
        if(n>0):
            for i in range(n):
                if(self.contactList[i]==id):
                    unique=False
        if(unique):
            return id
        else:
            self.generate_id()
       
        

    def check_unique(self,fname,lname,emailaddress,phonenumber):
        check=False
        n=len(self.contactList)
        checkfnln=True
        for j in range(n):
            if(self.contactList[j]._fName==fname and self.contactList[j]._lName==lname):
                    checkfnln=False
        if(n==0):
           check=True
        if(n>0):
            for i in range(n):
                if(checkfnln==True and self.contactList[i]._emailAddress!=emailaddress and self.contactList[i]._phoneNumber!=phonenumber):
                    check=True
                else:
                    check=False

        return check

    def check_correctPhoneNum(self,phonenumber):
        if(phonenumber.isdigit() and phonenumber.startswith("09") and len(phonenumber)==11):
            return True
        else:
            return False

    def check_correctEmail(self, emailaddress):
        if "@" in emailaddress and "." in emailaddress:
            if(emailaddress.find("@")<emailaddress.find(".")):
                return True
            else:
                return False
        else:
            False

    def search_command(self,splitCommand):
        if(splitCommand[0]=="search"):
            for x in range(len(self.contactList)):
                if(self.contactList[x]._fName.startswith(splitCommand[1]) or self.contactList[x]._lName.startswith(splitCommand[1]) or self.contactList[x]._emailAddress.startswith(splitCommand[1]) or self.contactList[x]._phoneNumber.startswith(splitCommand[1]) or self.contactList[x]._fName.endswith(splitCommand[1]) or self.contactList[x]._lName.endswith(splitCommand[1]) or self.contactList[x]._emailAddress.endswith(splitCommand[1]) or self.contactList[x]._phoneNumber.endswith(splitCommand[1])):
                    self.print_contact(x)


    def print_contact(self, indexContact):
        print("{} {} {} {} {}".format(self.contactList[indexContact]._ID , self.contactList[indexContact]._fName,self.contactList[indexContact]._lName , self.contactList[indexContact]._emailAddress , self.contactList[indexContact]._phoneNumber ))



    def delete_command(self,splitCommand):
        if(splitCommand[0]=="delete"):
            indexD=self.search_id(splitCommand)
            if(indexD!=None):
                self.contactList.pop(indexD)
                print("command ok")
            else:
                print("command failed")

    def update_command(self,splitCommand):
        check=True
        # checkE=True
        if(splitCommand[0]=="update"):
            indexU=self.search_id(splitCommand)
           
            if(indexU!=None):
                for x in range(len(splitCommand)):
                    if(splitCommand[x]=="-p"):
                        if(self.check_correctPhoneNum(splitCommand[x+1])==False):
                            check=False
                            
            if(indexU!=None):
                for x in range(len(splitCommand)):
                    if(splitCommand[x]=="-e"):
                        if(self.check_correctEmail(splitCommand[x+1])==False):
                            check=False
            if(indexU==None or check==False ):
                print("command failed")
            else:       
                for x in range(len(splitCommand)):
                    if(splitCommand[x]=="-f"):
                        self.contactList[indexU].set_fName(splitCommand[x+1])
                    if(splitCommand[x]=="-l"):
                        self.contactList[indexU].set_lName(splitCommand[x+1])
                    if(splitCommand[x]=="-e"):
                        self.contactList[indexU].set_emailAddress(splitCommand[x+1])
                    if(splitCommand[x]=="-p"):
                        self.contactList[indexU].set_phoneNumber(splitCommand[x+1])
                print("command ok")


    def search_id(self,splitCommand):
        for x in range(len(self.contactList)):
                if(splitCommand[1]==self.contactList[x]._ID):
                    return x


    def print_list(self):
        for i in range(len(self.contactList)):
            print(self.contactList[i]._ID)
            print(self.contactList[i]._fName)
            print(self.contactList[i]._lName)
            print(self.contactList[i]._emailAddress)
            print(self.contactList[i]._phoneNumber)

    def other_command(self,splitCommand):
        if(splitCommand[0]!="add" and splitCommand[0]!="search" and splitCommand[0]!="update" and splitCommand[0]!="delete"):
            print("command failed")


    # def printdata(self,fname,lname,emailaddress,phonenumber):
    #     print(fname,lname,emailaddress,phonenumber)
    # def printlist(self):
    #     print(self.contactList[0]._fName)

    

