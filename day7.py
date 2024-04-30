word_list = ["arvar","baboon","camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)
print(f"the solution is {chosen_word}")
display = []
for n in range(len(chosen_word)):
    display += "_"
print(display)
endofgame = False
while not endofgame:
    guess = input("guess the word").lower()
    for posi in range(len(chosen_word)):
        letter=chosen_word[posi]
        if letter == guess:
            display[posi]=letter
    print(display)
    if "_" not in display:
       endofgame = True
       print('win')
