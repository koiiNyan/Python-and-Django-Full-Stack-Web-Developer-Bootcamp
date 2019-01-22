# Creating a Dog class
class Dog():
    # Class Object attribute for every instance of the class
    species = "mammal"
    # Initialization
    def __init__(self,breed,name):
        # Self refers to itself, being the actual class obj
        self.breed = breed
        self.name = name

# myDog = Dog("Lab","Sammy")
# Breed is an attribute and not a method so there're no parentheses.
# print(myDog.breed)
# print(myDog.name)
# print(myDog.species)


class Circle():
    pi = 3.14
    # If don't provide a radius, it will be 1 by default
    def __init__(self,radius=1):
        self.radius = radius

    # Method of a class
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Resetting att
    def set_radius(self,new_radius):
        self.radius = new_radius


# myc = Circle(3)
# # myc.radius = 100
# myc.set_radius(999)
# print(myc.area())


#############################
# INHERITANCE & SPECIAL METHODS

class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

# mya = Animal()
# mya.whoAmI()
# mya.eat()


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("CAT CREATED")

    def nya(self):
        print("MEOW")

    # Overwritting
    def eat(self):
        print("CAT EATING")

# myc = Cat()
# myc.whoAmI()
# myc.eat()
# myc.nya()

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Special Method. String representation for the object
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    # Delete an object from the memory space
    def __del__(self):
        print("A book has been destroyed! :c")

b = Book("Python", "Jose", 200)
# When you call the print() on an obhect it looks for its string representation.
print(b)
print(len(b))
del b
