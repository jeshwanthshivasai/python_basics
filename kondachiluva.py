# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - ONE (GETTING STARTED)'''
# ---------------------------------------------------------------------------------------------------------------
'''Running Python in the terminal session'''
# print("Hello Python Interpreter!")
# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - TWO (VARIABLES & SIMPLE DATATYPES)'''
# ---------------------------------------------------------------------------------------------------------------
'''Variables'''
# message = "Hello Python World!"
# print(message)

# message = "Hello Python Interpreter!"
# print(message)

# message = "Hello Python Crash Course World!"
# print(message)
# -------------------------------------------------------------------------------
'''Strings'''
'''changing case in a string with methods'''
# name = "jeshwanth shiva sai"
# print(name.title())

'''upper method'''
# name = "jeshwanth shiva sai"
# print(name.upper())

'''lower method'''
# name = "jeshwanth shiva sai"
# print(name.lower())
# -------------------------------------------------------------------------------
'''Using Variable in Strings'''
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
# -------------------------------------------------------------------------------
'''Add Whitespace to Strings with tabs or newlines'''
'''Add tab to text'''
# print("\tPython")

'''add newline to text'''
# print("Languages:\nPython\nC\nJava")

'''combination of tab and newline'''
# print("Languages:\n\tPython\n\tJava\n\tC")
# -------------------------------------------------------------------------------
'''Stripping whitespace'''
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
# -------------------------------------------------------------------------------
'''Removing prefixes'''
# nostarch_url = 'http://nostarch.com'
# simple_url = nostarch_url.removeprefix('http://')
# print(simple_url)
# -------------------------------------------------------------------------------
'''Avoiding syntax errors w/ strings'''
'''usage of single and double quotes in a correct format'''
# message = "One of Python's strengths is its diverse community."
# print(message)
# -------------------------------------------------------------------------------
'''Numbers'''
'''(Integers: +, -, *, /)'''
# print(4+2)
# print(4-2)
# print(4*2)
# print(4/2)

'''two symbols to represent exponents'''
# print(3**2)
# print(3**10)

'''usage of multiple operators'''
# print(2+3*4)
# print((2+3)*4)
# -------------------------------------------------------------------------------
'''floats'''
# print(0.1+0.1)
# print(0.2+0.2)
# print(2*0.1)
# print(2*0.2)
# print(0.2+0.1)
# print(0.3+0.1)
# -------------------------------------------------------------------------------
'''Integers and floats'''
'''divide_two_numbers = float'''
# print(4/2)
'''mix_integer_and_float = float'''
print(1+2.0)
print(2*2.0)
print(3.0**3)
# -------------------------------------------------------------------------------
'''Underscores in numbers'''
# mymemory=1_00_00_00_00_00_00_00_00_00_00_00_00_00_000
# print(mymemory)
# -------------------------------------------------------------------------------
'''Multiple_assignment'''
# x, y, z = 0, 1, 2
# print(x)
# print(y)
# print(z)
# -------------------------------------------------------------------------------
'''Constants'''
'''uppercase_to_indicate_variable_to_treat_as_a_constant'''
# MY_AGE = 25
# print(MY_AGE)
# -------------------------------------------------------------------------------
'''Comments'''
'''say hello world'''
# print("Hello world!")
# -------------------------------------------------------------------------------
'''Zen of Python'''
# import  this
# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - THREE (INTRODUCING LISTS)'''
# ---------------------------------------------------------------------------------------------------------------
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# -------------------------------------------------------------------------------
'''accessing elements in the list'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[1])

'''more presentable format'''
# print(vegetables[1].title())
# -------------------------------------------------------------------------------
'''index starts at 0 and not 1'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[1])
# print(vegetables[3])

'''last index starts at '-1' (when not sure how long the list is)'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[-1])

'''(for second last item in the list and so on and so forth)'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables[-2])
# -------------------------------------------------------------------------------
'''using individual values from a list'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# message = f"My Favorite Vegetable is {vegetables[1].title()}."
# print(message)
# -------------------------------------------------------------------------------
'''Modifying, Adding and removing elements'''
'''modifying elements in a list'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# vegetables[3] = "bottlegourd"
# print(vegetables)
# -------------------------------------------------------------------------------
'''Adding elements to a list'''
'''appending elements to the end of a list'''
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

'''inserting elements into a list'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# vegetables.insert(0, 'cauliflower')
# print(vegetables)
# -------------------------------------------------------------------------------
'''Removing elements from a list'''
'''removing an item using the DEL statement'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# del vegetables[2]
# print(vegetables)

'''removing an item using the pop() method'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# popveg = vegetables.pop()
# print(vegetables)
# print(popveg)

# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# notvegetable = vegetables.pop()
# print(f"Very hard texture and it is {notvegetable.title()}.")
# -------------------------------------------------------------------------------
'''popping items from any position in a list'''
# vegetables = ['beetroot', 'capsicum', 'carrot', 'ridgegourd']
# print(vegetables)
# popveg = vegetables.pop(2)
# print(vegetables)
# print(popveg)

# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# notvegetable = vegetables.pop(2)
# print(f"Very hard texture and it is {notvegetable.title()}.")
# -------------------------------------------------------------------------------
'''Removing an item by value'''
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
# -------------------------------------------------------------------------------
'''Organizing a list'''
'''sorting a list "permanently" with the "sort()" method'''
'''alphabetical order'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.sort()
# print(vegetables)

'''reverse alphabetical order'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.sort(reverse=True)
# print(vegetables)
# -------------------------------------------------------------------------------
'''sorting a list "temporarily" with the "sorted()" method'''
'''alphabetical order'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(sorted(vegetables))

'''reverse alphabetical order'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.sort(reverse=True)
# print(vegetables)
# -------------------------------------------------------------------------------
'''printing a list in reverse order'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# vegetables.reverse()
# print(vegetables)
# -------------------------------------------------------------------------------
'''finding the length of a list'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(len(vegetables))
# -------------------------------------------------------------------------------
'''Avoiding index errors when working with lists'''
'''wantedly making mistakes (3 items but asking for 4th index)'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# print(vegetables[4])
# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - FOUR (WORKING WITH LISTS)'''
# ---------------------------------------------------------------------------------------------------------------
'''Looping through an entire list'''
# vegetables = ['beetroot', 'capsicum', 'tomato', 'ridgegourd']
# for veg in vegetables:
#     print(veg)
#--------------------------------------------------------------------------------
'''Doing more work within a loop'''
# friends = ['idioteye', 'kc', 'schola', 'ramya']
# for dosth in friends:
#     print(f"{dosth.title()}, nuv evaro nak telvadu")
#     print(f"evarra meerantha, {dosth.title()} \n")
#--------------------------------------------------------------------------------
'''Doing something after a for loop'''
# friends = ['idioteye', 'kc', 'schola', 'ramya']
# for dosth in friends:
#     print(f"{dosth.title()}, nuv evaro nak telvadu")
#     print(f"evarra meerantha, {dosth.title()} \n")
# print("Dandam ra andarki")
#--------------------------------------------------------------------------------
'''Making numerical lists'''
'''using range() function'''
# for value in range(1,11):
#     print(value)

'''using range() to make a "LIST OF NUMBERS'''
# numbers = list(range(1,11))
# print(numbers)

'''print only even numbers'''
# numbers = list(range(0,11,2))
# print(numbers)

'''print sqrs of numbers'''
# sqrs = [] #take an empty list
# for x in range(1,11): #let x be the number
#     square = x**2 #x i.e num to the pow 2 resulting in a sq
#     sqrs.append(square) #appending the nums to the sqrs list

# print(sqrs) #print the list

'''OR (LIST COMPREHENSION METHOD)'''

# sqrs = [x**2 for x in range(1,11)]
# print(sqrs)

'''OR'''

# sqrs = []
# for value in range(1,11):
#     sqrs.append(value**2)
# print(sqrs)

'''simple statistics with a list of numbers'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# min(numbers)
# print(min(numbers))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# max(numbers)
# print(max(numbers))\
#--------------------------------------------------------------------------------
'''Working with part of a list'''
'''slicing a list'''
# friends = ['ajey', 'kc', 'schola', 'ramya', 'selwyn']
# print(friends[0:3])
'''beginning of list (output from start to the given no.)'''
# print(friends[:4])
'''ending of a list (output from the given no. to end)'''
# print(friends[4:])
'''negative index (output only last elements of given no.)'''
# print(friends[-4:])

'''looping through a list'''
# friends = ['ajey', 'kc', 'schola', 'ramya', 'selwyn']
# print("First 3 friends :")
# for friend in friends[0:3]:
#     print(friend)

'''copying through a list'''
# myfav = ['pizza', 'cake', 'biryani', 'haleem', 'rasmalai']
# friend_fav = myfav[:]
# print("My fav first :")
# print(myfav)
# print("\nMy friends fav are :")
# print(friend_fav)

'''add new item to list'''
# myfav.append('pappu')
# print(myfav)
# friend_fav.append('avakay')
# print(friend_fav)
#--------------------------------------------------------------------------------
'''Tuples'''
'''defining a tuple'''
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# print('The first 11 positive integers are :', numbers)
# print(numbers)

'''looping through all values in a tuple'''
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# for number in numbers:
#     print(number)

'''writing over a tuple'''
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# print('The first 11 negative integers are :', numbers)
# for number in numbers:
#     print(number)

# numbers = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
# print('\nNegative integers in reverse are :', numbers)
# for number in numbers:
#     print(number)
# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - FIVE (IF STATEMENTS)'''
# ---------------------------------------------------------------------------------------------------------------
'''A simple example'''
# fav = ['michael_jackson', 'odesza', 'dyalla', 'spb']
# for musician in fav:
#     if musician == 'odesza':
#         print(musician.upper())
#     else:
#         print(musician.title())

'''Conditional tests'''
'''Checking for equality'''
# name = 'jesh'
# print(name == 'jesh')

'''Ignoring case when checking for equality'''
# name = 'jesh'
# print(name.upper() == 'Jesh')

'''Checking for inequality'''
# username = 'jeshwanthshivasai'
# if username != 'jeshwanthss':
#     print("Wrong username!")

'''Numerical comparisons'''
# number = 11
# if number != 9:
#     print("Wrong number!")

'''Checking multiple conditions'''
'''Using "and" to check multiple conditions'''
# age1 = 18
# age2 = 20
# print((age1 >= 20) and (age2 >= 20))

'''Using "or" to check multiple conditions'''
# age1 = 18
# age2 = 20
# print((age1 <= 20) or (age2 <= 20))

'''Checking whether a value is in a List'''
# fav = ['michael_jackson', 'odesza', 'dyalla', 'spb']
# print('odesza' in fav)

'''Checking whether a value is not in a List'''
# fav = ['michael_jackson', 'odesza', 'dyalla', 'spb']
# singer = 'odesza'
# if singer not in fav:
#     print(f"{singer.title()} will be added to the list.")
#--------------------------------------------------------------------------------
'''if Statements'''
'''Simple if statements'''
# age = 25
# if age > 18:
#     print('You are an adult')

'''if-else statements'''
# spot

'''if-elif-else chain'''
# age = 30
# if (age >= 18) and (age <= 25):
#     print('You are an adult')
# elif age < 18:
#     print('You are a kid')
# else:
#     print('You are a man')

'''Using mutliple elif blocks'''
# age = 60
# if (age >= 18) and (age <= 25):
#     print('You are an adult')
# elif age < 18:
#     print('You are a kid')
# elif (age >= 30) and (age <= 50):
#     print('You are in your mids')
# elif (age >= 50) and (age <= 80):
#     print('You are in your old-age')
# else:
#     print('You are a man')

'''Omitting the else block'''
# age = 25
# if (age >= 18) and (age <= 25):
#     print('You are a man')
# elif age < 18:
#     print('You are a kid')
# elif (age >= 30) and (age <= 50):
#     print('You are in your mids')
# elif (age >= 50) and (age <= 80):
#     print('You are in your old-age')

'''Testing mutiple conditions'''
# account = ['username', 'password', 'number']
# if 'username' in account:
#     print('Added username')
# if 'password' in account:
#     print('Added password')
# if 'number' in account:
#     print('Added number')
#--------------------------------------------------------------------------------
'''Using if statements with Lists'''
'''Checking for special items'''
# account = ['username', 'password', 'number']
# for info in account:
#     print(f"Added{info}")
# print("\nCongratulations your account has been created")

# account = ['username', 'password', 'number']
# for info in account:
#     if info == 'username':
#         print(f"Cant add username")
#     else:
#         print(f"Adding {info}")
# print("\nCongratulations your account has been created")

'''Using Multiple lists'''
# account = ['username', 'password', 'number', 'email', 'tfa', 'address']
# mandatory = ['email', 'username', 'password', 'tfa']
# for info in mandatory:
#     if info in account:
#         print(f"Added {info}")
#     else:
#         print(f"Not needed {info}")
# print("\nCongratulations your account has been created")
# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - SIX (DICTIONARIES)'''
# ---------------------------------------------------------------------------------------------------------------
'''A simple Dictionary'''
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#--------------------------------------------------------------------------------
'''Working with Dictionaries'''
'''Accessing values in a dictionary'''
# alien_0 = {'color': 'green', 'points': 5}
# newpoint = alien_0['points']
# print(f"You've scored {newpoint} points!")

'''Adding new value key pairs'''
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['position_x'] = 0
# alien_0['position_y'] = 25
# print(alien_0)

'''Starting with an empty dictionary'''
# alien_0 = {}
# alien_0['position_x'] = 0
# alien_0['position_y'] = 25
# print(alien_0)

'''Modifying values in a dictionary'''
'''SIMPLE EXAMPLE'''
# alien_0 = {'color' : 'green'}
# print(f"The color of the alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The color of the alien is now {alien_0['color']}.")

'''COMPLEX EXAMPLE'''
# alien_0 = {'positionx' : 0, 'positiony' : 25, 'speed' : 'medium'}
# print(f"The original position of the alien is {alien_0['positionx']}.")
# if alien_0['speed'] == 'slow':
#     incrementx = 1
# elif alien_0['speed'] == 'medium':
#     incrementx = 2
# else:
#     incrementx = 3
# alien_0['positionx'] += incrementx
# print(f"New position of the alien is {alien_0['positionx']}.")

'''removing key value pairs'''
# alien_0 = {'positionx' : 0, 'positiony' : 25, 'speed' : 'medium'}
# print(alien_0)
# del alien_0['speed']
# print(alien_0)

'''A dictionary of similar objects'''
# pglang = {
#     'jess' : 'Python',
#     'yogi' : 'Java',
#     'kc' : 'C',
#     'sathwik' : 'JavaScript',
# }
# language = pglang['jess'].title()
# print(f"Jess's fav. language is {language}.")

'''using get() to access values'''
# alien_0 = {'color' : 'green', 'speed' : 'slow'}
# # print(alien_0['points'])
# point_value = alien_0.get('points', 'No point value assigned.')
'''if the second arg is left in the call to get() and 
the key doesnt exist, python will retrun the value None.
The special value None means "no value exists". This is not an error: 
It's a special value meant to indicate the absence of a value)'''
# print(point_value)
#--------------------------------------------------------------------------------
'''Looping through a Dictionary'''
'''looping through all "KEY-VALUE" pairs'''
# user = {
#     'username' : 'jess',
#     'password' : '143qwerty',
#     'number' : 9381288684,
# }
# for key, value in user.items():
#     print(f"\nThe key is {key}.")
#     print(f"The value is {value}.")

'''AND'''

# pglang = {
#     'jess' : 'Python',
#     'yogi' : 'Java',
#     'kc' : 'C',
#     'sathwik' : 'JavaScript',
# }
# for name, lang in pglang.items():
#     print(f"\n{name.title()}'s Fav Lang is {lang.title()}.")

'''looping through all the "KEYS" in a dictionary'''
# pglang = {
#     'jess' : 'Python',
#     'yogi' : 'Java',
#     'kc' : 'C',
#     'sathwik' : 'JavaScript',
# }
# names = ['jess', 'yogi']
# for name in pglang:
#     print(f"Hey! Yo! {name.title()}")

#     if name in names:
#         language = pglang[name].title()
#         print(f"\t{name.title()}, how good are you at {language}")

'''looping through a dictionary's "KEYS" in a particular order'''
# pglang = {
#     'jess' : 'Python',
#     'yogi' : 'Java',
#     'kc' : 'C',
#     'sathwik' : 'JavaScript',
# }
# for name in sorted (pglang):
#     print(f"{name.title()}, Chadukondra rey!.")

'''looping through all "VALUES" in a dictionary'''
# pglang = {
#     'jess' : 'Python',
#     'yogi' : 'Java',
#     'kc' : 'C',
#     'sathwik' : 'JavaScript',
# }
# for language in pglang.values():
#     print(f"{language.title()}")

'''AND'''

# pglang = {
#     'jess' : 'Python',
#     'yogi' : 'Java',
#     'kc' : 'C',
#     'sathwik' : 'JavaScript',
# }
# for language in set(pglang.values()):
#     print(language.title())
#--------------------------------------------------------------------------------
'''Nesting'''
'''A list of Dictionaries'''
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 6}
# alien_2 = {'color' : 'blue', 'points': 7}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

'''game'''
# aliens = []
# for alien in range (30):
#     newalien = {'color': 'green', 'points': 5, 'speed': 'medium'}
#     aliens.append(newalien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
# for alien in aliens[:5]:
#     print(alien)

'''A list in a dictionary'''
'''EXAMPLE - 1'''
# pizza = {
#     'crust' : 'thick',
#     'toppings' : ['mushroom', 'pepper'],
# }
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings - ")
# for toppings in pizza['toppings']:
#     print(f"\t{toppings}")

'''EXAMPLE - 2'''

# pglang = {
#     'jess' : ['python', 'java'],
#     'yogi' : ['c'],
#     'suhas' : ['rust', 'go'],
#     'rohan' : ['python', 'powerbi'],
# }
# for name, language in pglang.items():
#     print(f"\n{name.title()}'s knows these languages:")
#     for lang in language:
#         print(f"\t{lang.title()}")

'''A dictionary in a dictionary'''
# users = {
#     'jss' : {
#         'fname' : 'jess',
#         'username' : 'jeshwanthshivasai',
#         'location' : 'hyderabad'
#     },
#     'yogi' : {
#         'fname' : 'yogitha',
#         'username' : 'chyogitha',
#         'location' : 'finland',
#     },
# }
# for user, info in users.items():
#     print(f"\nUsername : {user}")
#     fullname = f"{info['fname']} {info['username']}"
#     location = info['location']

#     print(f"\tFullname : {fullname.title()}")
#     print(f"\tLocation : {location.title()}")
# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - SEVEN (USER INPUT AND WHILE LOOPS)'''
# ---------------------------------------------------------------------------------------------------------------
'''how the input() Function works'''
# message = input("whom are you telling hello?")
# print(message)

'''writing clear prompts'''
# message = "vadiki peru rayamani chepu"
# message += "\nninne ra rey peru rayamai cheptunaru"
# name = input(message)
# print(f"\nHello, {name.title()}")

'''using int() to accept numerical input'''
# age = input("age please? :")
# age = int(age)
# print(age >= 18)

'''AND'''

# age = input("age please? :")
# age = int(age)

# if age >= 18:
#     print("\nYou are old enough to vote.")
# else:
#     print("\nGotta become an elder kid.")
#--------------------------------------------------------------------------------
'''The Modulo Operator'''
# number = input("number kottu nuvu, i'll tell you whether its even or odd.")
# number = int(number)

# if number%2  == 0:
#     print("\nThe number is even")
# else:
#     print("\nThe number is odd")
#--------------------------------------------------------------------------------
'''Introducing While Loops'''
'''The while loop in action'''
# currentnum = 0
# while currentnum <= 5:
#     print(currentnum)
#     currentnum 
# += 1

'''Using break to exit a loop'''
# currentnum = 0
# while currentnum < 10:
#     currentnum += 1
#     if currentnum % 2 == 0:
#         break
#     print(currentnum)
    
'''Using continue in a loop'''
# currentnum = 0
# while currentnum < 10:
#     currentnum += 1
#     if currentnum % 2 == 0:
#         continue
#     print(currentnum)

'''Avoiding Infinite Loops'''
'''AND FOR INFINITE LOOP REMOVE LAST LINE'''
# x = 1
# while x < 10:
#     print(x)
#     x += 1
#--------------------------------------------------------------------------------
'''Using a while loop with lists and dictionaries'''
'''Moving items from one list to another'''
# unconfirmed_users = ['john', 'jacob', 'james']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
# print("\nThe following users are confirmed.")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

'''Removing all instances of specific values from a list'''
# pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

'''Filling a dictionary with user input'''
# responses = {}
# active = True
# while active:
#     name = input("\nWhat's your name?")
#     response = input("Whats your fav car?")
#     responses[name] = response
#     repeat = input("An another response? (Yes/No)")
#     if repeat == 'No':
#         active = False
# print("\n---Poll Results---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to buy a {response}")
# ---------------------------------------------------------------------------------------------------------------
'''CHAPTER - EIGHT (USER INPUT AND WHILE LOOPS)'''
# ---------------------------------------------------------------------------------------------------------------
