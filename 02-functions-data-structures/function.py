# bill = 175.00

# tax_rate = 15

# total_tax = (bill * tax_rate) / 100.00

# print('Total tax', total_tax)

# def calculate_tax(bill, tax_rate):
#     return round((bill * tax_rate) / 100.00)

# print('Total tax: ',calculate_tax(175.00, 15))
# print('Total tax: ',calculate_tax(275.00, 22))

# variable scope four types: local, global, enclosing, built-in

# global

# my_global = 10

# def fn1():
#     local_v = 5
#     print('Access to Global', my_global)
# fn1()

# # local

# print("Can't access local", local_v)
# my_global = 10
# def fn1():
#     enclosed_v = 8
#     def fn2():
#         local_v = 5
#         print('Access to Global', my_global)
#         print('Access to enclosed', enclosed_v)
#     fn2()

# fn1()

#  List

