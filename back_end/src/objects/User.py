import datetime
import time
from ..units import verifyEmail

class User(object):
    __collection__ =  'user'

    def __init__(self, email, pwdHash, registerDate):
        super().__init__()
        self.__email = email
        self.__pwd = pwdHash
        self.__registerDate = registerDate


    def toString(self):
        return self.__email + self.__pwd + self.__registerDate
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        if(verifyEmail.is_valid_email(email)):
            self.__email = email
        else:
            raise ValueError('invaild email format: %s' %email)

    def get_dateInformat(self):
       return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(self.__registerDate))

    def get_pwd(self):
        return self.__pwd

    def get_registerDate(self):
        return self.__registerDate

    
        

    
