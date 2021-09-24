from Contact import Contact
import string
import random
import json
class Contactdon:
    
    def __init__(self, contactDic = {}):
        self.contactDic = contactDic
        self.read_json()
              
    def add_contact(self, fName, lName, emailAddress, phoneNumber, id):
        newContact = Contact(fName, lName, emailAddress, phoneNumber, id)
        self.contactDic[id] = newContact
        return True
        
    def input_command(self):
        splitCommand = []
        inputCommand = input()
        splitCommand = inputCommand.split(" ")
        n = splitCommand.count("")
        for i in range(n):
            splitCommand.remove("")

        if(splitCommand[0] == "add"):
            statusAdd = self.add(splitCommand)
            self.print_result(statusAdd)

        if(splitCommand[0] == "search"):
            self.search(splitCommand[1])

        if(splitCommand[0] == "delete"):
            statusDel=self.delete(splitCommand[1])
            self.print_result(statusDel)

        if(splitCommand[0] == "update"):
            statusUpd=self.update(splitCommand)
            self.print_result(statusUpd)

        if(splitCommand[0] == "exit"):
            self.exit()
        self.other_command(splitCommand)
        
        self.input_command()
        
    def print_result(self, status):
        if(status):
            print("command ok")
        else:
            print("command failed")
   
    def check_uniqueID(self, id):
        if id in self.contactDic.keys():
            return False
        return True

    def generate_id(self):
        letters = string.digits
        id=''.join(random.choice(letters) for i in range(5))
        if(self.check_uniqueID(id)):
            return id
        return self.generate_id()
              
    def add(self, splitCommand):
        existF = False
        existL = False
        existE = False
        existP = False
        id=self.generate_id()
        for x in range(len(splitCommand)):
            if(splitCommand[x] == "-f"):
                fname = splitCommand[x+1]
                existF = True
            if(splitCommand[x] == "-l"):
                lname = splitCommand[x+1]
                existL = True
            if(splitCommand[x] == "-e"):
                emailaddress = splitCommand[x+1]
                existE=True
            if(splitCommand[x] == "-p"):
                phonenumber = splitCommand[x+1]
                existP=True
        if(self.check_exist_data(existF, existL, existE, existP)):
            if(self.check_unique_fnamelname(fname, lname) and self.check_correctPhoneNum(phonenumber) and self.check_correctEmail(emailaddress) ):
                self.add_contact(fname, lname, emailaddress, phonenumber,id)
                return True
            return False
        
    def check_exist_data(self, existF, existL, existE, existP):
        if(existF and existL and existE and existP):
            return True
        return False

    def check_unique_fnamelname(self, fname, lname):
        check=False
        n=len(self.contactDic)
        if(n>0):
            for contact in self.contactDic:
                if(self.contactDic[contact]._fName == fname and self.contactDic[contact]._lName == lname):
                    return False
        return True

    def check_correctPhoneNum(self, phonenumber):
        if(phonenumber.isdigit() and phonenumber.startswith("09") and len(phonenumber) == 11):
            return True
        return False

    def check_correctEmail(self, emailaddress):
        if "@" in emailaddress and "." in emailaddress:
            if(emailaddress.find("@") < emailaddress.find(".")):
                return True
            return False
        else:
            False

    def search(self, word):
        for contact in self.contactDic:
            if(self.contactDic[contact]._fName.startswith(word) or self.contactDic[contact]._lName.startswith(word) or self.contactDic[contact]._emailAddress.startswith(word) or self.contactDic[contact]._phoneNumber.startswith(word) or self.contactDic[contact]._fName.endswith(word) or self.contactDic[contact]._lName.endswith(word) or self.contactDic[contact]._emailAddress.endswith(word) or self.contactDic[contact]._phoneNumber.endswith(word)):
                # self.print_contact(self.contactDic[contact]._ID)
                print(self.contactDic[contact])
           
    # def print_contact(self, id):
    #     print("{} {} {} {} {}".format(self.contactDic[id]._ID , self.contactDic[id]._fName , self.contactDic[id]._lName , self.contactDic[id]._emailAddress , self.contactDic[id]._phoneNumber ))

    def delete(self, id):
        if(id in self.contactDic.keys()):
            self.contactDic.pop(id)
            return True
        return False
           
    def update(self, splitCommand):
        check = True
        if(not (splitCommand[1] in self.contactDic.keys())):
            check = False
        for i in range(len(splitCommand)):
            if(splitCommand[i] == "-f"):
                if(self.check_unique_fname(splitCommand[1], splitCommand[i+1]) == False):
                    check = False
            if(splitCommand[i] == "-l"):
                if(self.check_unique_lname(splitCommand[1], splitCommand[i+1]) == False):
                    check = False
            if(splitCommand[i] == "-e"):
                if(self.check_unique_emailaddress(splitCommand[i+1])==False or self.check_correctEmail(splitCommand[i+1]) == False):
                    check = False
            if(splitCommand[i] == "-p"):
                if(self.check_unique_phonenum(splitCommand[i+1]) == False or self.check_correctPhoneNum(splitCommand[i+1]) == False):
                    check = False

        if(check == False):
            return False
        else:
            for x in range(len(splitCommand)):
                if(splitCommand[x] == "-f"):
                    self.contactDic[splitCommand[1]]._fName = splitCommand[x+1]
                if(splitCommand[x] == "-l"):
                    self.contactDic[splitCommand[1]]._lName = splitCommand[x+1]
                if(splitCommand[x] == "-e"):
                    self.contactDic[splitCommand[1]]._emailAddress = splitCommand[x+1]
                if(splitCommand[x] == "-p"):
                    self.contactDic[splitCommand[1]]._phoneNumber = splitCommand[x+1]
            return True
                
    def check_unique_fname(self, id, fname):
        for contact in self.contactDic:
            if(fname == self.contactDic[contact]._fName and self.contactDic[id]._lName == self.contactDic[contact]._lName):
                return False
        return True
        
    def check_unique_lname(self, id, lname):
        for contact in self.contactDic:
            if(lname == self.contactDic[contact]._lName and self.contactDic[id]._fName == self.contactDic[contact]._fName ):
                return False

    def check_unique_phonenum(self, phonenumber):
        for contact in self.contactDic:
            if(self.contactDic[contact]._phoneNumber == phonenumber):
                return False
       
    def check_unique_emailaddress(self, emailaddress):
        for contact in self.contactDic:
            if(self.contactDic[contact]._emailAddress == emailaddress):
                return False
      
    def other_command(self,splitCommand):
        if(splitCommand[0] != "add" and splitCommand[0] != "exit" and splitCommand[0] != "search" and splitCommand[0] != "update" and splitCommand[0] != "delete" and splitCommand[0] != "print"):
            print("command failed")

    def exit(self):
        self.write_json()
        quit()

    def write_json(self):
        listDict = []
        for contact in self.contactDic.values():
            listDict.append(contact.__dict__)

        with open('contactdict.json','w') as fp:
            json.dump(listDict, fp)
            

    def read_json(self):
        with open('contactdict.json') as fp:
            listdict = json.load(fp)
            
        for i in range(len(listdict)):
                self.add_contact(listdict[i].get("_fName"), listdict[i].get("_lName"), listdict[i].get("_emailAddress"), listdict[i].get("_phoneNumber"), listdict[i].get("_ID"))


        

