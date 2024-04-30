# fruits =["apple","orange","grapes"]
# for i in fruits:
#     print(i +"pie")
# print(fruits)

# range
# a =input().split()
# total = 0
# for n in range(1,101):
#     total += n
# print(total)


# studenth = input().split()
# for n in range(0,len(studenth)):
#     studenth[n] =int(studenth[n])
# totalh=0
# for height in studenth:
#     totalh += height
# print(f"total height= {totalh}")
# noofstudent=0
# for student in studenth:
#     noofstudent += 1
# print(f"no of student={noofstudent}")
# avgh= round(totalh/noofstudent)
# print(f"avg h={avgh}")

# max score
# studscore = input().split()
# for n in range(0,len(studscore)):
#     studscore[n]= int(studscore[n])
# print(studscore)
# highscore = 0
# for score in studscore:
#     if score > highscore:
#         highscore=score
# print(f"high score is {highscore}")



# target = int(input())
# evensum=0
# for n in range(2,target+1,2):
#     evensum += n
# print(evensum)

# fizz buzz
target= (100)
for number in range(1,target+1):
    if number % 3==0 and number % 5 == 0:
        print("bizzbuzz")
    elif number %3==0:
        print("fzz")
    elif number %5 ==0:
        print("buzz")
    else:
        print(number)
# password genrator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")


