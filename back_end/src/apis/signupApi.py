from back_end.src.mogodb import db
import back_end.src.objects.User as User

class SignUp(Object):
    #数据库user集合
    userCollection =  db.User.__collection__

    def __init__(self, user):
        super().__init__()
        self.__user = user

    #如果该用户邮箱已经被注册返回false，没有被注册返回true
    def checkBeforeSignUp(self):

       isRegitered =  SignUp.userCollection.find_one({"user_email": self.__user.get_email});

       if(isRegitered == None):
           return True

       return False

    def signup(self):
        user = {
            "user_email": self.__user.get_email(),
            "pwd": self.__user.get_pwd(),
            "register_date": self.__user.get_registerDate()
        }
        if(self.checkBeforeSignUp()):
            return SignUp.userCollection.insert_one(user).inserted_id
        return None

        