import os
import time
import random

symbols = ['┌', '┘', '└','┐','|','-']


def print_hangman(points):
     if points == 0:
          print("┌-----┐\n|\n|\n|\n|\n|\n┴")
     elif points == 1:
          print("┌-----┐\n|     O\n|\n|\n|\n|\n┴")
     elif points == 2:
          print("┌-----┐\n|     O\n|    /  \n|\n|\n|\n┴")
     elif points == 3: # for the easy stage
          print("┌-----┐\n|     O\n|    /| \n|\n|\n|\n┴")
     elif points == 4: # for the easy stage
          print("┌-----┐\n|     O\n|    /|\\ \n|\n|\n|\n┴")
     elif points == 5: # for the easy stage
          print("┌-----┐\n|     O\n|    /|\\ \n|     |\n|\n|\n┴")
     elif points == 6: # for the easy stage
          print("┌-----┐\n|     O\n|    /|\\ \n|     |\n|    /\n|\n┴")
     elif points == 7: # for the easy stage
          print("┌-----┐\n|     O\n|    /|\\ \n|     |\n|    / \n|\n┴")
     elif points == 8: # for the easy stage
          print("┌-----┐\n|     O\n|    /|\\ \n|     |\n|    / \\ \n|\n┴")

# printing easier from the function
def color_print(r,g,b,text):
     print(color(r,g,b,text))

#coloring text funciton
def color(r,g,b,text):
     return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)

# start screen function that will show when the game start
def start_screen():
     title = "Welcome To Hangman"
     names = "Created By Yedidya"
     s = True
     for i in range(6):
          print(symbols[0] + symbols[5]*(len(title)+6) + symbols[3])
          if s:
               print(symbols[4] + " "*2 +'*' + title + '*' + " "*2 + symbols[4])
               print(symbols[4] + " "*3 + names + " "*3 + symbols[4])
          else:
               print(symbols[4] + " "*3 + title + " "*3 + symbols[4])
               print(symbols[4] + " "*2 + '*' + names + '*' + " "*2 + symbols[4])
          print(symbols[2] + symbols[5]*(len(title)+6) + symbols[1])
          s = not s
          time.sleep(1)
          os.system('cls')
     white = 255
     for i in range(11):
          color_print(white,white,white, symbols[0] + symbols[5]*(len(title)+6) + symbols[3])
          color_print(white,white,white, symbols[4] + " "*2 +'*' + title + '*' + " "*2 + symbols[4])
          color_print(white,white,white, symbols[4] + " "*3 + names + " "*3 + symbols[4])
          color_print(white,white,white,symbols[2] + symbols[5]*(len(title)+6) + symbols[1])
          time.sleep(0.4)
          os.system('cls')
          white -= 25
     time.sleep(1)

# function that sets the word for the game
def set_word(word, answer):
     valid = True
     while True:
          print ("To start the game please enter a word: ")
          word = input("").lower()
          ans = input("Your word is: " + word + ". Are sure? Y/N ").lower()
          if ans == "y":
               valid = False
               for i in range(len(word)):
                    answer = (answer+ '-')
               return word, answer
          else:
               valid = True
     
def easy_mode(word, answer):
     print()
     run = True
     limit = 1
     valid_input = False
     points = 0
     letters = list(word)
     solution = list(answer)
     
     while run:
          answer = "".join(solution)
          if answer == word:
               os.system('cls')
               print ("CONGRATULATIONS! You got it right! The word was " + word)
               break
          if points > 7:
               os.system('cls')
               print("We are sorry... you didn't get the word " + word)
               print_hangman(8)
               break
          os.system('cls')
          print ("Welcome to the EASY level of the game.\nThis level gives you 8 chances to guess the word.\nGood luck\n")
          print("The word is " + answer)
          print_hangman(points)
          guess = input("What letter is in this word? ").lower()
          if (len(guess) != limit) or (ord(guess) < 97 or ord(guess) > 122):
               while not valid_input:
                    guess = input("Invalid input. What letter is in this word? ").lower()
                    if (len(guess) != limit) or (ord(guess) < 97 or ord(guess) > 122):
                         valid_input = False
                    else:
                         valid_input = True
          else:
               wrong = False
               for i in range(len(answer)):
                    if guess != letters[i] and guess not in letters:
                         wrong = True
                         break
                    if guess == letters[i]:
                         solution[i] = guess
                         wrong = False
               if wrong:
                    print("wrong letter. try again")
                    points+=1
                    time.sleep(1)

def medium_mode(word, answer):
     run = True
     limit = 1
     valid_input = False
     points = 0
     letters = list(word)
     solution = list(answer)
     
     while run:
          answer = "".join(solution)
          if answer == word:
               os.system('cls')
               print ("CONGRATULATIONS! You got it right! The word was " + word)
               break
          if points > 7:
               os.system('cls')
               print("We are sorry... you didn't get the word " + word)
               print_hangman(8)
               break
          
          os.system('cls')
          print("Welcome to the MEDIUM level of the game.\nThis level gives you 5 chances to guess the word.\nGood luck\n")
          print("The word is " + answer)
          print_hangman(points)
          guess = input("What letter is in this word? ").lower()
          if (len(guess) != limit) or (ord(guess) < 97 or ord(guess) > 122):
               while not valid_input:
                    guess = input("Invalid input. What letter is in this word? ").lower()
                    if (len(guess) != limit) or (ord(guess) < 97 or ord(guess) > 122):
                         valid_input = False
                    else:
                         valid_input = True
          else:
               wrong = False
               for i in range(len(answer)):
                    if guess != letters[i] and guess not in letters:
                         wrong = True
                         break
                    if guess == letters[i]:
                         solution[i] = guess
                         wrong = False
               if wrong:
                    print("wrong letter. try again")
                    points+=2
                    time.sleep(1)

def hard_mode(word, answer):
     run = True
     limit = 1
     valid_input = False
     points = 0
     letters = list(word)
     solution = list(answer)
     
     while run:
          answer = "".join(solution)
          if answer == word:
               os.system('cls')
               print ("CONGRATULATIONS! You got it right! The word was " + word)
               break
          if points > 7:
               os.system('cls')
               print("We are sorry... you didn't get the word " + word)
               print_hangman(8)
               break
          
          os.system('cls')
          print("Welcome to the HARD level of the game.\nThis level gives you 3 chances to guess the word.\nGood luck\n")
          print("The word is " + answer)
          print_hangman(points)
          guess = input("What letter is in this word? ").lower()
          if (len(guess) != limit) or (ord(guess) < 97 or ord(guess) > 122):
               while not valid_input:
                    guess = input("Invalid input. What letter is in this word? ").lower()
                    if (len(guess) != limit) or (ord(guess) < 97 or ord(guess) > 122):
                         valid_input = False
                    else:
                         valid_input = True
          else:
               wrong = False
               for i in range(len(answer)):
                    if guess != letters[i] and guess not in letters:
                         wrong = True
                         break
                    if guess == letters[i]:
                         solution[i] = guess
                         wrong = False
               if wrong:
                    print("wrong letter. try again")
                    points+=3
                    time.sleep(1)


# main function of program

start_screen()
play = True
print("Let us start the game")

while play:
     word = ""
     answer = ""
     word, answer = set_word(word, answer)
     os.system('cls')
     select = int(input("Please select the level.\n 1- Easy Mode\n 2- Medium Mode\n 3- Hard Mode\nI selected level "))
     time.sleep(2)
     if select == 1:
          easy_mode(word, answer)
          time.sleep(3)
          os.system('cls')
     elif select == 2:
          medium_mode(word, answer)
          time.sleep(3)
          os.system('cls')
     elif select == 3:
          hard_mode(word, answer)
          time.sleep(3)
          os.system('cls')
     else:
          print ("\nWrong selection. Game Shutdown!!!")
          exit()
     ask = input("Thanks for playing. would you like to play again? Y/N ").lower()
     if ask == "y":
          os.system('cls')
          print ("Yay! let's play again!")
          play = True
          time.sleep(1)
     elif ask == "n":
          os.system('cls')
          print("Thank you for playing with us today :)\nGoodbye!")
          play = False
          time.sleep(3)
     else:
          print("well, guess you want to go home.\nGoodbye!")
          
