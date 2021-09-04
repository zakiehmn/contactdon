from Contact import Contact
import string
import random
import csv
class Contactdon:
    
    def __init__(self,contactDic={}):
        self.contactDic=contactDic
        


    def add_contact(self,fName,lName,emailAddress,phoneNumber,id):
        newContact=Contact(fName,lName,emailAddress,phoneNumber,id)
        self.contactDic[id] = newContact
        print("command ok")
        

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
        print_command(self, splitCommand)
        self.other_command(splitCommand)
        self.command()
        
        
    # def add_command(self,splitCommand):
    #     existF=False
    #     existL=False
    #     existE=False
    #     existP=False
    #     if(splitCommand[0]=="add"):
    #         id=self.generate_id()
    #         for x in range(len(splitCommand)):
    #             if(splitCommand[x]=="-f"):
    #                 fname=splitCommand[x+1]
    #                 existF=True
    #             if(splitCommand[x]=="-l"):
    #                 lname=splitCommand[x+1]
    #                 existL=True
    #             if(splitCommand[x]=="-e"):
    #                 emailaddress=splitCommand[x+1]
    #                 existE=True
    #             if(splitCommand[x]=="-p"):
    #                 phonenumber=splitCommand[x+1]
    #                 existP=True
    #         if(self.checkFLEP(existF, existL, existE, existP)):
    #             if(self.check_unique(fname, lname, emailaddress, phonenumber) and self.check_correctPhoneNum(phonenumber) and self.check_correctEmail(emailaddress) ):
    #                 self.add_contact(fname, lname, emailaddress, phonenumber,id)
    #             else:
    #                 print("command failed")

    def checkFLEP(self,existF,existL,existE,existP):
        if(existF and existL and existE and existP):
            return True
        return False

    

    # def generate_id(self):
    #     unique=True
    #     # n=len(self.contactList)
    #     letters=string.digits
    #     id=''.join(random.choice(letters) for i in range(5))
    #     if(n>0):
    #         for i in range(n):
    #             if(self.contactList[i]==id):
    #                 unique=False
    #     if(unique):
    #         return id
    #     else:
    #         self.generate_id()

    def check_uniqueID(self, id):
        if id in self.contactDic.keys():
            return False
        return True

    def generate_id(self):
        letters=string.digits
        id=''.join(random.choice(letters) for i in range(5))
        if(self.check_uniqueID(id)):
            return id
        return self.generate_id()
       

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
                if(self.check_unique_fnln(fname, lname) and self.check_correctPhoneNum(phonenumber) and self.check_correctEmail(emailaddress) ):
                    self.add_contact(fname, lname, emailaddress, phonenumber,id)
                else:
                    print("command failed")
        

    def check_unique_fnln(self, fname, lname):
        check=False
        n=len(self.contactDic)
        if(n>0):
            for contact in self.contactDic:
                if(self.contactDic[contact]._fName==fname and self.contactDic[contact]._lName==lname):
                    return False
        return True

    #     check=False
    #     checkfnln=True
    #     for j in range(n):
    #         if(self.contactList[j]._fName==fname and self.contactList[j]._lName==lname):
    #                 checkfnln=False
    #     if(n==0):
    #        check=True
    #     if(n>0):
    #         for i in range(n):
    #             if(checkfnln==True and self.contactList[i]._emailAddress!=emailaddress and self.contactList[i]._phoneNumber!=phonenumber):
    #                 check=True
    #             else:
    #                 check=False
                    
    #     return check

    def check_correctPhoneNum(self,phonenumber):
        if(phonenumber.isdigit() and phonenumber.startswith("09") and len(phonenumber)==11):
            return True
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
            for contact in self.contactDic:
                if(self.contactDic[contact]._fName.startswith(splitCommand[1]) or self.contactDic[contact]._lName.startswith(splitCommand[1]) or self.contactDic[contact]._emailAddress.startswith(splitCommand[1]) or self.contactDic[contact]._phoneNumber.startswith(splitCommand[1]) or self.contactDic[contact]._fName.endswith(splitCommand[1]) or self.contactDic[contact]._lName.endswith(splitCommand[1]) or self.contactDic[contact]._emailAddress.endswith(splitCommand[1]) or self.contactDic[contact]._phoneNumber.endswith(splitCommand[1])):
                    self.print_contact(self.contactDic[contact]._ID)
            # for x in range(len(self.contactList)):
            #     if(self.contactList[x]._fName.startswith(splitCommand[1]) or self.contactList[x]._lName.startswith(splitCommand[1]) or self.contactList[x]._emailAddress.startswith(splitCommand[1]) or self.contactList[x]._phoneNumber.startswith(splitCommand[1]) or self.contactList[x]._fName.endswith(splitCommand[1]) or self.contactList[x]._lName.endswith(splitCommand[1]) or self.contactList[x]._emailAddress.endswith(splitCommand[1]) or self.contactList[x]._phoneNumber.endswith(splitCommand[1])):
            #         self.print_contact(x)


    def print_contact(self, id):
        print("{} {} {} {} {}".format(self.contactDic[id]._ID , self.contactDic[id]._fName , self.contactDic[id]._lName , self.contactDic[id]._emailAddress , self.contactDic[id]._phoneNumber ))



    def delete_command(self,splitCommand):
        if(splitCommand[0]=="delete"):
            if(splitCommand[1] in self.contactDic.keys()):
                self.contactDic.pop(splitCommand[1])
                print("command ok")
            else:
                print("command failed")
            # indexD=self.search_id(splitCommand)
            # if(indexD!=None):
            #     self.contactList.pop(indexD)
            #     print("command ok")
            # else:
            #     print("command failed")

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

            for x in range(len(splitCommand)):
                    if(splitCommand[x]=="-f"):
                        if(self.check_uniqueUF(indexU,splitCommand[x+1])==False):
                            check=False

            for x in range(len(splitCommand)):
                    if(splitCommand[x]=="-l"):
                        if(self.check_uniqueUL(indexU,splitCommand[x+1])==False):
                            check=False

            for x in range(len(splitCommand)):
                    if(splitCommand[x]=="-p"):
                        if(self.check_uniqueUP(indexU,splitCommand[x+1])==False):
                            check=False

            for x in range(len(splitCommand)):
                    if(splitCommand[x]=="-e"):
                        if(self.check_uniqueUE(indexU,splitCommand[x+1])==False):
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


    def check_uniqueUF(self,indexU,fname):
        for i in range(len(self.contactList)):
            if(fname==self.contactList[i]._fName and self.contactList[indexU]._lName==self.contactList[i]._lName ):
                return False


    def check_uniqueUL(self,indexU,lname):
        for i in range(len(self.contactList)):
            if(lname==self.contactList[i]._lName and self.contactList[indexU]._fName==self.contactList[i]._fName ):
                return False

    def check_uniqueUP(self,indexU,phonenumber):
         for i in range(len(self.contactList)):
             if(self.contactList[i]._phoneNumber==phonenumber ):
                 return False

    def check_uniqueUE(self,indexU,emailaddress):
        for i in range(len(self.contactList)):
             if(self.contactList[i]._emailAddress==emailaddress):
                 return False


    # def search_id(self, id):
        
        # for x in range(len(self.contactList)):
        #         if(splitCommand[1]==self.contactList[x]._ID):
        #             return x


    def print_list(self):
        for i in range(len(self.contactList)):
            print(self.contactList[i]._ID)
            print(self.contactList[i]._fName)
            print(self.contactList[i]._lName)
            print(self.contactList[i]._emailAddress)
            print(self.contactList[i]._phoneNumber)

    def other_command(self,splitCommand):
        if(splitCommand[0]!="add" and splitCommand[0]!="search" and splitCommand[0]!="update" and splitCommand[0]!="delete" and splitCommand[0]!="print"):
            print("command failed")

def print_command(self,splitCommand):
    if(splitCommand[0]=="print"):
        print(self.contactDic.items())
    

