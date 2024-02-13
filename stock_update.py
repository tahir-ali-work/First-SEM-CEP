
def stock_update(product_id, qty):

  # List to store product details
  products = []

  # Read data from the file
  with open('main_database/products.txt', 'r') as file:
    for line in file:
      fields = line.strip().split(':')
      product_data = {
          'ProductID': int(fields[0]),
          'Product Name': fields[1],
          'Price': float(fields[2]),
          'Description': fields[3],
          'Availability': int(fields[4])
      }
      
      products.append(product_data)
      
  # Update the quantity for the specified product
  for product in products:
    if product['ProductID'] == product_id:
      product['Availability'] -= qty

  # Write the modified data back to the file
  with open('main_database/products.txt', 'w') as file:
    for product in products:
      line = f"{product['ProductID']}:{product['Product Name']}:{product['Price']}:{product['Description']}:{product['Availability']}\n"
      file.write(line)
