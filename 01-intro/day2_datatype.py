
# Data type

# print("Hello"[0])

# print("123" + "456")  # concatenates 
# int
# 123
# float

# 10.5

# Boolean

# True
# False

# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

# function

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has" + new_num_char + "characters.")

# print(type(num_char))

# a = str(123)
# print(type(a))
# print(70 + float("100.5"))

# two_digit_number = input("Type a two digit number")
# print(type(two_digit_number))


# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# print(first_digit)
# print(second_digit)

# result = int(first_digit) + int(second_digit)

# print(int(result))
# Mathematical operations

# 3 + 5

# 7 - 5

# 3 * 2

# print(type(6/3))
# print(2 ** 3)
# PEMDAS LR order of priority goes from left to right

# Parentheses ()
# Exponents **
# Multiplication * / Division
# Addition + - Subtraction


# print(3 * 3 + 3 / 3-3)  # 7
# print(3 * (3 + 3 / 3-3)) # 3
# BMI
# height = input ("enter your height: ")
# weight = input("enter your weight: ")

# bmi =  float(weight) / float (height) ** 2
# bmi_as_int = int(bmi)
# print(bmi)

# print (round(8/3))
# print (round(8 // 3))
# print (round(8/3, 2))

#  User scores a point
# score = 0
# score = score + 1
# score += 1
# score -= 1
# score *= 1
# score /= 1

# print(score)
# f-string
# score = 0
# height = 1.8
# isWinning = True

# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# age = input("What is your current age?")

# age_as_int = int(age)

# years_remaining = 100 - age_as_int

# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# print(months_remaining)

# message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

# # print(message)

# tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# bill_with_tip = tip / 100 * bill + bill
tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
