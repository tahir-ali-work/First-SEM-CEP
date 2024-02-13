#Importing functions from different files
from check_user_availability import check_username_availability
from hash_password import hash_password
from password_strength import check_password_strength
from text_animation import text_animation
import os


# This function take inputted values from user and then stored into files
def create_account():
  """This function basically creating a new account by taking inputs from user."""

  #It will print 50 hypens 
  print(f"{'-'*50}")
  
  #printing the title, .center(50) will center the text and complete length of this text is 50.
  print(f"{'Creating an Account..'.center(50)}")

  #It will print 50 hypen 
  print(f"{'-'*50}")

  # Take first name as input
  first_name = input(f"{'Enter First Name:':20} ")
  print(f"{'-'*50}")

  #Checking first name is alphabets or not, otherwise it will take again input for it
  while not (first_name.isalpha()):
    print(f"{'Invalid Input!'}")
    first_name = input(f"{'Enter First Name:':20} ")

  # Take last name as input
  last_name = input(f"{'Enter Last Name:':20} ")
  print(f"{'-'*50}")

  #Checking last name is alphabets or not, otherwise it will take again input for it
  while not (last_name.isalpha()):
    print(f"{'Invalid Input!'}")
    last_name = input(f"{'Enter last Name:':20} ")

  #Take address input
  home_address = input(f'{"Enter Home Address:":20} ')
  print(f"{'-'*50}")
  shipping_address = input(f'{"Enter Shipping Address:":20} ')
  print(f"{'-'*50}")

  #Take username input
  username = input(f"{'Enter Username:':20}")
  print(f"{'-'*50}")

  #Check_username_availability is a user defined function which will check the username is exist or not, otherwise take again input of it.
  while check_username_availability(username):
    print(
        f"Username '{username}' is already taken. Please choose a different username."
    )
    username = input(f"{'Enter Username:':20}")

  #Intiate the Loop for checking password is meet with criterias or not which is defined in check_password_strength function
  while True:

    #Take password as input
    password = input(f'{"Enter Password":20}')
    print(f"{'-'*50}")

    # Check password strength, if is strong then function will return true, otherwise it will return false and print message which condition is not meet
    #From function we got two values in form of tuple then we unpack into var/identifiers.
    is_strong, message = check_password_strength(password)

    #If function return true then if-statement will execute and print message which is defined in function and then break which will break from the current while loop because we done with password
    if is_strong:
      print(f"{'-'*50}")
      print(message)
      print(f"{'-'*50}")
      break

    #If function return false then else-statement will execute and print message which is defined in function and then again taking input until all condtions      #meet
    else:
      print(message)
  print(f"{'-'*50}")
  
  #Take input phone number of user
  phone_no = int(input(f'{"Enter Phone Number:":20}'))
  print(f"{'-'*50}")
  
  #converting password into hash password using SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that produces a fixed-size output of 256 bits, commonly represented as a 64-character hexadecimal number. It is widely used in various security applications and protocols to ensure the integrity and authenticity of data.
  hashed_password = hash_password(password)

  # merge first and last names
  full_name = first_name + " " + last_name

  # Create a dictionary with user input
  user_details = {
      'First Name': first_name,
      'Last Name': last_name,
      'Username': username,
      'Home Address': home_address,
      'Shipping Address': shipping_address,
      'Phone Number': phone_no
  }

  #Declare folder path in identifier/variable
  #We use f-string because we want a specific folder name which is create by username.
  #In this folder we save three files, one is user details second is cart_save and last is shopping history
  folder_path = f'main_database/user_details_database/user_{username}_all'

  #Now checking the folder is exist or not, if not then it will create folder.
  if not (os.path.exists(folder_path)):
    os.makedirs(folder_path)

  # Generate a unique file name based on the username
  #We use f-string because we want a specific file name which is create by username.
  #In this file, we save all inputted details from user.
  file_path = f'main_database//user_details_database//user_{username}_all//user_{username}.txt'

  #This will first create file as per above file path and then write the details into the file
  with open(file_path, 'w') as file:

    # .items() will return (key:value) in tuple and then complete will be in form of list, we use for-loop to get tuple set and iterate over it to get value of key in key var and same for val.
    for key, value in user_details.items():

      #Basically we didn't want comma in the last so that why we set condtion when iteration reach to last obj then write in this style otherwise write in the style which is declare in else block.
      if user_details[key] == phone_no:
        file.write(f"{key}:{value}")
      else:
        file.write(f'{key}:{value},')

  #After creating folder as per name store in folder_path then it will create two more file which is shoping history where all checkouts data will be stored and another file which is user_cart where all cart data will be stored.
  file = open(
      f"main_database/user_details_database/user_{username}_all/shopping_history.txt",
      'w')
  file.close()
  
  file = open(
      f"main_database/user_details_database/user_{username}_all/cart_save.txt",
      'w')
  file.close()

  # Open the file in append mode and write the user's information (Full name/Username/Hashed password)
  with open("main_database//main_database.txt", "a") as file:

    # We print Full name then username and then password which is hashed and then we put '\n' for when we update with other user details so this will continue from next line not in a single line, as we know that after using append mode the cursor is at the end of file after opening file.
    file.write(f"{full_name},{username},{hashed_password}\n")

  # After successfully write in file then this message wil print.
  print("\nAccount created successfully..\n")

  #After creating account this will print welcome message
  #text_animation is a user defined function which perform the animation of text.
  text_animation(
      f"Welcome {full_name.title()}! To The Online Shopping Cart App")

  #after above all, this function will return the username which is taken from user input.
  return username
