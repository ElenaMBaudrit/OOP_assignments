'''
Assignment: Car
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 
Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.
'''
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def display_all(self):
        if self.price>=10000:
            print "Tax: 0.12"
        else:
            print "Tax:0.15"
        print "Price: ",self.price, "\nSpeed: ",self.speed, "\nFuel: ",self.fuel, "\nMileage: ",self.mileage
        return self
honda = Car(5000, '90mph', 'Not full', '50mpg')
honda.display_all()

toyota = Car(7000, '80mph','Full', '55mpg')
toyota. display_all()

porsche = Car(200000, '120mph','Full', '75mpg')
porsche. display_all()

nissan = Car(50000, '80mph', 'Not full', '65mpg')
nissan.display_all()

range_rover = Car(27000, '80mph','Almost full', '45mpg')
range_rover. display_all()

bmw = Car(200000, '120mph','Not full', '65mpg')
bmw. display_all()