from UserInterface import UserInterface
from Contactdon import Contactdon
class main:
    # from UserInterface import UserInterface
    # from Contactdon import Contactdon
    contactdon = Contactdon()
    # contactdon.input_command()

    userInterface = UserInterface(contactdon)
    userInterface.get_input()
    # if __name__ == "__main__":
    #     main()

    
    