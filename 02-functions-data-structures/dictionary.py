#  faster and more flexible than lists no duplication

# sample_dict = {1: 'Coffee', 2: 'Tea', 3: "Juice"}
# print(sample_dict[1])


# sample_dict[2] = "Mint Tea"

# print(sample_dict[2])

# del sample_dict[3]

# print(sample_dict)

my_d = {1: 'Test', 'Name': 'Jim'}

print(type(my_d))
print(my_d)
print(my_d[1])
print(my_d['Name'])

my_d[2] = "Test2"
my_d[2] = "Not a test"

print(my_d)

del my_d[1]
print(my_d)

# for x in my_d:
#     print(x)

for key, value in my_d.items():
    print(str(key) + " : " + value)