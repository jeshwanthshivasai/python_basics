#CHAPTER - ONE (GETTING STARTED)
--------------------------------------------------------------
#Running Python in the terminal session
print("Hello Python Interpreter!")
--------------------------------------------------------------
#CHAPTER - TWO (VARIABLES & SIMPLE DATATYPES)
--------------------------------------------------------------
#Variables
message = "Hello Python World!"
print(message)

message = "Hello Python Interpreter!"
print(message)

message = "Hello Python Crash Course World!"
print(message)
--------------------------------------------------------------
#Variables are labels
#1 Simple Message
message = "Hello Python"
print(message)

#2 Simple Messages
message = "Hello Python Program"
print(message)
message = "Hello Python Programming"
print(message)
--------------------------------------------------------------
#Strings
#title method
name = "jeshwanth shiva sai"
print(name.title())

#upper method
name = "jeshwanth shiva sai"
print(name.upper())

#lower method
name = "jeshwanth shiva sai"
print(name.lower())
----------------------------------------------------------------
#Variable in string
firstname = "Jeshwanth"
middlename = "Shiva"
lastname = "Sai"
fullname = f"{firstname} {middlename} {lastname}"
print(fullname)

firstname = "schola"
lastname = "eburouh"
fullname = f"{firstname} {lastname}"
print(f"Hello, {fullname.title()}!")

firstname = "jeshwanth"
lastname = "shiva sai"
fullname = f"{firstname} {lastname}"
message = f"Hello, {fullname.title()}!"
print(message)
----------------------------------------------------------------
#Add tab to text
print("\tPython")

#add newline to text
print("Languages:\nPython\nC\nJava")

#combination of tab and newline
print("Languages:\n\tPython\n\tJava\n\tC")
----------------------------------------------------------------
#Stripping whitespace
favourite_language = 'Python  1'
print(favourite_language)

favourite_language = 'Java  1 2'
favourite_language.rstrip()
print(favourite_language)

favourite_language = 'Java  1 2'
favourite_language = favourite_language.rstrip()
print(f avourite_language)

favourite_language = ' 2 1 Java'
favourite_language = favourite_language.lstrip()
print(favourite_language)

favourite_language = ' 2 1 Java  1 2'
favourite_language = favourite_language.strip()
print(favourite_language)
----------------------------------------------------------------
#Removing prefixes
nostarch_url = 'http://nostarch.com'
simple_url = nostarch_url.removeprefix('http://')
print(simple_url)
----------------------------------------------------------------
#Avoiding syntax errors w/ strings
#usage of single and double quotes in a correct format
message = "One of Python's strengths is its diverse community."
print(message)
----------------------------------------------------------------
#Numbers
#(INTEGERS: +, -, *, /)
print(4+2)
print(4-2)
print(4*2)
print(4/2)
#two_symbols_to_represent_exponents
print(3**2)
print(3**10)
#usage_of_multiple_operators
print(2+3*4)
print((2+3)*4)
#(FLOATS)
print(0.1+0.1)
print(0.2+0.2)
print(2*0.1)
print(2*0.2)
print(0.2+0.1)
print(0.3+0.1)
#INTEGERS_AND_FLOATS
#divide_two_numbers = float
print(4/2)
#mix_integer_and_float = float
print(1+2.0)
print(2*2.0)
print(3.0**3)
#underscores
mymemory=1_00_00_00_00_00_00_00_00_00_00_00_00_00_000
print(mymemory)
#multiple_assignment
x, y, z = 0, 1, 2
print(x)
print(y)
print(z)
#constants
#uppercase_to_indicate_variable_to_treat_as_a_constant
MY_AGE = 25
print(MY_AGE)
----------------------------------------------------------------
#Comments
#say hello world
print("Hello world!")
----------------------------------------------------------------
#Zen_of_Python
import  this
----------------------------------------------------------------
#CHAPTER - THREE (INTRODUCING LISTS)
----------------------------------------------------------------
