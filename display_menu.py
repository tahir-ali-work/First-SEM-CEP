#Importng functions from different files
from typing_extensions import clear_overloads
from clear_screen import clear_screen
from display_products import display_products_list
from load_shopping_history import display_shopping_history
from products import product_list
from text_animation import text_animation
from view_cart import view_cart
import time

#display_menu function is used to printing menu as below mention and take input for and then run respective function.
def display_menu(cart_name, username):

  #Desiging with printing menu
  print(f"{'-'*30}")
  print(f"{'Display MENU':^30}")
  print(f"{'-'*30}")
  text_animation('1. View Product List', 0.005)
  text_animation("2. View Cart", 0.005)
  text_animation("3. View Shopping History", 0.005)
  text_animation("4. Exit to application", 0.005)

  #Taking input where we want to go.
  text_animation("\nSelect an option (1 or 2 or 3 or 4): ")
  choice_1 = input()

  #This will show thw product list if true
  if choice_1 == "1":

    #product_list function returns the product after reading products.txt
    products = product_list()

    #display_products_list will take below arguements then print the list of products and their related input.
    display_products_list(products, cart_name, username)

  # Function to view the items in the shopping cart
  elif choice_1 == '2':
    view_cart(cart_name, username)

  #This function will show the history of products which we purchased
  elif choice_1 == '3':
    display_shopping_history(username)

  #When user wants to exit from app
  elif choice_1 == '4':
    text_animation("Quitting the App. Goodbye!")

    #After writing text it will hold for 0.3 sec then exit.
    time.sleep(0.3)
    exit()
    
  #if user input wrong then this will print
  else:
    print("\nInvalid input! try again")
    
