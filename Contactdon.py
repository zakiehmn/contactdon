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
           
    def update(self, paramsDict):
        check = self.check_update(paramsDict)
        if(check == False):
            return False
        else:
            self.update_data(paramsDict)
            return True

    def check_update(self, paramsDict):
        check = True
        if(not (paramsDict["id"] in self.contactDic.keys())):
            check = False
        for key in paramsDict.keys():
            if(key == "first name"):
                if(self.check_unique_fname(paramsDict["id"], paramsDict["first name"]) == False):
                    check = False
            if(key == "last name"):
                if(self.check_unique_lname(paramsDict["id"], paramsDict["last name"]) == False):
                    check = False
            if(key == "email address"):
                if(self.check_unique_emailaddress(paramsDict["email address"]) == False or self.check_correctEmail(paramsDict["email address"]) == False):
                    check = False
            if(key == "phone number"):
                if(self.check_unique_phonenum(paramsDict["phone number"]) == False or self.check_correctPhoneNum(paramsDict["phone number"]) == False):
                    check = False
        return check

    def update_data(self, paramsDict):
        for key in paramsDict.keys():
            if(key == "first name"):
                self.contactDic[paramsDict["id"]]._fName = paramsDict["first name"]
            if(key == "last name"):
                self.contactDic[paramsDict["id"]]._lName = paramsDict["last name"]
            if(key == "email address"):
                self.contactDic[paramsDict["id"]]._emailAddress = paramsDict["email address"]
            if(key == "phone number"):
                self.contactDic[paramsDict["id"]]._phoneNumber = paramsDict["phone number"]

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
        


        

