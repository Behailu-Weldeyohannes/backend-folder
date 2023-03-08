
# for i in range(10):
#     print("Looping..", i)

# favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

# for item in favorites:
#     print("I like this desert", item)
# for idx, item in enumerate(favorites):
#     print(idx, item)

# count = 0
# while count < len(favorites):
#     print('I like this desert', favorites[count])
#     count +=1

# nested loops

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8,9]

# count = 0
# # outer loop
# for x in list1:
#     count +=1
#     # inner loop
#     for y in list2:
#         count += 1
# print(count)


# for i in range(2):
#     for j in range(10):
#         print(0, end = " ")
#     print()

import time
start_time = time.time()

for i in range(200):
    for j in range(200):
        print(0, end = " ")
    print()

print(round((time.time() - start_time), 2))