from Contact import Contact
class Contactdon:
    
    def __init__(self,contactList):
        self.contactList=contactList


    def add_contact(self,fName,lName,emailAddress,phoneNumber):
        newContact=Contact(fName,lName,emailAddress,phoneNumber)
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
        if(splitCommand[0]=="add"):
            for x in range(len(splitCommand)):
                if(splitCommand[x]=="-f"):
                    fname=splitCommand[x+1]
                if(splitCommand[x]=="-l"):
                    lname=splitCommand[x+1]
                if(splitCommand[x]=="-e"):
                    emailaddress=splitCommand[x+1]
                if(splitCommand[x]=="-p"):
                    phonenumber=splitCommand[x+1]
        else:
            print("command failed")
        self.add_contact(fname, lname, emailaddress, phonenumber)

    # def printdata(self,fname,lname,emailaddress,phonenumber):
    #     print(fname,lname,emailaddress,phonenumber)
    # def printlist(self):
    #     print(self.contactList[0]._fName)

    

