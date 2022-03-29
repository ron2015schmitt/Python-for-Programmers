class Dog:
    info = "A Dog is a mammal" # class variable
    def barkhello():
        print("Woof Woof")

print(Dog.info)
dog1 = Dog()
dog1.name = "Fido" #instance variable
print(dog1.info)
print(dog1.name)
Dog.info = "N/A"
print(Dog.info)
print(dog1.info)

Dog.barkhello()

# dog1.barkhello()  # can;t call class method on instance
dog1.__class__.barkhello()

dog2 = Dog()
dog3 = Dog()

class Car:
    definition = "Something with 4 wheels and an engine"




class Dog:
    info = "A Dog is a mammal" # class variable
    def __init__(self, name, age, furcolor):   # can name 1st parameter anything you want. it will be the instance
        print("inside init")
        # instance vars
        self.name = name
        self.age = age
        self.furcolor = furcolor
    pass # end of class defs
    # now these are instance methods
    def barkhello(self):
        print("Woof Woof")
    def barkgoodbye(self):
        print("Woof!!")

dog1 = Dog("Fido", 3, "Black")
print(dir(dog1))
print(vars(dog1))


class BullDog(Dog): 
    pass # end of class defs
    def growl(self):  # instance methods must always have self parameter
        print("GRRRWL")

class Hound(Dog): pass   # pass is used when you don;t want other propertieds


dog4 = BullDog("Fido", 3, "Black")
print(dog4.growl())
print(dog4.barkhello())



class IterMixin(object):
    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value

class Car:
    def __init__(this, year, make, model):  
        this.year = year
        this.make = make
        this.model = model
        
    def age(self): return 2016 - self.year

mycar = Car(2000, "Honda", "Accord")

print(mycar.age())




class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def age(self):
        return 2016 - self.year

class Mustang(Car):
    def __init__(self, year):
        super().__init__(year, "Ford", "Mustang")

mine = Mustang(1960)    

print(vars(mine))


# use     super().__init__('Mammal') to call class method on parent class
