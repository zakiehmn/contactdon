from Contactdon import Contactdon

class UserInterface:

    def __init__(self, contactdon):
        self.contactdon = contactdon

    
    def get_input(self):
        inputCommand = input()
        self.check_input_command(inputCommand)

    def split_input_str(self, inputCommand):
        splitCommand = []
        splitCommand = inputCommand.split(" ")
        n = splitCommand.count("")
        for i in range(n):
            splitCommand.remove("")
        return splitCommand

    def check_input_command (self, inputCommand):
        splitCommand = self.split_input_str(inputCommand)
        if(splitCommand[0] == "add"):
            paramsDict = self.params_contact_dict(splitCommand)
            statusAdd = self.contactdon.add(paramsDict)
            self.output(statusAdd)

        if(splitCommand[0] == "search"):
            self.contactdon.search(splitCommand[1])

        if(splitCommand[0] == "delete"):
            statusDel = self.contactdon.delete(splitCommand[1])
            self.output(statusDel)

        if(splitCommand[0] == "update"):
            statusUpd = self.contactdon.update(splitCommand)
            self.output(statusUpd)

        if(splitCommand[0] == "addgroup"):
            statusGroup = self.contactdon.add_group(splitCommand)
            self.output(statusGroup)

        if(splitCommand[0] == "showgroup"):
            self.contactdon.show_group(splitCommand[1])

        if(splitCommand[0] == "exit"):
            self.contactdon.exit()

        # self.other_command(splitCommand)
        
        self.get_input()

    def params_contact_dict(self, splitCommand):
        paramsDict = {}
        for index in range(len(splitCommand)):
            if(splitCommand[index] == "-f"):
                fName = splitCommand[index + 1]
            if(splitCommand[index] == "-l"):
                lName = splitCommand[index + 1]
            if(splitCommand[index] == "-e"):
                emailAddress = splitCommand[index + 1]
            if(splitCommand[index] == "-p"):
                phoneNumber = splitCommand[index + 1] 
        paramsDict = {
            "first name" : fName ,
            "last name" : lName ,
            "email address" : emailAddress ,
            "phone number" : phoneNumber
        }
        return paramsDict

    def output(self, status):
        if(status):
            print("command ok")
        else:
            print("command failed")