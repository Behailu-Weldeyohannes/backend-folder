# data is collected in the prefered format
# numeric (integer, float, complex number)
# sequence (string, list, tuples)
# dictionary
# boolean
# set

# a = 10

# print(type(a))

# b = 2.3

# print(type(b))

# d = [1,2,3,4]
# print(type(d))

# string
# a = "Hello"
# b = "there"
# print(a +" "+ b)
# name = "John"
# print(name[0])
# print(len(name))

# Type casting (converting data types) It can be implicit or explicit

# str(11)
# print(str(11))
# int(20.5)
# print(int(20.5))
# float(50)
# print(50)
# ord()
# hex()
# oct()
# tuple()
# set()
# list()
# dict()

# user input, console output : for example object, sep, end, file, flush

# print('Hello', 'you!', sep= ', ')

# num1 = input("Please enter the first number")
# num2 = input("Please enter a second number")

# print(num1, num2)
# # print(int(num1) + (num2))


# sort() sorted()

# my_list = [1,5,3,7,2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_string = 'python'
# print(my_list,'original')
# print(sorted(my_list))
# print(my_list,'new')

# my_list = [1,5,3,7,2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_string = 'python'
# print(my_string,'original')
# print(sorted(my_string))
# print(my_string,'new')

# my_list = [1,5,3,7,2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_string = 'python'
# print(my_dict,'original')
# print(sorted(my_dict))
# print(my_dict,'new')

# my_list = [1,5,3,7,2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_string = 'python'
# print(my_dict,'original')
# print(sorted(my_dict.items()))
# print(my_dict,'new')

# my_list = [1,5,3,7,2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_string = 'python'
# print(my_list,'original')
# print(reversed(my_list))
# print(my_list,'new')

# my_list = [1,5,-3,7,-2]
# my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
# print(sorted(my_llist, key = lambda item :item[1]))

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

# print(movie)
# print(movie['title'])
# print(movie.get('budget'))
# print(movie.get('budget', 'not found'))
# movie['title'] = 'The Holy Grail'
# print(movie.get('title'))
# movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
# movie['budget'] = 25000
# print(movie.get('budget'))
# del movie['year']
# year = movie.pop('year')
# print(movie)
# print(year)

# print(len(movie))
# print(movie.keys())
# print(movie.values())
# print(movie.items())

# for key in movie:
#     print(key)

# for key, value  in movie.items():
#     print(key, value)
# python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
# holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
# life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}
# #membership test
# print('Arthur' in holy_grail)
# if 'Arthur' not in python:
#     print('He\'s not here!')

# people = {}
# people1 = {}
# people2 = {}
# #method 1 update
# people.update(python)
# people.update(holy_grail)
# people.update(life_of_brian)
# print(sorted(people))
# print(sorted(people.items()))
# #method 2 comprehension
# for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
# # print(sorted(people1))
# print(sorted(people1.items()))
# #method 3 unpacking 3.5 later
# people2 = {**python,**holy_grail,**life_of_brian}
# # print(sorted(people2))
# print(sorted(people2.items()))
# print('**********')
# print('The sum of the ages: ', sum(people.values()))

#create stores
#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
# freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
# antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
# pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

# #create an dempty shopping cart
# cart = {}
# #loop through stores/dicts
# for shop in (freelancers,antiques,pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     buy_items = ", ".join(list(cart.keys()))
# print(f'You Purchased {buy_items}. Today it is all free. Have a nice day of mayhem!')

#create stores
# freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
# antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
# pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
# #morning inventory
# department_store = {}
# for department in (freelancers, antiques, pet_shop) :department_store.update(department)
# department_store.pop('name')
# print('Morning inventory of stores', sorted(department_store.items()))
# print('-----------------')
# #create an dempty shopping cart
# cart = {}
# #create purse with 100Gp
# purse = 1000
# buy_items1 = ''
# #loop through stores/dicts
# for shop in (freelancers,antiques,pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
#     #exit on exit typed or buying nonexistant item
#     if buy_item == 'exit':
#         continue
#     if buy_item not in shop:
#         continue
#     #update string
#     buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '    
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     buy_items = ", ".join(list(cart.keys()))
#     total_sum = sum(cart.values())
# print(f'You Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
# print(f'You Purchased {buy_items1}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
# #evening inventory
# department_store_after = {**freelancers, **antiques, **pet_shop} #pyth 3.5
# department_store_after.pop('name')
# print('-----------------')
# print('Evening inventory of stores', sorted(department_store_after.items()))