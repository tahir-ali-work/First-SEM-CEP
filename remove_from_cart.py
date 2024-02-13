def update_products_file(product_id, quantity):
  with open("main_database/products.txt", "r") as file:
    lines = file.readlines()

  with open("main_database/products.txt", "w") as file:
    for line in lines:
      # Split the line into parts
      parts = line.strip().split(":")
      current_product_id = int(parts[0])

      # If the current line corresponds to the product being removed, update the quantity
      if current_product_id == product_id:
        current_quantity = int(parts[-1])
        new_quantity = current_quantity + quantity
        parts[-1] = str(new_quantity)

      # Write the modified line back to the file
      file.write(":".join(parts) + "\n")
      
def remove_from_cart(cart_name, product_id, quantity):
  for item in cart_name:
    if int(item["Product ID"]) == product_id:
      if int(item["Quantity"]) >= quantity:
        # Reduce the quantity from the item in the cart
        item["Quantity"] -= quantity
        # Update the total bill
        item["Total Bill"] = item["Quantity"] * item["Product Price"]
        print(
            f"\nRemoved {quantity} units of {item['Product Name']} from the cart."
        )
        # Update the products.txt file with the new quantity
        update_products_file(product_id, quantity)
        return True
      else:
        print(
            "\nInvalid quantity. Quantity to remove exceeds the quantity in the cart."
        )
        return False

  # If the loop completes without finding the product, print a message
  print("\nProduct not found in the cart.")

  # Ask the user for input again
  new_product_id = int(input("\nEnter the product ID to remove from cart: "))
  new_quantity = int(input("\nEnter the quantity to remove: "))

  # Make another attempt to remove the product and capture the result
  result = remove_from_cart(cart_name, new_product_id, new_quantity)

  # Return the result of the recursive call
  return result



