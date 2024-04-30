from random import randint

hard_level=5
easy_level=10
def check_ans(guess, answer ,turn):
    if guess>answer:
        print("too high")
        return turn - 1
    elif guess<answer:
        print("too low")
        return turn - 1
    else:
        print(f"you got the ans the ans was{answer}")

def set_difficulty():
    level = input("choose level easy or hard")
    if level=="easy":
            return easy_level
    else:
            return hard_level
def game():
    print("welcome to guessing game")
    print("i am thinking number from one to 100 try to guess")
    answer = randint(1,100)
    print(f"the correct ans is {answer}")
    turn = set_difficulty()

    guess=0
    while guess!=answer:
        print(f"you have {turn}attempts remaining")
        guess=int(input("make a guess"))
        turn = check_ans(guess,answer,turn)
        if turn==0:
            print("you loose")
        elif guess!=answer:
            print("guess again")
game()