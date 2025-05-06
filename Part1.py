# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example Usage
student1 = Student("Sara", 88)
student1.display()

student2 = Student("Zara", 92)
student2.display()


# 2. Using cls
class Counter:
    object_count = 0 

    def __init__(self):
        # Har object banne par count barh jayega
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.object_count)

# Teen objects create kiye (class ke bahar)
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Class method call kiya
Counter.display_count()


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand # Public variable

    def start(self): # Public method
        print(f"{self.brand} car is starting...")

# Object ban rahe hain
my_car = Car("Toyota")

# Public Variables access
print("Car brand:", my_car.brand)

# Public method call
my_car.start()


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "Default Bank" # Class Variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name # Updating class variable

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Object creation
user1 = Bank("Ali")
user2 = Bank("Maya")    

# Pehle dono ka bank name check karo
user1.display()
user2.display()

# Class method sa bank name change karo
Bank.change_bank_name("Pakistan National Bank")

# Ab dono ka bank name dobara check karo
user1.display()
user2.display()


# 5. Static Variables and Static Methods
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
    
# static method call (no object needed)
result = MathUtils.add(10, 15)
print("The sum is:", result)


# 6. Constructors and Destructors
class Logger:

    # Constructor
    def __init__(self):
        print("Logger object has been created!")

    # Destructor
    def __del__(self):
        print("Logger object has been destroyed!")

# Create an object of Logger class
logger1 = Logger()

# Delete the object explicitly to invoke the destructor
del logger1 


# 7. Access Modifiers: Public, Private, and Protected
class Employee:
    # Public Variable
    name = "Zain"

    # Protected variable
    _salary = 50000

    # Private variable
    __ssn = "123-45-6789"

# Creating an object of Employee class
emp = Employee()

# Accessing the public variable
print("Name:", emp.name)

# Accessing the protected variable 
print("Salary:", emp._salary)

# Accessing the private variable (This will raise an error)
try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error:", e)

# Accessing the private variable via name mangling
print("SSN (via name mangling):", emp._Employee__ssn)

