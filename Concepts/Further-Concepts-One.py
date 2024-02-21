#############################################################################################
#                                                                                           #
#                                                                                           #
#                           SOME FURTHER PYTHON LEARNING CONCEPTS                           #
#                                                                                           #
#                                                                                           #
############################################################################################# 

#############################################################################################
# List Comprehensions:                                                                      #
#                                                                                           #
#	List comprehensions provide a concise way to create lists in Python.                    #
#	They are a way to apply an operation to each item in a sequence (like a list)           #
#	and collect the results into a new list.                                                #
#                                                                                           #
# Example of list comprehension                                                             #
squares = [x**2 for x in range(10)]                                                         #
#                                                                                           #
#############################################################################################

#############################################################################################
# Object-Oriented Programming - OOP:                                                        #
#                                                                                           #
#	Python supports object-oriented programming, which allows you to create                 #
#	classes and objects, encapsulate data, and define methods to operate on that data.      #
#                                                                                           #
# Example of defining a class                                                               #
class Dog:                                                                                  #
    def __init__(self, name):                                                               #
        self.name = name                                                                    #
#                                                                                           #
    def bark(self):                                                                         #
        print(self.name + " says Woof!")                                                    #
#                                                                                           #
my_dog = Dog("Buddy")                                                                       #
my_dog.bark()  # Output: Buddy says Woof!                                                   #
#                                                                                           #
#############################################################################################

#############################################################################################
# Exception Handling:                                                                       #
#                                                                                           #
#   Python provides a robust way to handle errors and exceptions using try, except,         #
#   finally, and raise statements.                                                          #
#                                                                                           #
# Example of exception handling                                                             #
try:                                                                                        #
    result = 10 / 0                                                                         #
except ZeroDivisionError:                                                                   #
    print("Cannot divide by zero")                                                          #
#                                                                                           #
#############################################################################################
    
#############################################################################################
# Modules and Packages:                                                                     #
#                                                                                           #
#   Python modules are files containing Python code that can be imported and used in other  #
#   Python scripts. Packages are namespaces that contain multiple modules. You can create   #
#   your own modules and packages or use existing ones from the Python Standard Library or  #
#   third-party libraries.                                                                  #
#                                                                                           #
# Example of importing modules                                                              #
import math                                                                                 #
print(math.sqrt(16))  # Output: 4.0                                                         #
#                                                                                           #
#############################################################################################

#############################################################################################
# File I/O:                                                                                 #
#                                                                                           #
#    Python provides built-in functions for reading from and writing to files on the disk.  #
#                                                                                           #
# Example of file I/O                                                                       #
with open("example.txt", "r") as file:                                                      #
    data = file.read()                                                                      #
#############################################################################################

#############################################################################################
# Virtual Environments:                                                                     #
#                                                                                           #
#   Virtual environments allow you to create isolated environments for Python projects,     #
#   with their own dependencies and packages. This is useful for managing project           #
#   dependencies and avoiding conflicts between different projects.                         #
#                                                                                           #
# Example of creating a virtual environment                                                 #
python -m venv myenv                                                                        #
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`                       #
#                                                                                           #
#############################################################################################

#############################################################################################
# Decorators:                                                                               #
#   Decorators are a powerful feature in Python that allow you to modify the behavior       #
#   of functions or methods. They are often used for logging, authentication, and           #
#   performance monitoring.                                                                 #
#                                                                                           #
# Example of defining a decorator                                                           #
def my_decorator(func):                                                                     #
    def wrapper():                                                                          #
        print("Something is happening before the function is called.")                      #
        func()                                                                              #
        print("Something is happening after the function is called.")                       #
    return wrapper                                                                          #
#                                                                                           #
@my_decorator                                                                               #
def say_hello():                                                                            #
    print("Hello!")                                                                         #
#                                                                                           #
say_hello()  # Output: Something is happening before the function is called.                #
             #         Hello!                                                               #
             #         Something is happening after the function is called.                 #
#                                                                                           #
#############################################################################################