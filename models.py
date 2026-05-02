import abc 





class DatabaseManager :
    _instance =None 

    def __new__ (cls ):
        if cls ._instance is None :
            cls ._instance =super (DatabaseManager ,cls ).__new__ (cls )
            cls ._instance .products =[]
            print ("[System] Database initialized successfully (Singleton).")
        return cls ._instance 

    def add_product (self ,product ):
        self .products .append (product )

    def get_all_products (self ):
        return self .products 






class Product (metaclass =abc .ABCMeta ):
    def __init__ (self ,name ,price ):
        self .name =name 
        self .price =price 

    @abc .abstractmethod 
    def get_info (self ):
        pass 

class Pet (Product ):
    def get_info (self ):
        return f"Pet: {self.name} | Price: ${self.price}"

class Food (Product ):
    def get_info (self ):
        return f"Food: {self.name} | Price: ${self.price}"

class Accessory (Product ):
    def get_info (self ):
        return f"Accessory: {self.name} | Price: ${self.price}"

class ProductFactory :
    """المصنع لإنشاء المنتجات بناءً على النوع."""
    @staticmethod 
    def create_product (product_type ,name ,price ):
        if product_type =="pet":
            return Pet (name ,price )
        elif product_type =="food":
            return Food (name ,price )
        elif product_type =="accessory":
            return Accessory (name ,price )
        else :
            raise ValueError ("نوع المنتج غير معروف!")






class Observer (metaclass =abc .ABCMeta ):
    @abc .abstractmethod 
    def update (self ,status ):
        pass 

class Customer (Observer ):
    def __init__ (self ,name ):
        self .name =name 

    def update (self ,status ):
        print (f"[Notification] Dear {self.name}, your order status is now: {status}")

class Order :
    """الكائن الذي يتم مراقبته (Subject)."""
    def __init__ (self ,order_id ):
        self .order_id =order_id 
        self ._observers =[]
        self ._status ="Pending (قيد الانتظار)"

    def attach (self ,observer ):
        self ._observers .append (observer )

    def set_status (self ,status ):
        self ._status =status 
        self ._notify_all ()

    def _notify_all (self ):
        for observer in self ._observers :
            observer .update (self ._status )
