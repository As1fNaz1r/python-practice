# The service layer contains your business logic - the rules that make your application unique.

class Order:
    def __init__(self, customer_id, items, total):
        self.customer_id = customer_id
        self.items = items
        self.total = total
        self.status = "pending"
    
    def calculate_total(self):
        return sum(item['item'] * item['quantity'] for item in self.items)



class OrderService:
    def __init__(self, order_repo, email_service):
        self.order_repo = order_repo
        self.email_service = email_service

    def place_order(self, customer_id, items):
        

        


    
