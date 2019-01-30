class Transactions:
    countID = 0
    def __init__(self, loanAmt, today, sender, receiver):
        Transactions.countID +=1
        self.__countID = Transactions.countID
        self.__loanAmt = loanAmt
        self.__date = today
        self.__sender = sender
        self.__receiver = receiver

    def set_loanAmt(self,loanAmt):
        self.__loanAmt = loanAmt
    def set_date(self,date):
        self.__date = date
    def set_sender(self,sender):
        self.__sender = sender
    def set_receiver(self,receiver):
        self.__receiver = receiver

    def get_loanAmt(self):
        return self.__loanAmt
    def get_date(self):
        return self.__date
    def get_sender(self):
        return self.__sender
    def get_receiver(self):
        return self.__receiver


