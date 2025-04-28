import random
from Hangman_Data import r

life_man=["You have left 4 life","you have left 3 life","you have left 2 life","you have left 1 life","you have left 0 life","holy grab"]
Our_List=["Apple","banana","jackfruit","mango","pineapple"]
lives=6
chosen_word=random.choice(M.r)
print(chosen_word)

placeholder=""
word_length=len(chosen_word)
for K in range(word_length):
    placeholder+="_"
print(placeholder)
game_over=False
st_letter=[]
while not game_over:
    guess=input("guess a letter:").lower()
    display=""
    for i in chosen_word:
        if i==guess:
            display+=guess
            st_letter.append(guess)
        elif i in st_letter:
            display+=i
        else:
            display+="_"
    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose")
    if "_" not in display:
        game_over=True
        print("You Win")



