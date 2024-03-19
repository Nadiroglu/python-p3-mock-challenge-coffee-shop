class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name


    def orders(self):
        coffee_orders = []
        for order in Order.all:
            if order.coffee is self:
                coffee_orders.append(order)
        return coffee_orders
        # return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        customer_list = []
        for order in self.orders():
            if isinstance(order.customer, Customer):
                customer_list.append(order.customer)
        return customer_list

    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if not self.orders():
            return 0
        total = [order.price for order in self.orders() if order.coffee is self]
        return sum(total) / len(total)

        

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    
    def orders(self):
        order_of_customer = []
        for order in Order.all:
            if order.customer is self:
                order_of_customer.append(order)
        return order_of_customer
    
    def coffees(self):
        coffee_of_customer = []
        for order in self.orders():
            if isinstance(order.coffee, Coffee):
                coffee_of_customer.append(order.coffee)
        return coffee_of_customer

    
    def create_order(self, coffee, price):
        pass
    
class Order:

    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)


    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
