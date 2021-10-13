from Contactdon import Contactdon

class UserInterface:

    def __init__(self, contactdon):
        self.contactdon = contactdon

    def run (self):
        inputCommand = input()
        self.run_command(inputCommand)
        self.run()

    def split_input_str(self, inputCommand):
        splitCommand = []
        splitCommand = inputCommand.split(" ")
        n = splitCommand.count("")
        for i in range(n):
            splitCommand.remove("")
        return splitCommand

    def run_command (self, inputCommand):
        splitCommand = self.split_input_str(inputCommand)
        if(splitCommand[0] == "add"):
            paramsAdd = self.params_contact_dict(splitCommand)
            statusAdd = self.contactdon.add(paramsAdd)
            self.output(statusAdd)

        if(splitCommand[0] == "search"):
            self.contactdon.search(splitCommand[1])

        if(splitCommand[0] == "delete"):
            statusDel = self.contactdon.delete(splitCommand[1])
            self.output(statusDel)

        if(splitCommand[0] == "update"):
            paramsUpdate = self.add_id_params(splitCommand)
            print(paramsUpdate)
            statusUpd = self.contactdon.update(paramsUpdate)
            self.output(statusUpd)

        if(splitCommand[0] == "addgroup"):
            paramsGroup = self.params_group_dict(splitCommand)
            statusGroup = self.contactdon.add_group(paramsGroup)
            self.output(statusGroup)

        if(splitCommand[0] == "showgroup"):
            self.contactdon.show_group(splitCommand[1])

        if(splitCommand[0] == "exit"):
            self.contactdon.exit()

        self.other_command(splitCommand)
        

    def params_contact_dict(self, splitCommand):
        paramsDict = {}
        fName, lName, emailAddress, phoneNumber = "", "", "", ""
        for index in range(len(splitCommand)):
            if(splitCommand[index] == "-f"):
                fName = splitCommand[index+1]
            if(splitCommand[index] == "-l"):
                lName = splitCommand[index+1]
            if(splitCommand[index] == "-e"):
                emailAddress = splitCommand[index+1]
            if(splitCommand[index] == "-p"):
                phoneNumber = splitCommand[index+1]
        if(fName != ""):
            paramsDict["first_name"] = fName
        if(lName != ""):
            paramsDict.update({"last_name" : lName})
        if(emailAddress != ""):
            paramsDict.update({"email_address" : emailAddress})
        if(phoneNumber != ""):
            paramsDict.update({"phone_number" : phoneNumber})  
        return paramsDict

    def add_id_params(self, splitCommand):
        paramsDict = self.params_contact_dict(splitCommand)
        paramsDict.update({"id" : splitCommand[1]})
        return paramsDict

    def params_group_dict(self, splitCommand):
        paramsDict = {}
        for index in range(len(splitCommand)):
            if(splitCommand[index] == "-n"):
                groupName = splitCommand[index+1]
            if(splitCommand[index] == "-c"):
                idsStr = splitCommand[index+1]
                splitIds = self.separate_ids(idsStr)
        id = self.contactdon.generate_id()

        paramsDict = {
            "group_name" : groupName ,
            "contact_ids_list" : splitIds ,
            "group_id" : id
        }
        return paramsDict
                
    def separate_ids(self, idsStr):
        splitIds = idsStr.split(",")
        return splitIds

    def output(self, status):
        if(status):
            print("command ok")
        else:
            print("command failed")