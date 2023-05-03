# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

# while condition:
#     code
#     iterator
# Three Loop Questions:
# 1. What do I want to repeat?
#  -> 
# 2. What do I want to change each time?
#  -> 
# 3. How long should we repeat?
#  -> 

# i = 0
# while i <  5:
#     print(f"Loops are awesome")
#     i = i + 1

# i=0
# while i < 5:
#     i+=1
#     print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)

# print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> guess number and number of guesses
#3. How long should we repeat?
#  -> until user loses, runs out of guesses, or wins

# guess game

# num = 76
# guess = 0
# guess_limit=5
# guess_number = 0
# guess = int(input(f'Guess a number 1-100: '))
# guess_number +=1
# while guess_number < guess_limit:
    
#     if guess != num:
#         guess_number +=1
#         if guess > num:
#             guess = int(input(f'{guess} Too high - Guess again 1-100: '))
#         else:
#             guess = int(input(f'{guess} too low - Guess again 1-100: '))
#     if guess == num:
#         print(f'You Win! You Guessed it: {guess}')
#         break
    
# if guess != num:
#     print(f'Sorry you lose! It was {num}')

# For Loops
# print("For Loops")
# print("For Loops")


# for furgle in 'Norwegian blue':
#     print(furgle)

# print("For Loop done!")

# for furgle in range(8):
# for furgle in range(2,8):
# for furgle in range(1,15,3):
#     print(furgle)
# print("For Loop done!")

# for name in ['John','Terry','Eric','Michael','George']:
#     print(name)

# print("For Loop done!")

# friends = ['John','Terry','Eric','Michael','George']
# for friend in friends:
#     print(friend)

# print("For Loop done!")

# friends = ['John','Terry','Eric','Michael','George']
# for index in range(len(friends)):
#    print(friends[index])

# print("For Loop done!")

# friends = ['John','Terry','Eric','Michael','George']
# for friend in friends:
#     if friend == 'Eric':
#         print('Found ' + friend + '!')
#         # break
#         continue
#     print(friend)

# print("For Loop done!")

# friends = ['John','Terry','Eric']
# for friend in friends:
#     for number in [1,2,3]:
#         print(friend, number)

# print("For Loop done!")

#  *** Excercise

# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']
# msg = 'You are invited to the party on saturday.'
# names.extend(names1)
# #names = names + names1
# for index in range(2):
#     names.append(input('Enter a new name: '))

# for name in names:
#     msg1 = f'{name.title()}! {msg}'
#     print(msg1)

# *********** Enumuerate this *********************

# print('python101 - Enumerate')
# friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
# i = 1
# for friend in friends:
#     print(i, friend)
#     i = i +1 # += 1
#     print('**************')
#     for num, friend in enumerate(friends, 1):
#         print(num, friend)

# print('python101 - Enumerate')
# friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
# efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]

#i = 51
#for friend in friends:
#    print(i, friend)
#    i = i +1 # += 1
# for num, friend in enumerate(friends,51):
#     print(num, friend)
# for friend in enumerate(friends,51):
#     print(friend)
# for friend in enumerate(enumerate(friends,51),-100):
#     print(friend)   
# for num, letter in enumerate('python',start = 5):
#     print(num, letter)
# print(type(enumerate(friends)))
# print(list(enumerate(friends)))