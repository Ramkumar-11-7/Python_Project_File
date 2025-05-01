import random
from Number_File import L_1
from hangman_art import stages,logo
choose_Word=random.choice(L_1)
print(choose_Word)
print(f"your are welcome {logo} this game")
print("Hi I am Ramkumar founder of this Game")

under_score=""
length=len(choose_Word)
for u in range(length):
    under_score+="_"
print(under_score)
print(f"your finding number total number length is {length} ")

Game_over=False
pre_word=[]
lives = 6
print(f"you have only  {lives} lives so play well")



while not Game_over:

    guess = input("Enter a your number")
    display = ""
    if guess in pre_word:
        print("you already Guess this Number so please choose another Number")
    for i in choose_Word:
        if i==guess:
            display+=i
            pre_word.append(guess)
        elif i in pre_word:
            display+=i
        else:
            display+="_"
    print(display)


    if guess not in choose_Word:
        lives-=1
        print(f"you have only  {lives} lives so play well")
        if lives==0:
            Game_over=True
            print("You lose")

    if "_" not in display:
        Game_over=True
        print('''
                 _-====-__-======-__-========-_____-============-__
               _(                                                 _)
            OO(                                                   )_
           0  (_                  YOU WIN                         _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (BNSF 1995| |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################
''')
    print(stages[lives])


