import time
import sys

def countdown_timer(seconds):
  """
  Runs a countdown timer from the given seconds down to 0.
  Displays the remaining time in MM:SS format.
  """
  while seconds:
    mins, secs = divmod(seconds, 60) # Convert to minutes and seconds
    timer_format = f"{mins:02d}:{secs:02d}"
    print(timer_format, end='\r') # Print on the same line
    time.sleep(1) # Wait for 1 second
    seconds -= 1
  
  print("⏰ Time's up!")  # Display when the timer reaches zero

if __name__ == "__main__":
  try:
    user_input = int(input("Enter time in seconds: ")) # Get input
    countdown_timer(user_input) # Start countdown
  except ValueError:
    print("Invalid input! Please enter a valid number.")
    sys.exit(1)