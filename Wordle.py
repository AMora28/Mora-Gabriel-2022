# Wordle
import random
import colorama
from colorama import init
from colorama import Fore, Back, Style
import os

# word list
word_list = ["babes", "cabin", "cable", "ables", "about", "abort",
        "above", "abuse", "abyss", "ached", "acids", "acorn", "acted",
        "Acres", "Actor", "Acute", "Admin", "Admit", "Adobe", "Adopt",
        "Again", "Agile", "Agree", "Aglet"]

colorama.init(autoreset=True)

word_list = [each_string.upper() for each_string in word_list]

turn = 0

Chosen_word = random.choice(word_list)
chosen_letters = list(Chosen_word)
print(Chosen_word)


# Table


Table = ["_", "_", "_", "_", "_",
        "_", "_", "_", "_", "_",
        "_", "_", "_", "_", "_",
        "_", "_", "_", "_", "_",
        "_", "_", "_", "_", "_",
        "_", "_", "_", "_", "_"]

# if game still going
game_still_going = True


def clear_b():
os.system('cls')

def display_board():
   print(Table[0] + "|" + Table[1] + "|" + Table[2] + "|" + Table[3] + "|" + Table[4])
   print(Table[5] + "|" + Table[6] + "|" + Table[7] + "|" + Table[8] + "|" + Table[9])
   print(Table[10] + "|" + Table[11] + "|" + Table[12] + "|" + Table[13] + "|" + Table[14])
   print(Table[15] + "|" + Table[16] + "|" + Table[17] + "|" + Table[18] + "|" + Table[19])
   print(Table[20] + "|" + Table[21] + "|" + Table[22] + "|" + Table[23] + "|" + Table[24])
   print(Table[25] + "|" + Table[26] + "|" + Table[27] + "|" + Table[28] + "|" + Table[29])


def play_game():
   global turn
   # display initial board
   turn += 1
   display_board()

   while game_still_going:
       # handle players7

       handle_turn()

def handle_turn():
   global Guess
   U_Input = input("GUESS THE 5 LETTER WORD!\n")
   Guess = U_Input.upper()
   Guess_check()



def Guess_check():
   global Guess
   global F_Guess
   F_Guess = list(Guess)
   letter_count = len(F_Guess)
   if letter_count >= 6:
       clear_b()
       display_board()
       print("only 5 letter words!")
       handle_turn()
   elif letter_count <= 4:
       clear_b()
       display_board()
       print("only 5 letter words!")
       handle_turn()
   else:
       clear_b()
       check_word()

def check_word():
   # checking First Row ---------------------------------------------------------------------------------------
   if turn == 1:
       # First Letter Check
       if F_Guess[0] == chosen_letters[0]:
           Table[0] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] in chosen_letters:
           Table[0] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] != chosen_letters[0] or F_Guess[0] != chosen_letters:
           Table[0] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET

       # second Letter Check

       if F_Guess[1] == chosen_letters[1]:
           Table[1] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] in chosen_letters:
           Table[1] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] != chosen_letters[1] or F_Guess[1] != chosen_letters:
           Table[1] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET

           # third Letter Check

       if F_Guess[2] == chosen_letters[2]:
           Table[2] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] in chosen_letters:
           Table[2] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] != chosen_letters[2] or F_Guess[2] != chosen_letters:
           Table[2] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET

           # fourth Letter Check

       if F_Guess[3] == chosen_letters[3]:
           Table[3] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] in chosen_letters:
           Table[3] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] != chosen_letters[3] or F_Guess[3] != chosen_letters:
           Table[3] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET

           # fith Letter Check

       if F_Guess[4] == chosen_letters[4]:
           Table[4] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] in chosen_letters:
           Table[4] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] != chosen_letters[4] or F_Guess[4] != chosen_letters:
           Table[4] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       check_if_game_over()
   # checking Second Row ---------------------------------------------------------------------------------------

   elif turn == 2:
       # First Letter Check
       if F_Guess[0] == chosen_letters[0]:
           Table[5] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] in chosen_letters:
           Table[5] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] != chosen_letters[0] or F_Guess[0] != chosen_letters:
           Table[5] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET

       # second Letter Check

       if F_Guess[1] == chosen_letters[1]:
           Table[6] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] in chosen_letters:
           Table[6] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] != chosen_letters[1] or F_Guess[1] != chosen_letters:
           Table[6] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET

           # third Letter Check

       if F_Guess[2] == chosen_letters[2]:
           Table[7] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] in chosen_letters:
           Table[7] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] != chosen_letters[2] or F_Guess[2] != chosen_letters:
           Table[7] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET

           # fourth Letter Check

       if F_Guess[3] == chosen_letters[3]:
           Table[8] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] in chosen_letters:
           Table[8] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] != chosen_letters[3] or F_Guess[3] != chosen_letters:
           Table[8] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET

           # fith Letter Check

       if F_Guess[4] == chosen_letters[4]:
           Table[9] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] in chosen_letters:
           Table[9] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] != chosen_letters[4] or F_Guess[4] != chosen_letters:
           Table[9] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       check_if_game_over()
       # checking third Row ---------------------------------------------------------------------------------------

   elif turn == 3:
       # First Letter Check
       if F_Guess[0] == chosen_letters[0]:
           Table[10] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] in chosen_letters:
           Table[10] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] != chosen_letters[0] or F_Guess[0] != chosen_letters:
           Table[10] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET

       # second Letter Check

       if F_Guess[1] == chosen_letters[1]:
           Table[11] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] in chosen_letters:
           Table[11] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] != chosen_letters[1] or F_Guess[1] != chosen_letters:
           Table[11] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET

           # third Letter Check

       if F_Guess[2] == chosen_letters[2]:
           Table[12] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] in chosen_letters:
           Table[12] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] != chosen_letters[2] or F_Guess[2] != chosen_letters:
           Table[12] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET

           # fourth Letter Check

       if F_Guess[3] == chosen_letters[3]:
           Table[13] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] in chosen_letters:
           Table[13] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] != chosen_letters[3] or F_Guess[3] != chosen_letters:
           Table[13] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET

           # fith Letter Check

       if F_Guess[4] == chosen_letters[4]:
           Table[14] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] in chosen_letters:
           Table[14] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] != chosen_letters[4] or F_Guess[4] != chosen_letters:
           Table[14] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET

       check_if_game_over()

       # checking fourth Row ---------------------------------------------------------------------------------------

   elif turn == 4:
       # First Letter Check
       if F_Guess[0] == chosen_letters[0]:
           Table[15] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] in chosen_letters:
           Table[15] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] != chosen_letters[0] or F_Guess[0] != chosen_letters:
           Table[15] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET

       # second Letter Check

       if F_Guess[1] == chosen_letters[1]:
           Table[16] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] in chosen_letters:
           Table[16] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] != chosen_letters[1] or F_Guess[1] != chosen_letters:
           Table[16] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET

           # third Letter Check

       if F_Guess[2] == chosen_letters[2]:
           Table[17] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] in chosen_letters:
           Table[17] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] != chosen_letters[2] or F_Guess[2] != chosen_letters:
           Table[17] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET

           # fourth Letter Check

       if F_Guess[3] == chosen_letters[3]:
           Table[18] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] in chosen_letters:
           Table[18] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] != chosen_letters[3] or F_Guess[3] != chosen_letters:
           Table[18] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET

           # fith Letter Check

       if F_Guess[4] == chosen_letters[4]:
           Table[19] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] in chosen_letters:
           Table[19] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] != chosen_letters[4] or F_Guess[4] != chosen_letters:
           Table[19] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET

       check_if_game_over()

       # checking Fith/last Row ---------------------------------------------------------------------------------------
   elif turn == 6:
           # First Letter Check
       if F_Guess[0] == chosen_letters[0]:
               Table[20] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] in chosen_letters:
               Table[20] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] != chosen_letters[0] or F_Guess[0] != chosen_letters:
               Table[20] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET

           # second Letter Check

       if F_Guess[1] == chosen_letters[1]:
               Table[21] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] in chosen_letters:
               Table[21] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] != chosen_letters[1] or F_Guess[1] != chosen_letters:
               Table[21] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET

           # third Letter Check

       if F_Guess[2] == chosen_letters[2]:
               Table[22] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] in chosen_letters:
               Table[22] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] != chosen_letters[2] or F_Guess[2] != chosen_letters:
               Table[22] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET

               # fourth Letter Check

       if F_Guess[3] == chosen_letters[3]:
               Table[23] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] in chosen_letters:
               Table[23] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] != chosen_letters[3] or F_Guess[3] != chosen_letters:
               Table[23] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET

               # fith Letter Check

       if F_Guess[4] == chosen_letters[4]:
               Table[24] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] in chosen_letters:
               Table[24] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] != chosen_letters[4] or F_Guess[4] != chosen_letters:
               Table[24] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET

       check_if_game_over()

       # Checking 6th Row ---------------------------------------------------------------------------------------

   elif turn == 6:
       # First Letter Check
       if F_Guess[0] == chosen_letters[0]:
               Table[25] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] in chosen_letters:
               Table[25] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET
       elif F_Guess[0] != chosen_letters[0] or F_Guess[0] != chosen_letters:
               Table[25] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[0] + colorama.Back.RESET

       # second Letter Check

       if F_Guess[1] == chosen_letters[1]:
               Table[26] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] in chosen_letters:
               Table[26] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET
       elif F_Guess[1] != chosen_letters[1] or F_Guess[1] != chosen_letters:
               Table[26] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[1] + colorama.Back.RESET

       # third Letter Check

       if F_Guess[2] == chosen_letters[2]:
               Table[27] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] in chosen_letters:
               Table[27] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET
       elif F_Guess[2] != chosen_letters[2] or F_Guess[2] != chosen_letters:
               Table[27] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[2] + colorama.Back.RESET

       # fourth Letter Check

       if F_Guess[3] == chosen_letters[3]:
               Table[28] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] in chosen_letters:
               Table[28] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET
       elif F_Guess[3] != chosen_letters[3] or F_Guess[3] != chosen_letters:
               Table[28] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[3] + colorama.Back.RESET

       # fith Letter Check

       if F_Guess[4] == chosen_letters[4]:
               Table[29] = Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] in chosen_letters:
               Table[29] = Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET
       elif F_Guess[4] != chosen_letters[4] or F_Guess[4] != chosen_letters:
               Table[29] = Back.WHITE + Fore.LIGHTWHITE_EX + F_Guess[4] + colorama.Back.RESET

       check_if_game_over()

       # All rows done ---------------------------------------------------------------------------------------

       # When all if done. It will pass to Check_if_Game_over
   check_if_game_over()





def check_if_game_over():
   global game_still_going
   global F_Guess
   if turn == 6:
       game_still_going = False
       clear_b()
       display_board()
       print("Better Luck Next Time!\nThe Word Was", Chosen_word)
   elif Guess == Chosen_word:
       game_still_going = False
       clear_b()
       display_board()
       print("Congrats You have solved the word!\nThe Word Was", Chosen_word)
   else:
       clear_b()
       play_game()


play_game()

