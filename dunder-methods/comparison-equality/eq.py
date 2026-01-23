class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id


u1 = User(1, "asif")
u2 = User(1, "bhat")

print(u1 == u2)