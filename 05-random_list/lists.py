# states=  ["Delaware", "Texas", "Virginia", "Maryland", "N Carolina"]

# print(states[2])
# print(states[-2])

# states[0] = "S Carolina"

# states.append("Washington DC")
# states.extend(["Behailu", "Kenya"])

# print(states)



# # print(msg[2:3])
# print(msg[:3])
# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
# print(msg1.title())
# print(msg1[::-1].title())

#  Multiple  line 

# msg="""Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3"""
# print(msg)

# msg='Welcome to Python 101: Strings'
# print(msg.replace('Python','C'))

# msg='Welcome to Python 101: Strings'
# print('Python' not in msg)

# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

# name = input('What is your name?: ')
# age = input('What is your age?: ')
# print('Hello ' + name + 'You are '+ age + 'years old')
# calculator
# num1 = input('Enter a digit: ')
# num2 = input('Enter a second number: ')
# answer = float(num1) + float(num2)
# print(answer)
# name = input('Enter your name: ')
# distance_km = input('Enter distance in km: ')
# distance_mi = float(distance_km)/1.609
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911,130,328,535,740,308]
# print(friends)
# print(friends[3])
# print(friends[-1])
# print(friends[2:4])
# print(friends[:4])
# print(friends[:])
# print(len(friends))
# print(friends.index('Eric'))
# print(friends.count('Eric'))
# print(friends)
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)
# print(max(friends))
# print(min(cars))
# print(max(cars))
# print(sum(cars))

# friends.append('TerryG')
# print(friends)
# friends.insert(1,'TerryG')
# print(friends)

# friends[2]='Behailu'
# print(friends)
# friends.extend(cars)
# print(friends)

# friends.remove('Terry')
# friends.pop()
# friends.pop(2)
# friends.pop(-1)
# friends.clear()
# del friends
# del friends[2]
# print(friends)

# new_friends = friends[:]
# new_friends2 = friends.copy()
# new_friends3 = list(friends)
# print(new_friends)
# print(friends)
# print(new_friends3)
# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# new_day = input('Enter # of lemondaes for new day: ')
# sales_w2.append(int(new_day))
# # sales.extend(sales_w1)
# # sales.extend(sales_w2)

# sales = sales_w1 + sales_w2
# # sales.sort()
# # worst_day_prof = sales[0] * 1.5
# # best_day_prof = sales[-1] * 1.5
# worst_day_prof = min(sales) * 1.5
# best_day_prof = max(sales) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

#  **************Split and Join **********

# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split())
# print(msg.split(' '))
# print(msg.split(' '), type(msg.split(' ')))
# print(csv.split(' '))
# print(str(friends_list))
# print('-'.join(friends_list))

# print(''.join(msg.split()))
# print(msg.replace('', ''))
# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# # print(csv.split(','))
# # print(','.join(csv.split(',')))
# # print(','.join(csv.split(',')).split(':'))
# # print(','.join(','.join(csv.split(';')).split(':')))
# # print((','.join(','.join(csv.split(';')).split(':'))).split(','))
# # friends_list = ['Exercise: fill me with names']
# friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
# print(friends_list)
# print('replaced', csv.replace(';', ',').replace(':', ',').split(','))
# print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

#Tuples - faster Lists you can't change
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')

# print(friends)
# print(friends_tuple)
# print(friends[2:4])
# print(friends_tuple[2:4])

# ************** set **************
#Sets - blazingly fast unordered Lists 
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric', 'Eric'}
# # print(friends)
# # print(friends_tuple)
# # print(friends_set)
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# print(friends_set.intersection(my_friends_set))
# print(friends_set.difference(my_friends_set))
# print(friends_set.union(my_friends_set))

#Sets - blazingly fast unordered Lists 
#empty Lists
# empty_list = []
# empyt_list = list()

# #empty Tuple
# empty_tuple = ()
# empty_tuple = tuple()

# #empty Set
# empty_set = {} # this is wrong, this is a dictionary
# empty_set = set()

#Sets - Exercise

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']
#1. Check if ‘Eric’ and ‘John’ exist in friends
# print('Eric' in friends)
# print('Eric' in friends and 'John' in friends)
#2. combine or add the two sets 
# print(friends.union(my_friends))
# print(friends | my_friends)
# #3. Find names that are in both sets
# print(friends & my_friends)
#4. find names that are only in friends
# print(friends.difference(my_friends))
# print(my_friends - friends)
# print(friends - (my_friends))
# print(my_friends.difference(friends))

#5. Show only the names who only appear in one of the lists
# print(my_friends.symmetric_difference(friends))
# print(my_friends ^ friends)
#6. Create a new cars-list without duplicates

# cars_no_dupl = set(cars)
# print(cars_no_dupl)
# cars_no_dupl =list(set(cars))
# print(cars_no_dupl)

# Comments
print("#comments")

