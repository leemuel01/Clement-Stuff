class User:
    countID = 100

    #i took out balance from the parameter and set it to 0 first, later the balance will increase when we top up
    def __init__(self, firstname, lastname, email, phonenumber, password,accountnumber):
        User.countID +=1
        self.__userID = User.countID
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__phonenumber = phonenumber
        self.__password = password
        self.__balance = 0
        self.__accountnumber=accountnumber


    def get_userID(self):
        return self.__userID
    def get_firstname(self):
        return self.__firstname
    def get_lastname(self):
        return self.__lastname
    def get_email(self):
        return self.__email
    def get_phonenumber(self):
        return self.__phonenumber
    def get_password(self):
        return self.__password
    def get_balance(self):
        return self.__balance
    def get_accountnumber(self):
        return self.__accountnumber

    def set_userID(self, userID):
        self.__userID = userID
    def set_firstname(self, firstname):
        self.__firstname = firstname
    def set_lastname(self, lastname):
        self.__lastname = lastname
    def set_email(self, email):
        self.__email = email
    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber
    def set_password(self, password):
        self.__password = password
    def set_balance(self,balance):
        self.__balance=balance
    def set_accountnumber(self,accountnumber):
        self.__accountnumber= accountnumber