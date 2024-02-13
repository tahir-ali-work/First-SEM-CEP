#This function is used to show the shopping history
def display_shopping_history(username):
  
 # Constructing the file path for shopping history
  filename = f"main_database/user_details_database/user_{username}_all/shopping_history.txt"

  try:
    
    with open(filename, 'r') as file:
      
      shopping_history = []
      
      # Iterate through each line in the file
      for line in file:
        
        # Splitting the line into key-value pairs
        pairs = line.strip().split(',')

        # Creating a dictionary for each shopping history entry
        entry_dict = {}
        
        for pair in pairs:
          
          # Check if the pair can be unpacked into key and value
          if ':' in pair:
            
            # Split at the first occurrence of ':'
            key, value = pair.split(':',
                                    1)
            
            entry_dict[key.strip()] = value.strip()

        # Append the entry dictionary to the shopping history list
        shopping_history.append(entry_dict)

    # Check if there is any shopping history
    if not shopping_history:
      print("\nNo shopping history available.")

    # Iterate through each entry in the shopping history
    else:
      print(f"{'-' * 50}")
      print(f"{'Shopping History':^50}")
      for entry in shopping_history:
        print(f"{'-' * 50}")
        print(f"Product Name: {entry.get('Product Name')}")
        print(f"Quantity: {entry.get('Quantity')}")
        print(f"Date/Time: {entry.get('Date/Time')}")
        print(f"Total Bill: Rs.{entry.get('Total Bill')}")
      print(f"{'-' * 50}")

  #When file not found then this will print
  except FileNotFoundError:
    print("\nShopping history file not found. No shopping history available.")
    
  #if any value error then this will print
  except ValueError as e:
    print(f"Error: {e}")
