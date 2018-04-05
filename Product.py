'''
Assignment: Product
The owner of a store wants a program to track products. Create a product class to fill the following requirements.
Product Class:
Attributes:
    Price
    Item Name
    Weight
    Brand
    Status: default "for sale"
Methods:
    Sell: changes status to "sold"
    Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
    Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.
'''
class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def tax(self):
        total_tax=0.15
        for self.price in Product:
            total_price=self.price*total_tax
        return self

    def returned_product(self, return_reason):
        if (return_reason == "defective"):
            self.status = "Returned: Defective"
            self.price = 0
        elif (return_reason == "returned in box"):
            self.status = "Returned: In the box, like new"
            self.status= "For sale"
        elif (return_reason == "returned in box, opened"):
            self.status = "Returned: In the box, opened"
            discount=0.2
            self.status= "Used"
            discount_amount=self.price*0.20
        return self

    def display_info(self):
        print "Price: {}".format(self.price)
        print "Name: {}".format(self.item_name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        print "**********"
        return self
        
p1 = Product(24.99, "French press", "12 oz", "Bodum")
p2 = Product(174.99, "Giant bean bag", "15 lbs", "Big Squishy")
p3 = Product(8.99, "Heisenberg Mr Potato Head", "6 oz", "PopTaters")
p1.returned_product("defective").display_info()
p2.returned_product("returned in box").display_info()
p3.returned_product("opened").display_info()






'''
Todd's

class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price 
        self.name = name 
        self.weight = weight 
        self.brand = brand 
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self 

    def add_tax(self, tax):
        return self.price + (self.price * tax)

    def return_product(self, reason):
        if (reason == "defective"):
            self.status = "Defective"
            self.price = 0
        elif (reason == "returned in box"):
            self.status = "For Sale"
        elif (reason == "opened"):
            self.status = "Used"
            self.price = self.price - (self.price * .2)
        return self

    def display_info(self):
        print "Price: {}".format(self.price)
        print "Name: {}".format(self.name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        print "==========="
        return self

p1 = Product(99.99, "Cell phone", "6 oz", "Samsung")
p2 = Product(299.99, "PS4", "5 lbs", "Sony")
p3 = Product(399.99, "XBox One", "6 lbs", "Microsoft")
p1.return_product("defective").display_info()
p2.return_product("returned in box").display_info()
p3.return_product("opened").display_info()
'''

            
            

    



