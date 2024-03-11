# ---------------------------------------------------------------------------------------------------------------
# #CHAPTER - ONE (GETTING STARTED)
# ---------------------------------------------------------------------------------------------------------------
# #Running Python in the terminal session
# print("Hello Python Interpreter!")
# ---------------------------------------------------------------------------------------------------------------
# #CHAPTER - TWO (VARIABLES & SIMPLE DATATYPES)
# ---------------------------------------------------------------------------------------------------------------
# #Variables
# message = "Hello Python World!"
# print(message)

# message = "Hello Python Interpreter!"
# print(message)

# message = "Hello Python Crash Course World!"
# print(message)
# --------------------------------------------------------------
# #Strings
# #changing case in a string with methods
# name = "jeshwanth shiva sai"
# print(name.title())

# #upper method
# name = "jeshwanth shiva sai"
# print(name.upper())

# #lower method
# name = "jeshwanth shiva sai"
# print(name.lower())
# ----------------------------------------------------------------
# #Using Variable in Strings
# firstname = "Jeshwanth"
# middlename = "Shiva"
# lastname = "Sai"
# fullname = f"{firstname} {middlename} {lastname}"
# print(fullname)

# firstname = "schola"
# lastname = "eburouh"
# fullname = f"{firstname} {lastname}"
# print(f"Hello, {fullname.title()}!")

# firstname = "jeshwanth"
# lastname = "shiva sai"
# fullname = f"{firstname} {lastname}"
# message = f"Hello, {fullname.title()}!"
# print(message)
# ----------------------------------------------------------------
# #Add Whitespace to Strings with tabs or newlines
# #Add tab to text
# print("\tPython")

# #add newline to text
# print("Languages:\nPython\nC\nJava")

# #combination of tab and newline
# print("Languages:\n\tPython\n\tJava\n\tC")
# ----------------------------------------------------------------
# #Stripping whitespace
# favourite_language = 'Python  1'
# print(favourite_language)

# favourite_language = 'Java  1 2'
# favourite_language.rstrip()
# print(favourite_language)

# favourite_language = 'Java  1 2'
# favourite_language = favourite_language.rstrip()
# print(favourite_language)

# favourite_language = ' 2 1 Java'
# favourite_language = favourite_language.lstrip()
# print(favourite_language)

# favourite_language = ' 2 1 Java  1 2'
# favourite_language = favourite_language.strip()
# print(favourite_language)
# ----------------------------------------------------------------
# #Removing prefixes
# nostarch_url = 'http://nostarch.com'
# simple_url = nostarch_url.removeprefix('http://')
# print(simple_url)
# ----------------------------------------------------------------
# #Avoiding syntax errors w/ strings
# #usage of single and double quotes in a correct format
# message = "One of Python's strengths is its diverse community."
# print(message)
# ----------------------------------------------------------------
# #Numbers
# #(Integers: +, -, *, /)
# print(4+2)
# print(4-2)
# print(4*2)
# print(4/2)

# #two symbols to represent exponents
# print(3**2)
# print(3**10)

# #usage of multiple operators
# print(2+3*4)
# print((2+3)*4)
# ----------------------------------------------------------------
# #floats
# print(0.1+0.1)
# print(0.2+0.2)
# print(2*0.1)
# print(2*0.2)
# print(0.2+0.1)
# print(0.3+0.1)
# ----------------------------------------------------------------
# #Integers and floats
# #divide_two_numbers = float
# print(4/2)
# #mix_integer_and_float = float
# print(1+2.0)
# print(2*2.0)
# print(3.0**3)
# ----------------------------------------------------------------
# #Underscores in numbers
# mymemory=1_00_00_00_00_00_00_00_00_00_00_00_00_00_000
# print(mymemory)
# ----------------------------------------------------------------
# #Multiple_assignment
# x, y, z = 0, 1, 2
# print(x)
# print(y)
# print(z)
# ----------------------------------------------------------------
# #Constants
# #uppercase_to_indicate_variable_to_treat_as_a_constant
# MY_AGE = 25
# print(MY_AGE)
# ----------------------------------------------------------------
# #Comments
# #say hello world
# print("Hello world!")
# ----------------------------------------------------------------
# #Zen of Python
# import  this
# ---------------------------------------------------------------------------------------------------------------
# #CHAPTER - THREE (INTRODUCING LISTS)
# ---------------------------------------------------------------------------------------------------------------
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# ----------------------------------------------------------------
# #accessing elements in the list
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[1])

# #more presentable format
# print(vegetables[1].title())
# ----------------------------------------------------------------
# #index starts at 0 and not 1
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[1])
# print(vegetables[3])

# #last index starts at '-1' (when not sure how long the list is)
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[-1])

# #(for second last item in the list and so on and so forth)
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[-2])
# ----------------------------------------------------------------
# #using individual values from a list
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# message = f"My Favorite Vegetable is {vegetables[1].title()}."
# print(message)
# ----------------------------------------------------------------
# #Modifying, Adding and removing elements
# #modifying elements in a list
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# vegetables[3] = "bottlegourd"
# print(vegetables)
# ----------------------------------------------------------------
# #Adding elements to a list
# #appending elements to the end of a list
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# vegetables.append('bottlegourd')
# print(vegetables)

# vegetables = []
# vegetables.append('beetroot')
# vegetables.append('capscicum')
# vegetables.append('carrot')
# vegetables.append('ridgegourd')
# print(vegetables)

# #inserting elements into a list
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# vegetables.insert(0, 'cauliflower')
# print(vegetables)
# ----------------------------------------------------------------
# #Removing elements from a list
# #removing an item using the DEL statement
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# del vegetables[2]
# print(vegetables)

# #removing an item using the pop() method
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# popveg = vegetables.pop()
# print(vegetables)
# print(popveg)

# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# notvegetable = vegetables.pop()
# print(f"Very hard texture and it is {notvegetable.title()}.")
# ----------------------------------------------------------------
# #popping items from any position in a list
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# popveg = vegetables.pop(2)
# print(vegetables)
# print(popveg)

# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# notvegetable = vegetables.pop(2)
# print(f"Very hard texture and it is {notvegetable.title()}.")
# ----------------------------------------------------------------
# #Removing an item by value
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(vegetables)
# vegetables.remove('tomato')
# print(vegetables)

# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(vegetables)
# notvegetables = 'tomato'
# vegetables.remove(notvegetables)
# print(vegetables)
# print(f"Since {notvegetables.title()} is a fruit.")
# ----------------------------------------------------------------
# #Organizing a list
# #sorting a list "permanently" with the "sort()" method
# #alphabetical order
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.sort()
# print(vegetables)

# #reverse alphabetical order
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.sort(reverse=True)
# print(vegetables)
# ----------------------------------------------------------------
# #sorting a list "temporarily" with the "sorted()" method
# #alphabetical order
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(sorted(vegetables))

# #reverse alphabetical order
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.sort(reverse=True)
# print(vegetables)
# ----------------------------------------------------------------
# #printing a list in reverse order
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.reverse()
# print(vegetables)
# ----------------------------------------------------------------
# #finding the length of a list
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(len(vegetables))
# ----------------------------------------------------------------
# #Avoiding index errors when working with lists
#wantedly making mistakes (3 items but asking for 4th index)
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(vegetables[4])
# ---------------------------------------------------------------------------------------------------------------
# #CHAPTER - FOUR (WORKING WITH LISTS)
# ---------------------------------------------------------------------------------------------------------------
# #Looping through an entire list
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# for veg in vegetables:
#     print(veg)
#----------------------------------------------------------------
# #Doing more work within a loop
# friends = ['idioteye', 'kc', 'schola', 'ramya']
# for dosth in friends:
#     print(f"{dosth.title()}, nuv evaro nak telvadu")
#     print(f"evarra meerantha, {dosth.title()} \n")
#----------------------------------------------------------------
# #Doing something after a for loop
# friends = ['idioteye', 'kc', 'schola', 'ramya']
# for dosth in friends:
#     print(f"{dosth.title()}, nuv evaro nak telvadu")
#     print(f"evarra meerantha, {dosth.title()} \n")
# print("Dandam ra andarki")
#----------------------------------------------------------------
# #Making numerical lists
# #using range() function
# for value in range(1,11):
#     print(value)

# #using range() to make a "LIST OF NUMBERS"
# numbers = list(range(1,11))
# print(numbers)

# #print only even numbers
# numbers = list(range(0,11,2))
# print(numbers)

# #print sqrs of numbers
# sqrs = [] #take an empty list
# for x in range(1,11): #let x be the number
#     square = x**2 #x i.e num to the pow 2 resulting in a sq
#     sqrs.append(square) #appending the nums to the sqrs list

# print(sqrs) #print the list

# #OR (LIST COMPREHENSION METHOD)

# sqrs = [x**2 for x in range(1,11)]
# print(sqrs)

# #OR

# sqrs = []
# for value in range(1,11):
#     sqrs.append(value**2)
# print(sqrs)

# # simple statistics with a list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# min(numbers)
# print(min(numbers))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# max(numbers)
# print(max(numbers))\
#----------------------------------------------------------------
# #Working with part of a list
# #slicing a list
# friends = ['ajey', 'kc', 'schola', 'ramya', 'selwyn']
# print(friends[0:3])
# #beginning of list (output from start to the given no.)
# print(friends[:4])
# #ending of a list (output from the given no. to end)
# print(friends[4:])
# #negative index (output only last elements of given no.)
# print(friends[-4:])

# #looping through a list
# friends = ['ajey', 'kc', 'schola', 'ramya', 'selwyn']
# print("First 3 friends :")
# for friend in friends[0:3]:
#     print(friend)

# #copying through a list
# myfav = ['pizza', 'cake', 'biryani', 'haleem', 'rasmalai']
# friend_fav = myfav[:]
# print("My fav first :")
# print(myfav)
# print("\nMy friends fav are :")
# print(friend_fav)

# #add new item to list
# myfav.append('pappu')
# print(myfav)
# friend_fav.append('avakay')
# print(friend_fav)
#----------------------------------------------------------------
# #Tuples
# #defining a tuple
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# print('The first 11 positive integers are :', numbers)
# print(numbers)

# #looping through all values in a tuple
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# for number in numbers:
#     print(number)

# #writing over a tuple
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# print('The first 11 negative integers are :', numbers)
# for number in numbers:
#     print(number)

# numbers = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
# print('\nThe first 11 negative integers in reverse are :', numbers)
# for number in numbers:
#     print(number)
# ---------------------------------------------------------------------------------------------------------------
# #CHAPTER - FIVE ()
# ---------------------------------------------------------------------------------------------------------------
# #A simple example
# fav = ['michael_jackson', 'odesza', 'dyalla', 'spb']
# for musician in fav:
#     if musician == 'odesza':
#         print(musician.upper())
#     else:
#         print(musician.title())

# #Conditional tests
# #checking for equality
# name = 'jesh'
# name == 'jesh'
# print(name)

# #Ignoring case when checking for equality
# name = 'jesh'
# name.upper() == 'Jesh'
# print(name)

# #checking for inequality
username = 'jeshwanthshivasai'
if username != 'jeshwanthss':
    print("Wrong username!")

# #Numerical comparisons
number = 11
if number != 9:
    print("Wrong number!")

# #Checking multiple conditions