# __bool__ - Truthiness (True or False)
# __bool__ determines what happens when you use your object in an if statement or with bool().

# Default Behavior:
# Without __bool__, objects are always True (except None).



class ShoppingCart:
    def __init__(self):
        self.items = []
    items = []
    def add_items(self,item):
        self.items.append(item)

    def __bool__(self):
        # Cart is True if it has items, False if empty
        return len(self.items) > 0

cart = ShoppingCart()

if cart:
    print("cart has items")
else:
    print("cart is emppty")
# output cart is empty

cart.add_items("bag")
cart.add_items('pen')


if cart:
    print("cart has items")
else:
    print("cart is emppty")



# Important Note: If __bool__ is not defined but __len__ is, Python uses __len__:

# len(obj) == 0 → False
# len(obj) > 0 → True