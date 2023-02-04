# program to create and access an obj

class abc:
    var=10
obj=abc()
print(obj.var)

# program to create self arg  and access an obj

class abc:
    var=10
    print("steve smith")
    def display(self):
        print("hi hero")
obj=abc()
print(obj.var)
obj.display()

# program to check usage of a constructor

class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("the value is",value)
    
obj=abc(100)

# program to check usage of a constructor

class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("the obj value is ",var)
        
        print("the class value is ",abc.class_var)
    
obj1=abc(100)
obj2=abc(101)
obj3=abc(102)

# program to check number is odd or even

class Number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
            
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=Number()
n.even_odd(22)

"""wap THAT AS A CLASS NAME CIRCLE USE A CLASS VARIABLE TO DEFINE THE VALUES OF A CONSTANT
USE THIS CLASS VARible to caclulate area and cirucmferencer of the circle where the radius """

"""circumference = 2 * PI * radius
area = PI * radius * radius"""
class Circle:
    PI = 3.142
    
    def __init__(self, radius):
        self.radius = radius
        
    def area (self):
        return (Circle.PI * self.radius * self.radius)
    
    def circumference(self):
        return (2 * Circle.PI * self.radius)

r = int(input("Enter the radius of circle"))
c1 = Circle(r)
print ("The area of C1 circle is: ", c1.area())
print ("Circumference of C1 Circle is: ", c1.circumference())
print("")
r = int(input("Enter the radius of circle"))
c2 = Circle(r)
print ("Area of C1 circle is: ", c2.area())
print ("Circumference of C1 Circle is: ", c2.circumference())

