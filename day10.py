# a=int(input())
# b=int(input())
# def add():
#     return a*b
# add()
# print(add())

# def format_name(f_name,l_name):
#     a=f_name.title()
#     b=l_name.title()
#     return (f"{a}{b}")
# c=format_name("manas","gaikwad")
# print(c)
# print(len(c))


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year")
#             else:
#                 print("Not leap year")
#         else:
#             print("Leap year")
#     else:
#         print("Not leap year")
#
#
# # TODO: Add more code here 👇
# def days_in_month(year,month):
#     """please enter year first and the enter the date """
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
#
#  # 🚨 Do NOT change any of the code below
# year = int(input())  # Enter a year
# month = int(input())  # Enter a month
# days = days_in_month(year, month)
# print(days)
# # days_in_month(2021,2)
# """hello i am docstring"""
# days_in_month()

# calculator
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

op={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
num1= int(input("first no"))
num2= int(input("seconf no"))
for symbol in op:
    print(symbol)
opsym=input("pick op")
calculation = op[opsym]
answer=calculation(num1,num2)

print(f"{num1} {opsym} {num2}={answer}")