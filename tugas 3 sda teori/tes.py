class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):  # R-2.7
        self.customer = customer
        self.bank = bank
        self.account = acnt
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
        return self.balance

    def charge(self, price):
        try:  # R-2.5
            if price + self.balance > self.limit:
                return False
            else:
                self.balance += price
                return True
        except TypeError:
            raise TypeError("Harga harus berupa angka")

    def make_payment(self, amount):
        try:  # R-2.6
            if amount < 0:
                raise ValueError("Jumlah transaksi tidak boleh negatif")
            else:
                self.balance -= amount
        except TypeError:
            raise TypeError("Jumlah transaksi harus berupa angka")

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 1000, 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1, 17): #R-2.8
        if wallet[0].charge(val) is False:  # Check if charging is successful
            print(f"Kartu kredit '{wallet[0].get_account()}' telah melebihi kredit limit.")
            break
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()

