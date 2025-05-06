# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("Method from class A")

class B(A):
    def show(self):
        print("Method from class B")

class C(A):
    def show(self):
        print("Method from class C")

class D(B, C):
    pass

# Creating an object of class D
d = D()

# Calling the show() method to observe the Method Resolution Order (MRO)
d.show

# Printing the MRO to observe the order
print(D.mro())


# 16. Function Decorators
# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func() # Call the original function
    return wrapper

# Function to be decorated
@log_function_call
def say_hello():
    print("Hello, world!")

# Calling the decorated function
say_hello()


# 17. Class Decorators
# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

# Applying the class decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}"
    
# Creating an instance of the Person class
person = Person("Alice")

# Calling the greet method added by the decorator
print(person.greet())  # Output: Hello from Decorator!


# 18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Triggers the setter

    # Getter for the price attribute
    @property
    def price(self):
        return self._price

    # Setter to update the price attribute
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # Deleter to delete the price attribute
    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.name}")
        del self._price

# Creating a Product object
product = Product("Laptop", 1000)

# Accessing the price using the @property
print(product.price)  # Output: 1000 

# Updating the price using the @price.setter
product.price = 1200
print(product.price)  # Output: 1200

# Trying to set a negative price
product.price = -500  # Output: Price cannot be negative!

# Deleting the price using @price.deleter
del product.price  # Output: Deleting the price of Laptop
     

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Setting the factor

    def __call__(self, number):
        # This method allows the object to be called like a function
        return number * self.factor
    
# Creating an instance of Multiplier with a factor of 5
multiplier = Multiplier(5)

# Testing with callable() to check if the object is callable
print(callable(multiplier))  # Output: True

# Calling the object like a function to multiply an input by the factor
result = multiplier(10)  # This calls __call__(10) method
print(result)  # Output: 50


# 20. Creating a Custom Exception
# Custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age (must be outside the class)
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print(f"Age {age} is valid!")

# Handling the exception using try...except
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer for age.")


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start      # Set the starting number
        self.current = start    # Initialize current to the starting number

    def __iter__(self):
        # Return the iterator object itself
        return self

    def __next__(self):
        # If current is less than 0, stop the iteration
        if self.current < 0:
            raise StopIteration
        # Decrease current by 1 and return the value
        self.current -= 1
        return self.current + 1    # Return the number before decrementing

# Creating an object of Countdown
countdown = Countdown(5)

# Using the Countdown object in a for loop
for number in countdown:
    print(number)
