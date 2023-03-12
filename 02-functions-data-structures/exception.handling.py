
def divide_by(a, b):
    return a / b
print(divide_by(40, 4))


def divide_by2(c, d):
    return c / d


try:
    ans = divide_by2(40, 0)
except:
    print("Some thing went wrong!")

try:
    ans2 = divide_by2(50, 0)
except Exception as e:
    print("Some thing went wrong!", e)
    print(e.__class__)

try:
    ans3 = divide_by2(60, 0)
except ZeroDivisionError as e:
    print(e, "We cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")
   