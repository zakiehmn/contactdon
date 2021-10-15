import string
import random
class Utils:

    def generate_id(self):
        letters = string.digits
        id=''.join(random.choice(letters) for i in range(5))
        return id
 
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
