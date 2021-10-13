from Contact import Contact
from Group import Group 
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
        return True
        
    def check_uniqueID(self, id):
        if id in self.contactDic.keys():
            return False
        return True

    # move to utils
    def generate_id(self):
        letters = string.digits
        id=''.join(random.choice(letters) for i in range(5))
        if(self.check_uniqueID(id)):
            return id
        return self.generate_id()
              
    def add(self, paramsDict):
        id=self.generate_id()
        if(len(paramsDict.keys()) == 4):
            if(self.check_unique_fnamelname(paramsDict["first_name"], paramsDict["last_name"]) and 
               self.check_correctPhoneNum(paramsDict["phone_number"]) and self.check_correctEmail(paramsDict["email_address"]) ):
                self.add_contact(paramsDict["first_name"], paramsDict["last_name"],
                paramsDict["email_address"], paramsDict["phone_number"], id)
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
            if(self.contactDic[contact]._fName.startswith(word) 
               or self.contactDic[contact]._lName.startswith(word)
               or self.contactDic[contact]._emailAddress.startswith(word) 
               or self.contactDic[contact]._phoneNumber.startswith(word)
               or self.contactDic[contact]._fName.endswith(word) 
               or self.contactDic[contact]._lName.endswith(word) 
               or self.contactDic[contact]._emailAddress.endswith(word) 
               or self.contactDic[contact]._phoneNumber.endswith(word)):
            #    move to interface
                print(self.contactDic[contact])
        
        self.search_group(word)

    def delete(self, id):
        if(id in self.contactDic.keys()):
            self.contactDic.pop(id)
            return True
        return False
           
    def update(self, paramsDict):
        check = self.check_update_params(paramsDict)
        if(check == False):
            return False
        else:
            self.update_contact(paramsDict)
            return True
# check update params
    def check_update_params(self, paramsDict):
        check = True
        if(not (paramsDict["id"] in self.contactDic.keys())):
            check = False
        for key in paramsDict.keys():
            if(key == "first_name"):
                if(self.check_unique_fname(paramsDict["id"], paramsDict["first_name"]) == False):
                    check = False
            if(key == "last_name"):
                if(self.check_unique_lname(paramsDict["id"], paramsDict["last_name"]) == False):
                    check = False
            if(key == "email_address"):
                if(self.check_unique_emailaddress(paramsDict["email_address"]) == False or self.check_correctEmail(paramsDict["email_address"]) == False):
                    check = False
            if(key == "phone_number"):
                if(self.check_unique_phonenum(paramsDict["phone_number"]) == False or self.check_correctPhoneNum(paramsDict["phone_number"]) == False):
                    check = False
        return check

    def update_contact(self, paramsDict):
        for key in paramsDict.keys():
            if(key == "first_name"):
                self.contactDic[paramsDict["id"]]._fName = paramsDict["first_name"]
            if(key == "last_name"):
                self.contactDic[paramsDict["id"]]._lName = paramsDict["last_name"]
            if(key == "email_address"):
                self.contactDic[paramsDict["id"]]._emailAddress = paramsDict["email_address"]
            if(key == "phone_number"):
                self.contactDic[paramsDict["id"]]._phoneNumber = paramsDict["phone_number"]

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
        if(splitCommand[0] != "add" and splitCommand[0] != "exit" and splitCommand[0] != "search" 
            and splitCommand[0] != "update" and splitCommand[0] != "delete" and splitCommand[0] != "print" 
            and splitCommand[0] != "addgroup" and splitCommand[0] != "showgroup"):
            return False
        return True
# move to userinterface
    def exit(self):
        self.write_json(self.fileName)
        quit()

    def add_group(self, paramsDict):
        id = self.generate_id()
        group = Group(paramsDict["group_name"], paramsDict["group_id"])
        group.add_contact_group(paramsDict["contact_ids_list"], self.contactDic)
        if(len(paramsDict["contact_ids_list"]) != 0):
            self.groups.append(paramsDict)
            return True
        return False
   
    def show_group(self, id):
        for paramsDict in self.groups:
            if(paramsDict.get("group_id") == id):
                print("group name:" + paramsDict.get("group_name"))
                self.print_group_contact(paramsDict.get("contact_ids_list"))

    def print_group_contact(self, contactids):
        for id in contactids:
            print(self.contactDic[id])
# query
    def search_group(self, word):
        for paramsDict in self.groups:
                if(paramsDict.get("group_name").startswith(word) or paramsDict.get("group_name").endswith(word)):
                    member = self.count_group_members(paramsDict.get("group_id"))
                    print(paramsDict.get("group_id") + " " +  paramsDict.get("group_name") + " " + str(member) + "members")
    
    def count_group_members(self, id):
        for paramsdict in self.groups:
            if(paramsdict.get("group_id") == id):
                number = len(paramsdict.get("contact_ids_list"))
                return number

    def write_json(self, fileName):
        listContactDict = []
        for contact in self.contactDic.values():
            listContactDict.append(contact.__dict__)

        with open(fileName,'w') as fp:
            json.dump(listContactDict, fp)    


        with open("groupsList.json",'w') as g:
            json.dump(self.groups, g)
        
    def read_json(self, fileName):
        with open(fileName) as fp:
            listdict = json.load(fp)
            
        for i in range(len(listdict)):
            self.add_contact(listdict[i].get("_fName"), listdict[i].get("_lName"), listdict[i].get("_emailAddress"), listdict[i].get("_phoneNumber"), listdict[i].get("_ID"))

        with open("groupsList.json") as g:
            self.groups = json.load(g)


        

