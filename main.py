from clear_screen import clear_screen
from text_animation import text_animation
from create_acc import create_account
from login import login
from display_menu import display_menu
import time

def welcome_message():
  border = "*******************************"
  print(border)
  text_animation("*   Welcome to the App!       *", 0.005)
  print("*                             *")
  text_animation("*  1. Sign Up                 *", 0.005)
  print("*                             *")
  text_animation("*  2. Login Account           *", 0.005)
  print("*                             *")
  text_animation("*  3. Exit cart app           *", 0.005)
  print("*                             *")
  print(border)


#Initilize cart as list for storing products in main memory until use go back from add to cart option, after that it will be saved in a file
cart = []

# initialize the program in loop to continous run until exit option not execute
while True:

  # before starting app this function will clear the screen content
  #clear_sreen is a user-defined function which is used to clear the screen
  clear_screen()

  # it will print the text like welcome , sign,login
  welcome_message()

  # now selecting choice which we want to do like sign or login or quit to app
  #text_animation is a user defined function which perform the animation of text.
  text_animation("\nSelect an option (1 or 2 or 3): ")

  #taking input from user(1,2,3)
  choice = input()

  # if user type 1 then it go to the process of sign up
  if choice == "1":

    # first clear the previous content
    #clear_sreen is a user-defined function which is used to clear the screen
    clear_screen()

    #create_account is a user defined function which perform the sign up process, and return only username which will use further in the app
    user = create_account()

    #After sign up process, in which last message is about successfully creation of account then this statement will execute this will skip next line.
    print()

    #Initiatlizing while-loop
    while True:

      print()

      #display_menu is a user defined function which is used to print the menu like View product list etc.
      display_menu(cart, user)

  # if this true then it will go for login account
  elif choice == "2":

    # after taking input we give to login function and then this will check it in database and act accordingly
    user = login()

    while True:
      print()

      #display_menu is a user defined function which is used to print the menu like View product list etc.
      display_menu(cart, user)

  # if this is true then it will exit from app
  elif choice == '3':

    #First clear the terminal screen
    clear_screen()
    
    # after clear screen this print the message
    text_animation("Quitting the App. Goodbye!")

    #After write text it will hold for 1 sec
    time.sleep(1)
    
    break

  # if choice is out of range then this block will execute
  else:
    text_animation("Invalid choice.")
    print()

    #After writing it will hold for 0.5 sec
    time.sleep(0.5)

    #It will continue to start
    continue
