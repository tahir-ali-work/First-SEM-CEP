#Importing os module from builtin python libary
import os

#This function basically verifying the file that is it exist in given file path or not,if yes then it will just return true otherwise false.
def check_username_availability(username):
  """This function basically verifying the file that is it exist in given file path or not,if yes then it will just return true otherwise false."""

  # Check if the username is already taken by searching their folder name.
  file_path = f'main_database//user_details_database//user_{username}_all'

  #path.exist will check and returns only True or False.
  return os.path.exists(file_path)
