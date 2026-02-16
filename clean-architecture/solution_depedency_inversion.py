# If you want to switch from MySQL to PostgreSQL, you have to change OrderService. That's fragile


from abc import ABC, abstractmethod

#Define what we need (interface/contract)

class Database(ABC):
    @abstractmethod
    def save(self, tables, data):
        pass
    

#High level business logic
class OrderService:
    def __init__(self, databse:Database):
        self.db = Database

    def create_order(self, order_data):
        self.db.save("orders", order_data)

#low-level implementation
class MySQLDatabase(Database):
    def save(self, table,data):
        print((f"saving to MYSQL: {table}"))

class PostgreSQLDatabase(Database):
    def save(self, table, data):
        print("Saving to Postgresql:{table}")
    

#usage you control what gets injected
service  = OrderService(MySQLDatabase)
#or
service = OrderService(PostgreSQLDatabase)


# Key Insight: Your business logic says "I need something that can save data" without caring how it saves. The implementation details are injected from outside.

