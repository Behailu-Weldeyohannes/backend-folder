#  imutable not support item 
my_tuple = (1, "strings", 4.5, True)
my_tuple2 = 2, "strings", 4.5, False

print(my_tuple[1])
print(my_tuple2[1])
print(type(my_tuple))
print(type(my_tuple2))

print(my_tuple.count('strings'))
print(my_tuple.index(4.5))

for x in my_tuple:
    print(x)

  