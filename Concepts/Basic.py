#############################################################################################
#                                                                                           #
#                                                                                           #
#                                       PYTHON BASICS                                       #
#                                                                                           #
#                                                                                           #
############################################################################################# 

#############################################################################################
# VARIABLES AND DATA TYPES:                                                                 #
#                                                                                           #
#	In Python, you can store data in variables.                                             #
#	Common data types include integers, floats, strings,                                    #
#	booleans, lists, tuples, and dictionaries.                                              #
#                                                                                           #
# Example variable assignments                                                              #
#                                                                                           #
x = 5             # Integer                                                                 #
y = 3.14          # Float                                                                   #
name = "AydanS"    # String                                                                  #
is_student = True # Boolean                                                                 #
my_list = [1, 2, 3]      # List                                                             #
my_tuple = (4, 5, 6)     # Tuple                                                            #
my_dict = {"a": 1, "b": 2}  # Dictionary                                                    #
#                                                                                           #
#                                                                                           #
#############################################################################################

#############################################################################################
# BASIC OPERATIONS:                                                                         #
#                                                                                           #
#	Python supports common arithmetic operations like addition,                             #
#	subtraction, multiplication, and division.                                              #
#                                                                                           #
# Example arithmetic operations                                                             #
sum = 5 + 3                                                                                 #
difference = 7 - 2                                                                          #
product = 4 * 6                                                                             #
quotient = 10 / 2                                                                           #
#                                                                                           #
#############################################################################################

#############################################################################################
# CONTROL STRUCTURES:                                                                       #
#                                                                                           #
#	Python provides control structures like if statements, for loops,                       #
#	and while loops for decision-making and iteration.                                      #
#                                                                                           #
# Example if statement                                                                      #
if x > 0:                                                                                   #
    print("x is positive")                                                                  #
elif x < 0:                                                                                 #
    print("x is negative")                                                                  #
else:                                                                                       #
    print("x is zero")                                                                      #
#                                                                                           #
# Example for loop                                                                          #
for i in range(5):                                                                          #
    print(i)                                                                                #
#                                                                                           #
# Example while loop                                                                        #
count = 0                                                                                   #
while count < 5:                                                                            #
    print(count)                                                                            #
    count += 1                                                                              #
#                                                                                           #
#############################################################################################

#############################################################################################
# FUNCTIONS:
#                                                                                           #
#	Functions in Python allow you to                                                        #
#	encapsulate reusable blocks of code.                                                    #
#                                                                                           #
# Example function                                                                          #
def greet(name):                                                                            #
    print("Hello, " + name + "!")                                                           #
#                                                                                           #
greet("AydanS")  # Output: Hello, AydanS!                                                   #
#                                                                                           #
#############################################################################################

#############################################################################################
# INPUT AND OUTPUT:                                                                         #
#                                                                                           #
#	You can read input from the user and display output                                     #
#	using the input() and print() functions, respectively.                                  #
#                                                                                           #
# Example input and output                                                                  #
name = input("Enter your name: ")                                                           #
print("Hello, " + name + "!")                                                               #
#                                                                                           #
#############################################################################################

#############################################################################################
# COMMENTS:                                                                                 #
#                                                                                           #
#	Comments are used to add notes or explanations within the code.                         #
#	They start with the # symbol and are ignored by the Python interpreter.                 #
#                                                                                           #

# This is a single-line comment                                                             #

"""                                                                                         #
This is a multi-line comment. It can span across multiple lines.                            #
Can also be achieved with three ' instead of ".                                             #
Note that multi-line strings like these are actually valid strings in Python,               #
but if they are not assigned to a variable or used anywhere, they act as comments.          #
Can also be achieved with three ' instead of ".                                             #
"""                                                                                         #
#############################################################################################
