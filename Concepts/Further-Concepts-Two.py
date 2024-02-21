#############################################################################################
#                                                                                           #
#                                                                                           #
#                           SOME FURTHER PYTHON LEARNING CONCEPTS                           #
#                                                                                           #
#                                                                                           #
############################################################################################# 

#############################################################################################
# Generators and Iterators:                                                                 #
#                                                                                           #
#   Generators are a type of iterable, like lists or tuples, but they generate their values #
#   lazily. This means they generate values one at a time and only when needed, which can   # 
#   save memory and improve performance.                                                    # 
#                                                                                           #
# Example of a generator                                                                    #
def square_numbers(nums):                                                                   #
    for num in nums:                                                                        #
        yield num * num                                                                     #
#                                                                                           #
my_nums = square_numbers([1, 2, 3, 4, 5])                                                   #
print(next(my_nums))  # Output: 1                                                           #
print(next(my_nums))  # Output: 4                                                           #
#                                                                                           #
#############################################################################################

#############################################################################################
#Concurrency and Parallelism:                                                               #
#                                                                                           #
#   Python offers several libraries and modules for concurrent and parallel programming,    #
#   such as asyncio for asynchronous programming, and multiprocessing and threading for     #
#   parallel execution.                                                                     #
#                                                                                           #
# Example of asynchronous programming with asyncio                                          #
import asyncio                                                                              #
#                                                                                           #
async def hello():                                                                          #
    print("Hello")                                                                          #
    await asyncio.sleep(1)                                                                  #
    print("World")                                                                          #
#                                                                                           #
asyncio.run(hello())                                                                        #
#                                                                                           #
#############################################################################################

#############################################################################################
# Functional Programming:                                                                   #
#                                                                                           #
#   Python supports functional programming paradigms, including higher-order functions,     #
#   lambda functions, and functions like map, filter, and reduce.                           #
#                                                                                           #
# Example of using map and lambda function                                                  #
numbers = [1, 2, 3, 4, 5]                                                                   #
squared = map(lambda x: x**2, numbers)                                                      #
print(list(squared))  # Output: [1, 4, 9, 16, 25]                                           #
#                                                                                           #
#############################################################################################

#############################################################################################
# Regular Expressions (Regex):                                                              #
#                                                                                           #
#   Regular expressions are a powerful tool for pattern matching and text processing.       #
#   Python's re module provides support for working with regular expressions.               #
#                                                                                           #
# Example of using regular expressions                                                      #
import re                                                                                   #
pattern = r'\b(\w+)\s+\1\b'  # Match repeated words                                         #
text = "hello hello world"                                                                  #
matches = re.findall(pattern, text)                                                         #
print(matches)  # Output: ['hello']                                                         #
#                                                                                           #
#############################################################################################

#############################################################################################
# Closures and Scope:                                                                       #
#                                                                                           #
# Python supports closures, which are functions that remember the values from the           #
# enclosing lexical scope even when the scope has finished executing.                       #
#                                                                                           #
# Example of closure                                                                        #
def outer_function(message):                                                                #
    def inner_function():                                                                   #
        print(message)                                                                      #
    return inner_function                                                                   #
#                                                                                           #
my_func = outer_function("Hello")                                                           #
my_func()  # Output: Hello                                                                  #
#                                                                                           #
#############################################################################################
