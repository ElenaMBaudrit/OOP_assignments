#Todd's March 21st 2018

#example of a class.
class Person(object):
    #Always put "object" inside the parentheses of the class
    def __init__(self, name, age, location):
    #double underscores in Python: something that is written somewhere else. "Dunder"= double underscores.
    #constructor: name of the function/method. There will be the attributes for the specific class.
    #the "name, age, location" are the parameters that "person" instance will have. "Self" help us create the linkage between the class and the instances. It is similar to "this", from JQuery.
        self.name = name
        self.age = age
        self.location = location
    def say_hello(self):
        print "Hello, my name is {}".format(self.name)


#Instance: think of it as a variable, defining the class it belongs to.
p1 = Person("Javier", 23, "San Jose")
print p1.name
print p1.age
print p1.location

#If there are more individuals, it goes like this:
p2 = Person ("Rodolfo", 23, "San Jose")
p3 = Person("Elena", 21, "San Jose")
p4 = Person ("Manzura", 21, "Tempe")
p3.say_hello()


    