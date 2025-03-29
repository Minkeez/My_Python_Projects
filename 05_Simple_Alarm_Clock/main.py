import time
import datetime
import threading
import os
import winsound # For Windows sound

# List to store multiple alarms
alarms = []
stop_thread = False # Global flag to control the alarm thread

# Function to check alarms
def check_alarm():
  print("")
  global stop_thread
  while not stop_thread:
    now = datetime.datetime.now().strftime("%H:%M") # Get current time in HH:MM format
    for alarm in alarms:
      alarm_time = f"{alarm[0]:02d}:{alarm[1]:02d}"
      if now == alarm_time:
        print(f"\n⏰ Alarm! Time reached: {alarm_time}")
        play_sound() # Trigger alarm sound
        alarms.remove(alarm) # Remove alarm after triggering
    time.sleep(1) # Check every second

# Function to play alarm sound (Cross-platform support)
def play_sound():
  try:
    if os.name == 'nt': # Windows
      winsound.Beep(1000, 1000) # Beep at 1000 Hz for 1 second
    else: # Linux and MacOS
      os.system("echo -e '\a'") # Terminal bell sound
  except Exception as e:
    print(f"Error playing sound: {e}")

# Function to add an alarm
def add_alarm():
  print("")
  while True:
    try:
      alarm_time = input("Enter alarm time (HH:MM): ")
      hour, minute = map(int, alarm_time.split(":"))
      if 0 <= hour < 24 and 0 <= minute < 60:
        alarms.append((hour, minute))
        print(f"✅ Alarm set for {hour:02d}:{minute:02d}")
        break
      else:
        print("⚠️ Invalid time. Please enter HH:MM (24-hour format).")
    except ValueError:
      print("⚠️ Invalid input. Use HH:MM format.")

# Function to remove an alarm
def remove_alarm():
  print("")
  if not alarms:
    print("⚠️ No alarms to remove.")
    return
  print("⏰ Current alarms:")
  for i, alarm in enumerate(alarms):
    print(f"{i + 1}. {alarm[0]:02d}:{alarm[1]:02d}")

  try:
    index = int(input("Enter alarm number to remove: ")) - 1
    if 0 <= input < len(alarms):
      removed = alarms.pop(index)
      print(f"✅ Removed alarm: {removed[0]:02d}:{removed[1]:02d}")
    else:
      print("⚠️ Invalid selection.")
  except ValueError:
    print("⚠️ Invalid input.")

# Function to display alarms
def show_alarms():
  print("")
  if not alarms:
    print("⏳ No alarms set.")
  else:
    print("⏰ Active Alarms:")
    for i, alarm in enumerate(alarms):
      print(f"{i + 1}. {alarm[0]:02d}:{alarm[1]:02d}")

# Function to handle user commands
def alarm_menu():
  global stop_thread
  while True:
    print("\n===== Alarm Clock Menu =====")
    print("1. Set Alarm")
    print("2. Remove Alarm")
    print("3. View Alarms")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
      add_alarm()
    elif choice == "2":
      remove_alarm()
    elif choice == "3":
      show_alarms()
    elif choice == "4":
      print("\n⏳ Exiting alarm clock...")
      stop_thread = True # Stop alarm checking thread
      break
    else:
      print("⚠️ Invalid choice. Please try again.")

# Start the alarm checking thread
alarm_thread = threading.Thread(target=check_alarm, daemon=True)
alarm_thread.start()

# Start the user menu
alarm_menu()