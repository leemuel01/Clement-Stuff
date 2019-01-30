class Account:
    countID = 0

    def __init__(self, Sender,Receiver, AccountNo,Bank, Type, Amount):
        Account.countID +=1
        self.__userID = Account.countID
        self.__Sender=Sender
        self.__Receiver=Receiver
        self.__AccountNo = AccountNo
        self.__Bank=Bank
        self.__Type = Type



    def get_AccountNo(self):
        return self.__AccountNo

    def get_Type(self):
        return self.__Type

    def get_userID(self):
        return self.__userID

    def set_userID(self, userID):
        self.__userID = userID

    def set_Type(self,Type):
        self.__Type=Type

    def set_AccountNo(self,AccountNo):
        self.__AccountNo=AccountNo
