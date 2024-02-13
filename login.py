# This function is used to login their respective account details
from hash_password import hash_password


def login():

  # we use while loop for continue infinite until condition fulfil
  while True:
    print(f"\n{'-'*30:^30}")
    print(f"{'Login Credentials..':^30}")
    print(f"{'-'*30:^30}")

    # taking input from user which user give when he/she sign up account
    username = input("Enter Username: ")
    print(f"{'-'*30:^30}")
    password = input("Enter password: ")

    # now reading text file for checking the inputted details and existing details
    with open("main_database//main_database.txt", 'r') as db:
      
      # run loop in file for getting lines in line variable from db file
      for line in db:
        
        # After getting single line then we use split(',') to separated all words and link with variables.
        # we use strip() to remove the '\n' in the last line
        # we can use this (, _ ) because we didn't want the third value so that's why we use it as none, aur ye agar use nh krte to error deta kiu k usko store bh to krna ha isliya aur ye utne hi dene hn jitne uske agay words hunge kiu k list return hogy to har words ko alag alag krke dega
        # we use slicing because at 0 index we got full name, at 1 index we got username and at 2 index we got hashed password
        words = line.strip().split(',')
        existing_username, existing_password = words[1], words[2]

        # This block check that inputted username and password is matching or not in db file
        if existing_username == username and existing_password == hash_password(
            password):
          print("\nLogin Successfully")

          # After matching the this break will exit from for loop
          break

      # When for loop complete and not got any things then this else block will execute
      else:
        print("Invalid login details! Please try again.")

        # here we use recursive function
        username = login()

    # this break we use to exit from while loop.
    break
  return username
