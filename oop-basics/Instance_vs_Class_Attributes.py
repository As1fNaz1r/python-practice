# Instance attributes - Each object has its own copy 
# Class attributes - Shared by all objects

class BankAccount:
    bank_name = "MyBank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Alice",1000)
acc2 = BankAccount("Bob",500)

print(acc1.bank_name)
print(acc2.bank_name)

print(acc1.owner)
print(acc2.owner)


BankAccount.bank_name = "NewBank"

print(acc1.bank_name)
print(acc2.bank_name)


# output
# MyBank
# MyBank
# Alice
# Bob
# NewBank
# NewBank



# When to use which:

# Instance attributes: Data unique to each object (name, balance, age)
# Class attributes: Data shared by all objects (constants, defaults, counters)