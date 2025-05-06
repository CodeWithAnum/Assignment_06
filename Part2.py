# 8. The super() Function
# Base class Person
class Person:
    def __init__(self, name):
        self.name = name

# Derived class Teacher
class Teacher(Person):
    def __init__(self, name, subject):
        # Calling the base class constructor using super()
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Teacher class ka object bana rahe ha
teacher = Teacher("Mr. Ali jawad", "Mathematics")

# Teacher ki details display kar rahe hain
teacher.display() 


# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Class Rectangle that inherits from Shape and implements the area method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# Creating an object of Rectangle and calling the area method
rect = Rectangle(5, 10)
print(f"Area of Rectangle: {rect.area()}")


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method that prints a message with the dog's name
        print(f"{self.name} says woof!")

# Creating an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Calling the bark method 
my_dog.bark()


# 11. Class Methods
class Book:
    # Class variable to track the total number of books
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        # Increment the total_books count when a new book is added
        cls.total_books += 1

    def __init__(self, title, author):
        # Instance variables
        self.title = title
        self.author = author
        # Call the class method to increment the book count when a new book is created
        Book.increment_book_count()

# Creating new book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

# Accessing the class variable
print(f"Total books: {Book.total_books}")


# 12. Static Methods
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(C):
        # Formula to convert Celsius to Fahrenheit
        return (C * 9/5) + 32
    
# Calling the static method without creating an instance of the class
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")


# 13. Composition
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return f"The {self.engine_type} engine is starting."
    
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        # Composition: Passing an Engine object to the car class
        self.engine = engine

    def start_car(self):
        # Accessing the start method of the Engine class via the Car class
        return f"{self.brand} car is starting. {self.engine.start()}"
    
# Creating an Engine object
engine = Engine("V8")

# Creating a Car object and passing the Engine object to it
car = Car("Ford", engine)

# Calling the start_car method which uses the Engine's start method
print(car.start_car())


# 14. Aggregation
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_info(self):
        return f"Employee Name: {self.name}, Position: {self.position}"
    
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        # Aggregation: Storing a reference to an Employee object
        self.employee = employee

    def get_department_info(self):
        return f"Department: {self.department_name}, Employee: {self.employee.get_employee_info()}"
    
# Creating an Employee object
employee1 = Employee("Sara", "Software Engineer")

# Creating a Department object and passing the Employee object to it
department1 = Department("IT Department", employee1)

# Calling the method to get the department and employee info
print(department1.get_department_info())

