#Importing functions from different file.
from remove_from_cart import remove_from_cart
from clear_screen import clear_screen
from load_cart import load_cart_from_file
from text_animation import text_animation

# Function to view the items in the shopping cart
def view_cart(cart_name, username):

  # Clear the terminal screen
  clear_screen()

  # Load the shopping cart details from the file
  cart_name = load_cart_from_file(username)

  # Check if the cart is empty
  if not cart_name:
    text_animation("\nYour cart is empty.\n")
    
  else:
    while True:
      
      # Display the details of each item in the cart
      for i in cart_name:
        if i['Quantity'] > 0:
          text_animation(f"{'-' * 30}\n"
                f"Product ID: {i['Product ID']}\n"
                f"Product Name: {i['Product Name']}\n"
                f"Product Price: {i['Product Price']}\n"
                f"Quantity: {i['Quantity']}\n"
                f"Total Bill: {i['Total Bill']}\n"
                f"{'-' * 30}")

      # Display menu options
      text_animation("\na)Remove from cart\nb) Back to Menu\n")
      choice_inp = input("Enter your choice: ")

      text_animation(f"You chose: {choice_inp}")

      if choice_inp.lower() == "a":
        while True:
          try:
            
            # Prompt the user to enter the product ID and quantity to remove from the cart
            product_id = int(
                input("\nEnter the product ID to remove from cart: "))
            qty = int(input("\nEnter the quantity to remove: "))

            #This will execute the remove cart function if user select opt a.
            remove_result = remove_from_cart(cart_name, product_id, qty)

            if remove_result:
              # If the removal was successful, update the cart_save.txt file about their details because after removing QTY, this will update their info into cart_save.txt again
              file_path = f"main_database/user_details_database/user_{username}_all/cart_save.txt"
              with open(file_path, 'w') as file:
                for i in cart_name:
                  if i['Quantity'] > 0:
                    for j, k in i.items():
                      if j == 'Total Bill':
                        file.write(f"{j}:{k}")
                      else:
                        file.write(f"{j}:{k},")
                    file.write(f"\n")

              # Exit the inner loop if removal is successful
              break
            
            else:
              text_animation("\nProduct not found or invalid quantity. Please try again.")

          except ValueError:
            text_animation("\nInvalid input. Please enter a valid number.")

      elif choice_inp.lower() == 'b':
        break

      else:
        text_animation("\nInvalid Input\n\n")
