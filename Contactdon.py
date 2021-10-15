from Contact import Contact
from Group import Group 
from Utils import Utils
import string
import random
import json
class Contactdon:
    
    def __init__(self, contactDic = {}, contactFile = 'contactdict.json',
                 groupFile = 'groupsList.json', groups = [], utils = Utils()):
        self.contactDic = contactDic
        self.contactFile = contactFile
        self.groupFile = groupFile
        self.groups = groups
        self.read_json(contactFile, groupFile)
        self.utils = utils

    def add_contact(self, fName, lName, emailAddress, phoneNumber, id):
        newContact = Contact(fName, lName, emailAddress, phoneNumber, id)
        self.contactDic[id] = newContact
        return True
        
    def check_uniqueID(self, id):
        if id in self.contactDic.keys():
            self.utils.generate_id()
        return id
              
    def add(self, paramsDict):
        id = self.utils.generate_id()
        id = self.check_uniqueID(id)
        if(len(paramsDict.keys()) == 4):
            if(self.check_unique_fnamelname(paramsDict["first_name"], paramsDict["last_name"]) and 
               self.utils.check_correctPhoneNum(paramsDict["phone_number"]) and 
               self.utils.check_correctEmail(paramsDict["email_address"]) ):
                self.add_contact(paramsDict["first_name"], paramsDict["last_name"],
                paramsDict["email_address"], paramsDict["phone_number"], id)
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

    def search_contact(self, query):
        contactResult = []
        for contact in self.contactDic.values():
            if(contact._fName.startswith(query) 
               or contact._lName.startswith(query)
               or contact._emailAddress.startswith(query) 
               or contact._phoneNumber.startswith(query)
               or contact._fName.endswith(query) 
               or contact._lName.endswith(query) 
               or contact._emailAddress.endswith(query) 
               or contact._phoneNumber.endswith(query)):
                contactResult.append(contact)
        return contactResult

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
                if(self.check_unique_emailaddress(paramsDict["email_address"]) == False or
                   self.utils.check_correctEmail(paramsDict["email_address"]) == False):
                    check = False
            if(key == "phone_number"):
                if(self.check_unique_phonenum(paramsDict["phone_number"]) == False or
                   self.utils.check_correctPhoneNum(paramsDict["phone_number"]) == False):
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
            if(fname == self.contactDic[contact]._fName and 
               self.contactDic[id]._lName == self.contactDic[contact]._lName):
                return False
        return True
        
    def check_unique_lname(self, id, lname):
        for contact in self.contactDic:
            if(lname == self.contactDic[contact]._lName and 
               self.contactDic[id]._fName == self.contactDic[contact]._fName ):
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
      
    # def other_command(self,splitCommand):
    #     if(splitCommand[0] != "add" and splitCommand[0] != "exit" and splitCommand[0] != "search" 
    #         and splitCommand[0] != "update" and splitCommand[0] != "delete" and splitCommand[0] != "print" 
    #         and splitCommand[0] != "addgroup" and splitCommand[0] != "showgroup"):
    #         return False
    #     return True

    def exit(self):
        self.write_json(self.contactFile,self.groupFile)
        

    def add_group(self, paramsDict):
        print(paramsDict)
        group = Group(paramsDict["group_name"], int(paramsDict["group_id"]))
        print(group)
        print(paramsDict["contact_ids_list"])
        group.add_contact_group(paramsDict["contact_ids_list"], self.contactDic)
        if(len(paramsDict["contact_ids_list"]) != 0):
            self.groups.append(group)
            print(self.groups)
            return True
        return False
   
    def group_to_dict(self,group):
        groupDict = {}
        idsList = []
        idsList = self.contact_to_id_list(group._membersList)
        groupDict = {
            "group_name" : group._name,
            "contact_ids_list" : idsList,
            "group_id" : group._id
        }
        return groupDict

    def contact_to_id_list(self, members):
        idsList = []
        for contact in members:
            idsList.append(contact._ID)
        return idsList


    def return_group(self, id):
        for group in self.groups:
            if(group._id == int(id)):
                return group
 
# query
    def search_group(self, query):
        resultGroup = []
        for group in self.groups:
                if(group._name.startswith(query) or
                   group._name.endswith(query)):
                    resultGroup.append(group)
        return resultGroup
         
    def write_json(self, contactFile, groupFile):
        listContactDict = []
        for contact in self.contactDic.values():
            listContactDict.append(contact.__dict__)

        with open(contactFile,'w') as fp:
            json.dump(listContactDict, fp) 

        groupDictList = []
        for group in self.groups:
            groupDictList.append(self.group_to_dict(group))
        with open(groupFile,'w') as g:
            json.dump(groupDictList, g)
        
    def read_json(self, contactFile, groupFile):
        with open(contactFile) as fp:
            listdict = json.load(fp)
            
        for i in range(len(listdict)):
            self.add_contact(listdict[i].get("_fName"), listdict[i].get("_lName"),
                             listdict[i].get("_emailAddress"), listdict[i].get("_phoneNumber"),
                             listdict[i].get("_ID"))

        
        with open(groupFile) as g:
            groupDictList = json.load(g)
            for Dict in groupDictList:
                self.add_group(Dict)


        

