from datetime import date, datetime

try:
  birth_date_str = input("Enter your birth Date(YYYYMMDD ex. 2002-11-25):")
  birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
  today = date.today()

  if birth_date > today:
    print("Error: Birthdate cannot be in the future.")
  else:
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
      age -= 1
    if (today.month, today.day) == (birth_date.month, birth_date.day):
      print("Happy Birthday! 🎉")

    print(f"Your age is {age}")

except ValueError:
  print("Invalid date format! Please enter in YYYY-MM-DD format.")
