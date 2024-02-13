# Importing necessary functions and modules from other files
from add_to_cart import add_to_cart
from clear_screen import clear_screen
from products import product_list
from view_cart import view_cart
from buyNow import buy_now


# Function to display the product list and provide options to the user
def display_products_list(products, cart_name, username):

  #clear_sreen is a user-defined function which is used to clear the screen
  clear_screen()

  #Then skip next line
  print()

  while True:

    # Field width specifier within the curly braces.
    # < denotes left-aligning the text, and 10 is the width of the field,
    # ensuring that the total width is 10 characters.
    print("Product List:")
    print("------------------------------------------------------------------")
    print(
        f"| {'ProductID':<10} | {'Product Name':<20} | {'Price':<10} | {'Availability':<12} |"
    )
    print("------------------------------------------------------------------")

    # Iterate over each product and print its details
    for product in products:
      print(
          f"| {product['ProductID']:<10} | {product['Product Name']:<20} | Rs.{product['Price']:<9.2f} | {product['Availability']:<12} |"
      )
    print("------------------------------------------------------------------")

    print("a)Add to Cart\nb)Buy Now\nc)View Cart\nd)Back to menu")

    #Taking input from user as per above text
    choice_in = input()

    # If user chooses 'a', add the product to the cart
    if choice_in.lower() == 'a':

      #product_list is a user-defined function which is used to read products.txt from main_database folder and return the list of products.
      product = product_list()

      #We give above data in product var/identifier and cart_name which is also give to display_products_list function and username which is enter at the time of login or create account after it this will break the current loop only
      add_to_cart(product, cart_name, username)
      break

    # If user chooses 'b', buy the product now
    elif choice_in.lower() == 'b':
      
      #product_list is a user-defined function which is used to read products.txt from main_database folder and return the list of products.
      product = product_list()

      #This function will purchase item and that details will store in shopping history file.
      buy_now(product, username)
      break

    # If user chooses 'c', view the contents of the cart
    elif choice_in.lower() == 'c':
      
      # Function to view the items in the shopping cart
      view_cart(cart_name, username)
      break

    # If user chooses 'd', exit from the loop and return to the main menu
    elif choice_in.lower() == 'd':
      break
    #If user enter other than printed options then this will print
    else:
      print("Invalid choice\n")
