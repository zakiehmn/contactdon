from Contact import Contact
import string
import random
import json
class Contactdon:
    
    def __init__(self, contactDic = {}, fileName = 'contactdict.json', groups = []):
        self.contactDic = contactDic
        self.fileName = fileName
        self.groups = groups
        self.read_json(fileName)
        
              
    def add_contact(self, fName, lName, emailAddress, phoneNumber, id):
        newContact = Contact(fName, lName, emailAddress, phoneNumber, id)
        self.contactDic[id] = newContact
        # print(self.contactDic[id])
        return True
        
    # def input_command(self):
    #     UserInterface1 = UserInterface()
    #     splitCommand = UserInterface1.input()

    #     if(splitCommand[0] == "add"):
    #         statusAdd = self.add(splitCommand)
    #         self.print_result(statusAdd)

    #     if(splitCommand[0] == "search"):
    #         self.search(splitCommand[1])

    #     if(splitCommand[0] == "delete"):
    #         statusDel = self.delete(splitCommand[1])
    #         self.print_result(statusDel)

    #     if(splitCommand[0] == "update"):
    #         statusUpd = self.update(splitCommand)
    #         self.print_result(statusUpd)

    #     if(splitCommand[0] == "addgroup"):
    #         statusGroup = self.add_group(splitCommand)
    #         self.print_result(statusGroup)

    #     if(splitCommand[0] == "showgroup"):
    #         self.show_group(splitCommand[1])

    #     if(splitCommand[0] == "exit"):
    #         self.exit()

        
    #     self.other_command(splitCommand)
        
    #     self.input_command()
        
    # def print_result(self, status):
    #     UserInterface1 = UserInterface()
    #     UserInterface1.output(status)
   
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
              
    def add(self, paramsDict):
        # existF = False
        # existL = False
        # existE = False
        # existP = False
        # id=self.generate_id()
        # for x in range(len(splitCommand)):
        #     if(splitCommand[x] == "-f"):
        #         fname = splitCommand[x + 1]
        #         existF = True
        #     if(splitCommand[x] == "-l"):
        #         lname = splitCommand[x + 1]
        #         existL = True
        #     if(splitCommand[x] == "-e"):
        #         emailaddress = splitCommand[x + 1]
        #         existE=True
        #     if(splitCommand[x] == "-p"):
        #         phonenumber = splitCommand[x + 1]
        #         existP=True
        # if(self.check_exist_data(existF, existL, existE, existP)):
        #     if(self.check_unique_fnamelname(fname, lname) and self.check_correctPhoneNum(phonenumber) and self.check_correctEmail(emailaddress) ):
        #         self.add_contact(fname, lname, emailaddress, phonenumber,id)
        #         return True
        #     return False
        id=self.generate_id()
        if(len(paramsDict.keys()) == 4):
            if(self.check_unique_fnamelname(paramsDict["first name"], paramsDict["last name"]) and self.check_correctPhoneNum(paramsDict["phone number"]) and self.check_correctEmail(paramsDict["email address"]) ):
                self.add_contact(paramsDict["first name"], paramsDict["last name"], paramsDict["email address"], paramsDict["phone number"], id)
                return True
        return False

    # def check_exist_data(self, existF, existL, existE, existP):
    #     if(existF and existL and existE and existP):
    #         return True
    #     return False

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
                print(self.contactDic[contact])
        
        self.search_group(word)

    def delete(self, id):
        if(id in self.contactDic.keys()):
            self.contactDic.pop(id)
            return True
        return False
           
    def update(self, splitCommand):
        check = self.check_update(splitCommand)
        if(check == False):
            return False
        else:
            self.update_data(splitCommand)
            return True

    def check_update(self, splitCommand):
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
        return check

    def update_data(self, splitCommand):
         for x in range(len(splitCommand)):
                if(splitCommand[x] == "-f"):
                    self.contactDic[splitCommand[1]]._fName = splitCommand[x+1]
                if(splitCommand[x] == "-l"):
                    self.contactDic[splitCommand[1]]._lName = splitCommand[x+1]
                if(splitCommand[x] == "-e"):
                    self.contactDic[splitCommand[1]]._emailAddress = splitCommand[x+1]
                if(splitCommand[x] == "-p"):
                    self.contactDic[splitCommand[1]]._phoneNumber = splitCommand[x+1]
                
    def check_unique_fname(self, id, fname):
        for contact in self.contactDic:
            if(fname == self.contactDic[contact]._fName and self.contactDic[id]._lName == self.contactDic[contact]._lName):
                return False
        return True
        
    def check_unique_lname(self, id, lname):
        for contact in self.contactDic:
            if(lname == self.contactDic[contact]._lName and self.contactDic[id]._fName == self.contactDic[contact]._fName ):
                return False
        return True

    def check_unique_phonenum(self, phonenumber):
        for contact in self.contactDic:
            if(self.contactDic[contact]._phoneNumber == phonenumber):
                return False
        return True
       
    def check_unique_emailaddress(self, emailaddress):
        for contact in self.contactDic:
            if(self.contactDic[contact]._emailAddress == emailaddress):
                return False
        return True
      
    def other_command(self,splitCommand):
        if(splitCommand[0] != "add" and splitCommand[0] != "exit" and splitCommand[0] != "search" and splitCommand[0] != "update" and splitCommand[0] != "delete" and splitCommand[0] != "print" and splitCommand[0] != "addgroup" and splitCommand[0] != "showgroup"):
            print("command failed")

    def exit(self):
        self.write_json(self.fileName)
        quit()

    def add_group(self, splitCommand):
        groupContacts = []
        for x in range(len(splitCommand)):
            if(splitCommand[x] == "-n"):
                group_name = splitCommand[x+1]
            if(splitCommand[x] == "-c"):
                IDs = splitCommand[x+1]

        split_IDs = self.separate_IDs(IDs)
       
        if(len(split_IDs) != 0):
            self.add_ID_group(group_name, split_IDs)
            return True
        else:
            return False

            
    def separate_IDs(self, IDs):
        split_IDs = IDs.split(",")
        return split_IDs

    def add_ID_group(self, name, groupIDs):
        groupDict = {}
        groupDict[name] = groupIDs
        self.groups.append(groupDict)

    def show_group(self, name):
        for d in self.groups:
            if name in d.keys():
                for l in d.values():
                    for id in l:
                        print(self.contactDic[id])
                                
    def group_member(self, name):
        for d in self.groups:
            for group in d.keys():
                if(name == group):
                    idslist = d[group]
        
        return len(idslist)

    def search_group(self, word):
        for d in self.groups:
            for group in d.keys():
                if(group.startswith(word) or group.endswith(word)):
                    member = self.group_member(group)
                    print(group +"  " +  "members :"+ " " + str(member) )
                    

    def write_json(self, fileName):
        listDict = []
        for contact in self.contactDic.values():
            listDict.append(contact.__dict__)

        with open(fileName,'w') as fp:
            json.dump(listDict, fp)    
       
        with open("groupsList.json",'w') as g:
            json.dump(self.groups, g)
        
    def read_json(self, fileName):
        with open(fileName) as fp:
            listdict = json.load(fp)
            
        for i in range(len(listdict)):
            self.add_contact(listdict[i].get("_fName"), listdict[i].get("_lName"), listdict[i].get("_emailAddress"), listdict[i].get("_phoneNumber"), listdict[i].get("_ID"))

        with open("groupsList.json") as g:
            groupsDict = json.load(g)

        for dicti in groupsDict:
            self.groups.append(dicti)
        


        

