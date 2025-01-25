from pprint import pprint

class InsufficientFundsException(Exception):
    pass


class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        self._transaction_history = []
        
    def get_balance(self):
        return self.__balance
    
    def deposite(self, amount):
        self.__balance += amount
        transaction = {
            'name': self.account_holder,
            'type' : 'deposite',
            'amount': amount,
            'current_balance': self.__balance
            
        }
        self._transaction_history.append(transaction)
        
        return self.__balance
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            transaction = {
            'name': self.account_holder,
            'type' : 'withdraw',
            'amount': amount,
            'current_balance': self.__balance
            
        }
            self._transaction_history.append(transaction)
            return self.__balance
        else:
            raise InsufficientFundsException("Insufficient funds")
        
    def get_transactions(self):
        return self._transaction_history
    

        
        
if __name__ == "__main__":
    try:
        akash = Account(1,"Akash Pawar", 10000)
        # akash_balance = akash.get_balance()
        # withdraw = akash.withdraw(100000)
        akash.deposite(10)
        akash.withdraw(1)
        akash.deposite(1000)
        akash.withdraw(12)
        
        akash_transactions = akash.get_transactions()
        pprint(akash_transactions)
        
        
    
    except InsufficientFundsException as e:
        print("Error : Insufficient Funds !")
        pass
    
    
    