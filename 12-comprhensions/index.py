# numbers = [1,2,3,4,5,6,7,8,9]

# new_list = []
# for num in numbers:
#     new_list.append(num * num)

# print(new_list)

# new_list = [num*num for num in numbers]
# print(new_list)

# new_list = [num for num in numbers if num % 2 == 0]
# print(new_list)
# new_list = [num for num in numbers if num % 2 == 1]
# print(new_list)
# new_list = [num for num in numbers if num % 2 != 0]
# print(new_list)

# new_list = filter(lambda num: num % 2 == 0, numbers)
# print(list(new_list))

# new_list = []
# for letter in 'spam':
#    for num in range(4):
#        new_list.append((letter,num))
# print(new_list)

# new_list = [(letter, num) for letter in 'spam' for num in range(4)]

# print(new_list)

# Dictionary comprehensions
# movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
# "Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
# year =[1971,1975,1979,1982,1983,2014]
# names = ['John','Eric','Michael','Graham','Terry','TerryG']

# print(list(zip(movies, year)))

# # give me a dict('movies': year) for each movies, year in zip(movies, year)
# new_dict = dict()
# for movie, yr in zip(movies,year):
#     new_dict[movie] = yr
# print(new_dict)

# new_dict = {movie:yr for movie, yr in zip(movies, year)}
# print(new_dict)
# print("*******")
# new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983}
# print(new_dict)

# new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
# print(new_dict)
# n1 =[(name,movie,yr) for name,movie,yr in zip(names,movies,year) if yr < 1981]
# print(n1)

# n1 =[[name + "s favorite movie was" + movie + " from " + str(yr)] for name,movie,yr in zip(names,movies,year) if yr < 1981 ]
# print(n1)