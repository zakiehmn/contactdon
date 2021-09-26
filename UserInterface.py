class UserInterface:
    def __init__(self):
        pass

    def input(self):
        splitCommand = []
        inputCommand = input()
        splitCommand = inputCommand.split(" ")
        n = splitCommand.count("")
        for i in range(n):
            splitCommand.remove("")

        return splitCommand
    
    def output(self, status):
        if(status):
            print("command ok")
        else:
            print("command failed")