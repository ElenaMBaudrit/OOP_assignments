'''
Assignment: Bike
Create a new class called Bike with the following properties/attributes:
    price
    max_speed
    miles
Create 3 instances of the Bike class.
Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
Add the following functions to this class:
    displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
    ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
    reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
What would you do to prevent the instance from having negative miles?
Which methods can return self in order to allow chaining methods?
'''

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles =  0
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        self.miles+=10
        print "Riding "
        return self
    def reverse(self):
        self.miles-=5
        print "Reversing"
        return self
cannondale =  Bike(700, 25)
cannondale.ride().ride().ride().reverse().displayInfo()

trek =  Bike(800, 30)
trek.ride().ride().reverse().reverse().displayInfo()

patito = Bike(50, 10)
patito.reverse().reverse().reverse().displayInfo()











'''
class Bike{
	var $price = 10;
	var $max_speed = 80;
	var $miles = 11;
	
	function __construct($x, $y)
	{
		$this->price = $x;
		$this->max_speed = $y;
		echo "creating bike <br>";
		$this->miles = 0;
	}
	function displayInfo(){
		echo "Price of this bike is $".$this->price.'dollars<br>';
		echo 'the maximum speed is: '.$this->max_speed."<br>";
		echo "number of miles driven is: ".$this->miles."<br>";
	}
	function driving(){
		echo 'bike is rolling...';
		echo "<img style='height:30px' src='http://upload.wikimedia.org/wikipedia/commons/7/79/2009-03-11_Beat_up_car_driving_in_Durham.jpg'/>";
		$this->miles = $this->miles+10;
	}
	function reverse(){
		echo "bike is reversing";
		echo "<img style='height:30px' src='http://www.designboom.com/snapshots/tokyobike/bike_images/others/01.jpg'>";
		$this->miles=$this->miles-5;
		if ($this->miles < 0) {
			$this->miles = 0;
		}
	}
}
//outside of the class now, generating specific instatiations or instances
$huffy = new Bike(50, 5);
$schwin = new Bike(100, 10);
$trek = new bike(200, 15);
$huffy->driving();$huffy->driving();$huffy->driving();
$huffy->reverse();
$huffy->displayInfo();
$schwin->driving();$schwin->driving();$schwin->reverse();$schwin->reverse();
$schwin->displayInfo();
$trek->reverse();$trek->reverse();$trek->reverse();
$trek->displayInfo();
'''