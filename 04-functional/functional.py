#  clean consistent maintainable code. does not change data outside the scope

# coffees = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano', 'Decaf']

# def reverse(str):
#     return str[::-1]

# reversed_coffees = map(reverse, coffees)

# for x in reversed_coffees:
#     print(x)
# def greeting():
#     print("Hello Friend!")

# greeting()

# def greeting2(name):
#     print("Hello, " + name)

# greeting2("Mesi")

# def greeting2(name, age):
#     # print("Hello, " + name + ", you are "+ age + '!')
#     print(f"Hello {name}, you are {age}!")

# greeting2("Mesi", "32")

# def greeting(name,age="28"):
# def greeting(name,age=28):
#     print("Hello " + name + ", you are " + str(age) + "!")
#     print(f"Hello {name}, you are {age}!")

# name = input("Enter your name: ")    
# greeting(name,32)
# greeting("Judith")

# def greeting(name, age=28, color = 'red'):
#     #Greets user with 'name' from 'input box' and 'age' next year, if available, default age is used
#     # also includes favorite color
#     print('Hello '  +  name.capitalize() + ', you will be ' + str(age+1) +' next birthday!')
#     print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
#     print(f'We hear you like the color {color.lower()}!')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# color = input('Enter favorite color: ')
# greeting(name, int(age), color)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

# def greeting(name, age=28, color="red"):
#  #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
#    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
#    print(f"We hear you like the color {color.lower()}!")

# greeting("brian", 27,"Blue")
# greeting(age=27, name="brian",color="Blue")

# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     # return amount, tax, total_amount
#     # return [amount, tax, total_amount]
#     # return {amount, tax, total_amount}
#     return f"{amount}, {tax}, {total_amount}"
    
# price = value_added_tax(100)    
# print(price, type(price))
# # print(price[1], type(price))
# print(price, type(price))
