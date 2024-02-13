#Importing function from other file
from stock_update import stock_update


# Function to add a product to the cart
def add_to_cart(products, cart_name, username):
  continue_adding = True

  while continue_adding:
    
    # Ask the user to input the Product ID to add to the cart
    product_id_str = input("\nEnter the Product ID (0 to cancel): ")

    try:
      
      # Convert the input to an integer
      product_id = int(product_id_str)

      # Check if the user wants to cancel the operation (0 is to cancel)
      if product_id == 0:
        break

      # Check if the entered Product ID is within the valid range
      if 1 <= product_id <= len(products):
        
        # Get the selected product details
        selected_product = products[product_id - 1]

        # Ask the user to input the quantity of the product
        while True:

          #Taking input for QTY
          quantity_product_str = input("\nEnter the QTY of product: ")

          #Checking input is digits or not
          if quantity_product_str.isdigit():

            #Convert str into int
            quantity_product = int(quantity_product_str)

            #This break statement will exit from the current loop.
            break

          #If not digits then this will print and take again input and check condtion.
          else:
            print(
                "\nInvalid input. Please enter a valid integer for Quantity.")

        # Check if the entered quantity is within the available stock
        if 1 <= quantity_product <= selected_product['Availability']:
          
          # Assign the product details to a variable
          product_name = selected_product['Product Name']
          product_price = selected_product['Price']

          # Initialize var/identifier to check if the product is already in the cart or not
          product_already_in_cart = False

          # Loop through the cart to check if the product is already present
          for item in cart_name:

            #Checking selected product name is exist in cart or not.
            if item["Product Name"] == product_name:
              
              # Product is already in the cart, update quantity and total bill
              item["Quantity"] += quantity_product
              item["Total Bill"] = item["Quantity"] * item["Product Price"]
              
              product_already_in_cart = True

              # No need to continue checking once the product is found
              break  

          if not product_already_in_cart:
            
            # If the product is not already in the cart, add it to the cart
            cart_name.append({
                "Product ID": product_id,
                "Product Name": product_name,
                "Product Price": product_price,
                "Quantity": quantity_product,
                "Total Bill": product_price * quantity_product
            })

          # Printing the message about the product which is added to the cart
          print(f"\n{product_name} (QTY: {quantity_product}) added to cart.\n")

          #Declaring file path
          file_path = f"main_database/user_details_database/user_{username}_all/cart_save.txt"

          # Write the cart details in the above declare file path.
          with open(file_path, 'w') as file:
            for i in cart_name:
              for j, k in i.items():
                if j == 'Total Bill':
                  file.write(f"{j}:{k}")
                else:
                  file.write(f"{j}:{k},")
              file.write(f"\n")

            #This will update the QTY in products.txt, when any user add products in cart so QTY will minus from products.txt this will help to reduce over purchasing etc
            stock_update(product_id, quantity_product)

          while True:
            
            # Ask if the user wants to add more product to the cart
            ans = input("Do you want to add more products? (Y/N): ")

            if ans.lower().strip() == 'n':
              # If the user does not want to add more products, break out of the loop
              continue_adding = False

              #This break statement will exit from the current loop
              break
            
            elif ans.lower().strip() == 'y':
              continue_adding = True

              #This break statement will exit from the current loop
              break

            #If user input wrong then this will print and take again input because of while-loop.
            else:
              print("\nInvalid input. Please enter 'Y' or 'N'.")

        #If QTY enter by user and availability is not within range then this will print
        else:
          print("\nInsufficient stock. Please choose a lower quantity.")

      #When user enter out of range Product ID then this will print    
      else:
        print("\nInvalid Product ID. Please enter a valid ProductID.")

    #When user enter wrong product ID like any string etc then this will print
    except ValueError:
      print("Invalid input. Please enter a valid integer for Product ID.")
