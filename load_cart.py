
def load_cart_from_file(username):

  #Declaring file path
  filename = f"main_database/user_details_database/user_{username}_all/cart_save.txt"

  try:
    with open(filename, 'r') as file:
      cart = {}

      # Iterate through each line in the file
      for line in file:
        
        # Splitting the line into key-value pairs
        pairs = line.strip().split(',')

        # Creating a dictionary for each item
        item_dict = {}

        # Iterate through each pair in the line
        for pair in pairs:
          if ':' in pair:
            key_value = pair.split(':')
            if len(key_value) == 2:
              key, value = key_value
              item_dict[key.strip()] = value.strip()

        
        product_name = item_dict.get('Product Name')
        quantity = int(item_dict.get('Quantity', 0))
        product_price = float(item_dict.get('Product Price', '0.0'))
        
        # Check if the quantity is greater than 0 before updating the cart
        if quantity > 0:
          
          # Check if 'Total Bill' is not an empty string before converting to float
          total_bill_str = item_dict.get('Total Bill', '0')
          total_bill = float(total_bill_str) if total_bill_str else 0.0

          #if product is already in cart then this will only update QTY and bill not add separately
          if product_name in cart:
            
            # Convert the quantity to int before updating
            cart[product_name]['Quantity'] += quantity
            cart[product_name]['Total Bill'] += total_bill

          #If not in cart then this will update separately
          else:
            item_dict['Quantity'] = quantity
            item_dict['Total Bill'] = total_bill
            item_dict['Product Price'] = product_price
            cart[product_name] = item_dict

      # Return a list of cart items
      return list(cart.values())

  #If fille not found which we declare then this will print and return empty list
  except FileNotFoundError:
    print("\nCart file not found. Starting with an empty cart.")
    return []
