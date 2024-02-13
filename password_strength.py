#This function will checking the password that is it meet criterias which is defined below or not.
#The any() function is a built-in Python function that returns True if at least one element of an iterable (such as a list, tuple, or string) is true. If the iterable is empty, it returns False.
#The return statement is returning a tuple with two values. When this function is called, you can receive the result as a tuple and unpack it into separate variables. 

def check_password_strength(password):
  #This function will checking the password that is it meet criterias which is defined below or not.
  
  # Minimum length check
  if len(password) < 8:
    return False, "\nPassword should be at least 8 characters long\n"

  # Check for at least one uppercase letter
  if not any(char.isupper() for char in password):
    return False, "\nPassword should contain at least one uppercase letter\n"

  # Check for at least one lowercase letter
  if not any(char.islower() for char in password):
    return False, "\nPassword should contain at least one lowercase letter\n"

  # Check for at least one digit
  if not any(char.isdigit() for char in password):
    return False, "\nPassword should contain at least one digit\n"

  # Check for at least one special character
  special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
  if not any(char in special_characters for char in password):
    return False, "\nPassword should contain at least one special character\n"

  #If all conditions meet then this will return True with message both will in form of tuple.
  return True, f"{'Password is strong':^50}"
