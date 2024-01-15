class Account:
    def __init__(self, owner: str, starting_amount=0):
        self.starting_amount = starting_amount
        self.owner = owner
        self.amount = starting_amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount >= 0:
            self.amount += transaction_amount
            self._transactions.append(transaction_amount)
            return f"New balance: {self.amount}"
        else:
            raise ValueError("sorry cannot go in debt!")

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            if self.amount + amount >= 0:
                self.amount += amount
                self._transactions.append(amount)
                return f"New balance: {self.amount}"
            else:
                raise ValueError("sorry cannot go in debt!")

    @property
    def balance(self):
        return sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.starting_amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.starting_amount + other.starting_amount)
        new_account._transactions = self._transactions + other._transactions

        return new_account


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.amount)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
