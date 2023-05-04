# print(' Lambda Functions')
# def square(x):
#     return x*x
# square1 = lambda x: x*x
# def square2(x):return x*x
# print(square1(3))

# def square(x):
#     return x*x
# #name = lambda parameter(s): expression
# double_mult = lambda x,y: 2*x*y

# # print(double_mult(2,3))


# def name_and_alias(name,alias):
#     return name.strip().title() + ':' + alias.strip().title()
# name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()
# def name_and_alias2(name,alias):return name.strip().title() + ':' + alias.strip().title()

# print(name_and_alias2(' john  ClEEse  ','HECKLER'))
# print(name_and_alias(' john  ClEEse  ','HECKLER'))

# monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
# monty_python.sort(key = lambda name:name.split(' ')) # order by first name
# monty_python.sort(key = lambda name:name.split(' ')[-1]) # order by last name
# print(monty_python)

# monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
# def sort_names(name):
#     return name.split(' ')
# monty_python.sort(key = lambda name:name.split(' ')[-1])
# print(monty_python)
# monty_python.sort(key= sort_names)
# print(monty_python)

# def func(n):
#     return lambda a: a*n
# # a*2
# doubler = func(2)
# print(doubler(3))
# quintipler = func(5)
# print(quintipler(3))
# print(type(func(3)))


# def price_calc(start,hourly_rate):
#     return lambda hours: start + hourly_rate * hours
    
# walkin_cost = price_calc(10,30)
# premium_cost = price_calc(1,25)
# print(walkin_cost(2))
# print(premium_cost(2))
# print(price_calc(1,25)(2))

# print((lambda a,b,c: a+b+c)(2,3,4))
# print((lambda a,b,c=2: a+b+c)(2,3,4))
# print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))
# print((lambda *args: sum(args))(2,3,4,50))


# print('Lambdas Exercise')

# def join_list_no_duplicates(list_a,list_b):
#    return list(set(list_a + list_b))
# list_a = [1,2,3,4]
# list_b = [3,4,5,6,7]
# #write lambda below 

# print(join_list_no_duplicates(list_a,list_b))
# print('***********************')
# join_list_no_duplicates1 = lambda list_a,list_b:list(set(list_a + list_b))
# print(join_list_no_duplicates(list_a,list_b))

# signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# print(sorted(signups)) # Lexicographic sort
# #write sorting by integer
# print(sorted(signups,key = lambda id:int(id[3:]))) # Integer sort