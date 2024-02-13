#Importing functions from different files
from products import product_list
import time
from stock_update import stock_update

# Dictionary to store shopping history details
shopping_history = {}

# Function to handle the purchase of a product details
def buy_now(products, username):

  # Ask the user to input the Product ID to purchase 
  product_id = int(input("\nEnter the Product ID (0 to cancel): "))

  # Check if the user wants to cancel the operation (0 is to cancel)
  if product_id == 0:
    return

  # Check if the entered Product ID is within the valid range
  if 1 <= product_id <= len(products):

    # Get the selected product details
    selected_product = products[product_id - 1]

    # Display the selected product details
    print(
        f"\nSelected Product: {selected_product['Product Name']} - Price: Rs.{selected_product['Price']}"
    )

    # Ask the user to input the quantity of the product
    quantity_product = int(input("\nEnter the QTY of product: "))

    # Check if the entered quantity is within the available stock
    if 1 <= quantity_product <= selected_product['Availability']:

      # Extract product details
      product_name = selected_product['Product Name']
      product_price = selected_product['Price']
      totalbill = product_price * quantity_product

      # Get the current time in a formatted string
      formatted_time = time.strftime("%d %b %Y %I:%M:%S %p")

      # Display the purchased products details with data and time 
      print(f"{'-' * 50}")
      print(
          f"{'Product':16}: {product_name}\n{'Quantity':16}: {quantity_product}\n{'Purchased Time':16}: {formatted_time} "
      )
      print(f"{'-' * 50}")
      print(f'Your total bill is: {totalbill}')
      print(f"{'-' * 50}")

      # Update shopping history dictionary
      shopping_history.update({
          'Product ID': product_id,
          'Product Name': product_name,
          'Quantity': quantity_product,
          'Date/Time': formatted_time,
          'Total Bill': totalbill
      })

      # Update stock and shopping history file
      stock_update(product_id, quantity_product)

      #Write Shopping history details into file.
      path = f"main_database/user_details_database/user_{username}_all/shopping_history.txt"
      with open(path, "a") as file:
        for i, j in shopping_history.items():
          if i == 'Total Bill':
            file.write(f'{i}:{j}')
          else:
            file.write(f'{i}:{j}' + ',')
        file.write('\n')

      # Ask if the user wants to buy more items
      print(f'\n\nDo you want to buy more items?[y/n]')
      ans = input()

      # If yes, display the product list and call buy_now function recursively
      if ans.lower() == 'y':
        products = product_list()

        while True:
          print("Product List:")
          print(
              "------------------------------------------------------------------"
          )
          print(
              f"| {'ProductID':<10} | {'Product Name':<20} | {'Price':<10} | {'Availability':<12} |"
          )
          print(
              "------------------------------------------------------------------"
          )

          for product in products:
            print(
                f"| {product['ProductID']:<10} | {product['Product Name']:<20} | Rs.{product['Price']:<9.2f} | {product['Availability']:<12} |"
            )
          print(
              "------------------------------------------------------------------"
          )
          break
        buy_now(products, username)

      # If no, display a thank you message
      elif ans.lower() == 'n':
        print("\n\nThank you for shopping with us!")
        pass

    # Call buy_now function recursively to retry purchase
    else:
      print("\n\nInvalid quantity. Please try again.")
      buy_now(products, username)
      
  #If entered product ID is out of range then this will print
  else:
        print("\n\nInvalid Product ID. Please enter a valid ProductID.")
