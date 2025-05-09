
class an:
    def hei():
        return 1

h=an
print(type(h)) #result <class 'type'>

#in python everything is a object if we define a class that is also 
# a object if class type / otherwise it self is a object


def cake():

    c="cake"

    global stobery

    def stobery():
        return c

def ice():
    return "ice "

#above code cake() and ice() are the objects of the string class.
#when runnig the code looks the same frame (cake and ice)
# but stobery is not in the same frame to do it we need to mention
# it as global, then we can access it


class abc:
    pass
              
class ghi:
    f=abc

v=ghi()
b=ghi()

print(v)#<__main__.ghi object at 0x000001BDF7E9F790>
print(b) #<__main__.ghi object at 0x000001BDF7E9F7D0>

# above code i build two class objects as abc and ghi these two classes
#are itself objects of type class, so every thing in python in objects
#you can see it int he object address. i build a two new instances of ghi
# class and these two instances are refers using variable v and b

class abc:
    def ghi(lk):
        print(lk) #<__main__.abc object at 0x00000297E6D7FC90>
    
    def pqr(self):
        return 3
    
    def __call__(self):
        return 2

a = abc()
a.ghi()
print(a) #<__main__.abc object at 0x00000297E6D7FC90>

#in above refers the self or anything is self==a


class abc:
    def value(self, x):
        self.data = x
        self.p=4

    def show_value(self):
        print(self.data)

obj1 = abc()
obj2 = abc()

obj1.value(10)
obj2.value(20)

obj1.show_value() # Output: 10
obj2.show_value()   # Output: 20

#self refers to the object and inside the object make a variable as data and stores value

class abc:
    def value(self, x):
        self.data = x
        self.p = 4

obj1 = abc()
obj2 = abc()

obj1.value(10)
obj2.value(10)

print("obj1.data id =", id(obj1.data))
print("obj2.data id =", id(obj2.data))

print("obj1.__dict__ =", obj1.__dict__)
print("obj2.__dict__ =", obj2.__dict__)

# we can see the share the value 10 both means has the same memory address
#for both objects data 

