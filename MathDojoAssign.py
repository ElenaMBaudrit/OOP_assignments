'''
Assignment: MathDojo
    HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.
PART I
    Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
    Then create a new instance called md. It should be able to do the following task:
            md.add(2).add(2,5).subtract(3,2).result
        which should perform 0+2+(2+5)-(3+2) and return 4.
PART II
    Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:
            md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
        should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.
PART III
    Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.
'''

#PART I
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def displayInfo(self):
        print self.add, self.substract
        return self

    def addNum(self, *nums): #'*': wildcard
        self.add = 0
        for value in nums:
            self.add += value
        self.result += self.add
        return self

    def subsNum(self, *nums):
        self.substract = 0
        for value in nums:
            self.substract += value
            self.result -= self.substract
        return self

md = MathDojo()
print md.addNum(2).addNum(2,5).subsNum(3,2).result

#PART II
class MathDojo(object):
    def __init__(self):
        self.result = 0
 
    def add(self, *nums):
        for obj in nums:
            if type(obj) is list:
                for value in obj:
                    self.result += value
            elif type(obj) is int:
                    self.result += obj
        return self

    def substract(self, *nums):
        for obj in nums:
            if type(obj) is list:
                for value in obj:
                    self.result -= value
            elif type(obj) is int:
                    self.result -= obj
        return self

md = MathDojo()    
print md.add(2).add(3, 5, 7, 8).substract(5,5).result
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).substract(2, [2,3], [1.1, 2.3]).result

#PART III
class MathDojo(object):
  def __init__(self):
      self.result = 0
 
  def addNum(self, *nums):
      for obj in nums:
            if type(obj) is list:
                for value in obj:
                    self.result += value
            elif type(obj) is int:
                self.result += obj
            elif type(obj) is tuple:
                self.result += value
      return self
  def subsNum(self, *nums):
      for obj in nums:
            if type(obj) is list:
                for value in obj:
                    self.result -= value
            elif type(obj) is int:
                self.result -= obj
            elif type(obj) is tuple:
                self.result -= value    
      return self
      
md = MathDojo()   
print md.addNum(2).addNum(3, 5, 7, 8).subsNum(5,5).result
print md.addNum([1],3,4).addNum([3, 5, 7, 8], [2, 4.3, 1.25]).subsNum(2, [2,3], [1.1, 2.3]).result
