class CreditCard :
    def __init__(self, customer, bank, account, limit, balance=0):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = balance
    
    def get_customer(self):
        return self.customer
    
    def get_bank(self):
        return self.bank
    
    def get_account(self):
        return self.account
    
    def get_limit(self):
        return self.limit
    
    def get_balance(self):
        return self.get_balance
    
    def charge(self, price):
        try:
            if price + self.balance > self.limit:
                return False
            else:
                return True
        except TypeError:
            raise TypeError("Tagihan harus berupa angka")
    
    def make_payment(self, amount):
        try:
            if amount < 0:
                raise ValueError("Jumlah transaksi tidak boleh negatif")
            else:
                self.balance -= amount
        except TypeError:
            raise TypeError("Jumlah transaksi harus berupa angka")

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '1234 5678 9012 3456', 1000))
    wallet.append(CreditCard('John Bowman', 'California Federal', '1234 3628 8312 1234', 2500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '6789 1234 9345 3236', 3000))

    for val in range(1,17):
        wallet[0].charge(val) is False
        print(f"Credit Card '{wallet[0].get_account()}' telah mencapai limit")
        break
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance = ', wallet[c].get_balance())
        print()