import datetime

def main():
  print("=== Age Calculator ===")
  try:
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    print(f"You entered: {birth_year}/{birth_month}/{birth_day}")

    birth_date = datetime.date(birth_year, birth_month, birth_day)
    today = datetime.date.today()  # current system date

    # Check if birth_date is in the future
    if birth_date > today:
      print("Error: Your date of birth is in the future. Please enter a valid birthdate.")
    else:
      age = today.year - birth_date.year
      # If today's month/day is before birth month/day, subtract 1 year
      if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

      print(f"Your age is: {age} years old.")

  except ValueError:
    print("Your date of birth is incorrect.")

if __name__ == "__main__":
  main()