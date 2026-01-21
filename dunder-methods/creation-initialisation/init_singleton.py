# Preventing __init__ from Running Multiple Times in Singleton


class Singleton:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        if not Singleton._initialized:
            print("initialized once")
            self.data = []
            Singleton._initialized = True


s1 = Singleton()
s2 = Singleton()

