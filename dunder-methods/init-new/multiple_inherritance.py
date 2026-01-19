class A:
    def __new__(cls):
        print("A.__new__")
        return super().__new__(cls)

class B:
    def __new__(cls):
        print("B.__new__")
        return super().__new__(cls)

class C(A, B):
    def __new__(cls):
        print("C.__new__")
        return super().__new__(cls)

c = C()
# C.__new__
# A.__new__
# B.__new__
