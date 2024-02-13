# Importing time module from builtin python library
import time


#text_animation is a user defined function which perform the animation of text by using simple for-loop control structure.
#This function take parameter from user, first is "text" which we want to animate and other is "delay" which is basically after each iteration,how much time delay to print next characters.By default value is 0.005 seconds.
def text_animation(text, delay=0.005):
  """text_animation is a user defined function which perform the animation of text by using simple for-loop control structure.
This function take parameter from user, first is "text" which we want to animate and other is "delay" which is basically after each iteration,how much time delay to print next characters.By default value is 0.005 seconds."""

  #it will convert into form that first letter of all words will be capital and rest will be small.
  text = text.title()

  # we run the loop on text which will give single characters on each iterate.
  for char in str(text):
      
    print(char, end='', flush=True)
    # Jab aap text animation ka code likh rahe hain, aap chahte hain ki har character print
    # hone ke baad foran dikhe aur wait na kare. flush=True ka istemal isi purpose ke liye hota hai.
    # after getting characters we use delay to slow down the printing
    
    time.sleep(delay)  

  # Newline at the end
  print()
