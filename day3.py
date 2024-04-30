# print("welcome to rollercoaster")
# height = int(input("enter your height"))
#
# if height >= 100:
#     print("you can")
#
#     age=int(input("enter age"))
#     if age<=18:
#         print("pay17")
#     else:
#         print("pay7")
# else:
#     print("wou cant")
#
#



# num = int(input("enter the no to check even or odd"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")
# # nested if else

# bmi cali
# height = float(input('enter the height'))
# weight = float(input("enter the weight"))
# bmi = weight/(height*height)
# if bmi<=18.5:
#     print(f"your bmi is {bmi}under weight")
# elif bmi>18.5 & bmi<25:
#     print(f"your bmi is {bmi}normal weight")
# elif bmi>25 & bmi<30:
#     print(f"your bmi is {bmi}over weight")
# elif bmi>35:
#     print(f"your bmi is {bmi}clinically obese")

# leap year
year = int(input('enter yeear'))
if year%4 ==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")

# multiple if
print("welcome")
height1=int(input("enter height"))
if height1>120:
    print("can ride")
    age = int(input("enter age"))
    if age<12:
        bill=5
        print("pay 5")
    elif age>18:
        bill=10
        print("pay 10")
    else:
        bill=7
        print("pay7")
        wantphotos=str(input("want photos? Y or  N ."))
        if wantphotos=="Y":
            bill+=3
            print(f"your bill is{bill} ")
        else:
            print(f"your bill is {bill}")
else:
    print("you cant")

# TREASURE ISLAND
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")



choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


