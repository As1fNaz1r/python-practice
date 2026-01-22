Real-World Use Cases
1. Lazy Loading (Don't load until needed):

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        # Don't load profile yet!
    
    def __getattr__(self, name):
        if name == "profile":
            print("Loading profile from database...")
            self._profile = {"name": "John", "email": "john@example.com"}
            return self._profile
        raise AttributeError(f"No attribute {name}")

u = User(123)
# Profile not loaded yet
print(u.profile)  # NOW it loads
print(u.profile)  # Already loaded, uses _profile directly
2. Dynamic Attributes (API wrapper):

class APIClient:
    def __getattr__(self, endpoint):
        return f"Calling API endpoint: /{endpoint}"

api = APIClient()
print(api.users)     # "Calling API endpoint: /users"
print(api.products)  # "Calling API endpoint: /products"
3. Validation:

class StrictPerson:
    def __setattr__(self, name, value):
        if name == "age" and not isinstance(value, int):
            raise TypeError("Age must be an integer")
        super().__setattr__(name, value)

p = StrictPerson()
p.age = 25      # OK
p.age = "25"    # TypeError!
Common Mistakes
Mistake 1: Forgetting super() in __getattribute__

class Bad:
    def __getattribute__(self, name):
        return self.__dict__[name]  # 💥 Calls __getattribute__ again!
Mistake 2: Thinking __getattr__ is always called

class Test:
    def __init__(self):
        self.x = None  # x EXISTS (even though it's None)
    
    def __getattr__(self, name):
        return "default"

t = Test()
print(t.x)  # Prints None, NOT "default" (because x exists!)
print(t.y)  # Prints "default" (y doesn't exist)
Mistake 3: Using self.x = value in __setattr__

class Bad:
    def __setattr__(self, name, value):
        self.name = value  # 💥 Infinite recursion!
When to Use What?
__getattr__: Default values, dynamic attributes, API wrappers (SAFE, use this most of the time)
__getattribute__: Proxies, logging every access, security (POWERFUL but dangerous)
__setattr__: Validation, read-only attributes, logging changes
__delattr__: Prevent deletion, cleanup resources