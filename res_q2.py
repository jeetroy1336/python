# Write a Python program that demonstrates method overriding 
# using a base class Animal and two derived classes Dog and Cat.

# The Animal class should have a method sound(self) that prints 
# "The animal makes a sound."

# The Dog class should override this method to print "The dog barks,"

# and the Cat class should override it to print "The cat meows."

# Create instances of Animal, Dog, and Cat,

# and call the sound() method on each object to demonstrate how 
# method overriding works by showing the respective sounds each animal makes.

class Animal:
    
    def sound(self):
        print("The animal makes a sound.")
class Dog(Animal):
    def sound(self):
        print("The dog barks")
class Cat(Dog):
    def sound(self):
        print("The cat meows")

a1 = Animal()
d1 = Dog()
c1 = Cat()

a1.sound()
d1.sound()
c1.sound()
    