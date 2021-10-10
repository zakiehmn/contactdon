from UserInterface import UserInterface
from Contactdon import Contactdon
class main:
    contactdon = Contactdon()
    userInterface = UserInterface(contactdon)
    userInterface.run()
    
    if __name__ == "__main__":
        main()

    
    