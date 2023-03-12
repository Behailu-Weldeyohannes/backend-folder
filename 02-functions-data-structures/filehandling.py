# file = open('test.txt', mode = 'r')

# data = file.readline()
# print(data)

# file.close()


# with open('test.txt', mode = 'r') as file:
#     data = file.readline()
# print(data)

# file.close()


# creating file

# with open('newfile.txt', mode='w') as file:
#     file.write("This is a new file created!")

# add multiple lines

# with open('newfile.txt', mode='w') as file:
#     file.writelines(["This is a new file created!", "This is another line", "\n New line"])
try:
    with open('sample/newfile.txt', mode='w') as file:
        file.writelines(["\n This is a new file created!2", "This is another line", "\n New line"])
except FileNotFoundError as e:
    print("ERROR", e)
