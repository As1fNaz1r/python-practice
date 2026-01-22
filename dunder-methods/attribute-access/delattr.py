class ProtectedData:
    def __init__(self):
        self.data = "important"
    
    def __delattr__(self, name):
        if name == "data":
            print("you cant delete it")
        else:
            super().__delattr__(name)


p = ProtectedData()
del p.data