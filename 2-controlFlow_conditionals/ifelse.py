
# water_level = 90
# if water_level > 80:
#     print("Drain water")
# else: 
#     print("Continue")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#  Modulo operation

# 7 % 2
# number = int(input("Which number do you want check?"))
# if number % 2 == 0:
#     print("This is a even number.")
# else:
#     print("This is an odd number.")

# nested if / else

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age <= 18:
#         print("Pleae pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#  if / elif / else


# age = int(input("What is your age?"))
# if age <= 12:
#     print("Pleae pay $5.")
# elif age <= 18:
#     print("Please pay $7.")
# else:
#     print("Please pay $12.")

# BMI

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / height ** 2)

# if bmi <= 18.5:
#     print ( f"Your bmi is {bmi}, you're underweight")
# elif bmi < 25:
#     print(f" Your bmi is {bmi}, you have a normal weight.")
# elif bmi  < 30:
#     print(f" Your bmi is {bmi}, you'reYou're overweight")
# elif bmi  <= 35:
#     print(f" Your bmi is {bmi}, you're obese")
# else:
#     print("You're clinically obese.")

#  a leap year

# year = int(input("Which year do you want to check?"))
# leap = "Leap year"
# noLeap = "Not a leap year"

# if year % 4 == 0:
#     print(f"{year} , is divisible by 4 so it is {leap}")
# elif year % 100 == 0:
#     print(f"{year} is divisible by 100, so it is a {leap}.")
# elif year % 400 == 0:
#     print(f"{year} is divisible by 400, so it's a {leap}")
# else:
#     print(f"{year} is {noLeap}")

# or

# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not Leap year")

# ******************  multiple if statement in succession ****************

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age <= 12:
#         bill = 5
#         print("Child ticket are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Please pay $12.")
#     wants_photo = input("Do you want a photo taken? Y or No. ")
#     if wants_photo == "Y":
#         # bill = bill + 3
#         bill += 3
#     print(f"Your final bill is {bill}")


# else:
#     print("Sorry, you have to grow taller before you can ride.")

# ********************** Pizza Order Practice ***************

# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheeze = input("Do you want extra cheeze? Y or N ")
# bill = 0



# if size == "S":
#     bill += 15 
# elif size == "M":
#     bill += 20 
# elif size == "L":
#     bill += 25 

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheeze == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")


# **************** Logical Operations ******************



# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age <= 12:
#         bill = 5
#         print("Child ticket are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")

#     else:
#         bill = 12
#         print("Please pay $12.")
#     wants_photo = input("Do you want a photo taken? Y or No. ")
#     if wants_photo == "Y":
#         # bill = bill + 3
#         bill += 3
#     print(f"Your final bill is {bill}")


# else:
#     print("Sorry, you have to grow taller before you can ride.")

#  *************************Love calculator ****************
# https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love


# lowercase = "Behailu".lower()
# lowercase.count("b")
# print(lowercase)


# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true =  t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love =  l + o + v + e

# love_score =  int(str(true) + str(love))
# print(love_score)

# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, yo go together like coke and mentos.")
# elif(love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")


