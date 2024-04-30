# def greet():
#     print("goodafternoon")
#     print("goodnight")
#     print("good morning")
# greet()
# fun that allow input
#
# def greetname(name):
#     print(f"hello {name}")
#     print(f"how do you do {name}")
# greetname("manas")

# def greetwith(name="manas",loction="pen"):
#     print(f"hello {name} i am from {loction}")
# # greetwith("manas","pen")
# greetwith()
import math
# def paintwall(height,weidth,cover):
#     num_can =(height*weidth)/cover
#     roundup_can =math.ceil(num_can)
#     print(f"you will nee {num_can}cans of paint")
# testh=int(input())
# teshv=int(input())
# coverage=5
# paintwall(height=testh,weidth=teshv,cover=coverage)

def prime (number):
    isprime = True
    for i in range(2,number):
        if number % i ==0:
            isprime == False
    if isprime:
        print("it is prime ")
    else:
         print("it is not prime")
n =int(input("enter no"))
prime(number=n)
# print(prime())

# caesar_cipher
