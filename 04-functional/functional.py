#  clean consistent maintainable code. does not change data outside the scope

coffees = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano', 'Decaf']

def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    print(x)
