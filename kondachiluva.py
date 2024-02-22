#Running Python in the terminal session
print("Hello Python Interpreter!")
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
Stripping whitespace
favourite_language = 'Python  1'
print(favourite_language)

favourite_language = 'Java  1 2'
favourite_language.rstrip()
print(favourite_language)

favourite_language = 'Java  1 2'
favourite_language = favourite_language.rstrip()
print(favourite_language)

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
Avoiding syntax errors w/ strings
usage of single and double quotes in a correct format
message = "One of Python's strengths is its diverse community."
print(message)
