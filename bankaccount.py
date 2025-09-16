from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def get_blanace(self):
        pass