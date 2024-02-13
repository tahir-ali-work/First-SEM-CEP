#Reading products.txt file and fetch info of it
def product_list():

  # Initialize an empty list to store products
  products = []

  try:
    # Attempt to open the file 'main_database/products.txt' in read mode
    with open('main_database/products.txt', 'r') as file:

      # Iterate over each line in the file
      for line in file:

        # Split the line into fields using ':' as the delimiter
        # and strip any leading/trailing whitespace using .strip(),
        # then store the resulting list into the 'fields' variable/identifier.
        fields = line.strip().split(':')

        # Create a dictionary for each product using the fields
        product = {
            'ProductID': int(fields[0]),
            'Product Name': fields[1],
            'Price': float(fields[2]),
            'Description': fields[3],
            'Availability': int(fields[4])
        }

        # Append the product dictionary to the products list
        products.append(product)

  except FileNotFoundError:
    # Handle the case where the file is not found
    # Print an error message indicating that the product data file is not found
    print("Product data file not found.")

  # Return the list of products
  return products
