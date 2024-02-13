#Importing os module
import os

# This function will clear the screen content.
def clear_screen():
  """This function will clear the screen content."""
  # Here we use the os.name which means check the operating system name, where 'nt' means window OS.
  # because different OS have different commands so thats why we first check for window if yes then run 'cls' otherwise it will execute else which is for other then windows
  os.system('cls' if os.name == 'nt' else 'clear')
