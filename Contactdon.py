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
        if(splitCommand[0]=="print"):
            self.print_list()
        self.add_command(splitCommand)
        self.search_command(splitCommand)
        self.command()
        
        
    def add_command(self,splitCommand):
        if(splitCommand[0]=="add"):
            id=self.generate_id()
            for x in range(len(splitCommand)):
                if(splitCommand[x]=="-f"):
                    fname=splitCommand[x+1]
                if(splitCommand[x]=="-l"):
                    lname=splitCommand[x+1]
                if(splitCommand[x]=="-e"):
                    emailaddress=splitCommand[x+1]
                if(splitCommand[x]=="-p"):
                    phonenumber=splitCommand[x+1]
            if(self.check_unique(fname, lname, emailaddress, phonenumber)==True):
                self.add_contact(fname, lname, emailaddress, phonenumber,id)
            else:
                print("command failed")

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

    def search_command(self,splitCommand):
        if(splitCommand[0]=="search"):
            for x in range(len(self.contactList)):
                if(self.contactList[x]._fName.startswith(splitCommand[1]) or self.contactList[x]._lName.startswith(splitCommand[1]) or self.contactList[x]._emailAddress.startswith(splitCommand[1]) or self.contactList[x]._phoneNumber.startswith(splitCommand[1]) or self.contactList[x]._fName.endswith(splitCommand[1]) or self.contactList[x]._lName.endswith(splitCommand[1]) or self.contactList[x]._emailAddress.endswith(splitCommand[1]) or self.contactList[x]._phoneNumber.endswith(splitCommand[1])):
                    self.print_contact(x)

    # def start_end_with(self,splitCommand,x):
    #     if(self.contactList[x]._fName.startswith(splitCommand[1] or self.contactList[x]._lName.startswith(splitCommand[1] or self.contactList[x]._emailAddress.startswith(splitCommand[1] or self.contactList[x]._phoneNumber.startswith(splitCommand[1] or self.contactList[x]._fName.endswith(splitCommand[1] or self.contactList[x]._lName.endswith(splitCommand[1] or self.contactList[x]._emailAddress.endswith(splitCommand[1] or self.contactList[x]._phoneNumber.endswith(splitCommand[1]):
    #          self.print_contact(x)

    def print_contact(self, indexContact):
        print("{} {} {} {} {}".format(self.contactList[indexContact]._ID , self.contactList[indexContact]._fName,self.contactList[indexContact]._lName , self.contactList[indexContact]._emailAddress , self.contactList[indexContact]._phoneNumber ))



    def print_list(self):
        for i in range(len(self.contactList)):
            print(self.contactList[i]._ID)
            print(self.contactList[i]._fName)
            print(self.contactList[i]._lName)
            print(self.contactList[i]._emailAddress)
            print(self.contactList[i]._phoneNumber)

    


    # def printdata(self,fname,lname,emailaddress,phonenumber):
    #     print(fname,lname,emailaddress,phonenumber)
    # def printlist(self):
    #     print(self.contactList[0]._fName)

    

