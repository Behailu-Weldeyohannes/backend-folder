#  List

list1 = [1,2,3,4,5]

print(list1[1])
list2 = ["A", "B", "C"]
list3 = ["Hello", 1, True, 20.40]

list4 = [1, [2,3,4], 5, 6]

print(*list1)
print(list1, sep = " ,")

list1.insert(len(list1), 0)
list1.append(7)

list1.extend([6,7,8,9])
print(list1, sep = ",")

list1.pop(4)
del list1[0]
print(list1, sep = ",")

#  iterate

for x in list1:
    print("Value: ", x)