# Why NotImplemented not False?

class A:
    def __eq__(self,other):
        if not isinstance(other,A):
            return NotImplemented
        return True

class B:
    def __eq__(self,other):
        # if not isinstance(other, B):
        #     return NotImplemented
        return True

a = A()
b = B()

print(a == b)

# # Python tries: a.__eq__(b) → NotImplemented
# # Then tries: b.__eq__(a) → True
# a == b  # True - B got a chance!