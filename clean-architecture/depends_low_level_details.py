
# Clean Architecture is about organizing your code so that:
# Business logic doesn't depend on frameworks, databases, or UI
# You can swap out technologies without rewriting everything
# Testing is straightforward
# Changes in one area don't break others
# ❌ Bad: High-level code depends on low-level details

class OrderService:
    def __init__(self):
        self.db = MySQLDatabase()
    def create_order(self, order_data):
        self.db.insert("orders", order_data)

# If you want to switch from MySQL to PostgreSQL, you have to change OrderService. That's fragile