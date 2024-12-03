from menu import MenuItem, Menu

class OrderItem:
    def __init__(self, menuitem: MenuItem, quantity: int = 1):
        self.menuitem = menuitem
        self.quantity = quantity

class Order:
    def __init__(self):
        self.orders = [] # accepts a OrderItem(menuitem, quantity)
    
    def add(self, menuitem: MenuItem, quantity: int = 1): 
        for order in self.orders:
            if order.menuitem == menuitem:
                order.quantity += quantity #should it increment?
                break
        else:
            self.orders.append(OrderItem(menuitem, quantity))  
# we want to link the menuitem price to the  multiply the quantity 
    def total_price(self):
        order_sum = []
        for order in self.orders:
            #order is a OrderItem class (menuitem, quantity)
            total = order.menuitem.price*order.quantity # menuitem is a MenuItem (name, price)
            order_sum.append(total)
        return sum(order_sum)
    
    def total_quantity(self):
        quantity_sum = []
        for order in self.orders:
            quantity_sum.append(order.quantity)
        return sum(quantity_sum)
    
    def print(self):
        print('YOUR ORDER:                 Qty     Price     Total', end='\n')
        for order in self.orders:
            print(f"  {order.menuitem.name:<24}  {order.quantity:>3}  {f'${order.menuitem.price:.2f}':>8}  {f'${order.menuitem.price*order.quantity:.2f}':>8}", end='\n')
        print(f'{"TOTAL":<24}        {f"${self.total_price():.2f}":>19}', end='\n')

