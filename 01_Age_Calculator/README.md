# Age Calculator

A simple command-line utility to calculate a user's age based on their date of birth.

### Overview

This **Age Calculator** allows users to input a birthdate (year, month, and day) and then calculates their current age in years (and optionally months/days). By default, it uses the system's current date to do the calculation.

### Features

- **Basic Age Calculation:**
  Subtracts the birth year from the current year, adjusting if the birthday hasn't occurred yet this year.
- **Error Handling:**
  Catches invalid dates (like `2022/02/30`) and prints an error message.
- **Easy to Extend:**
  You can enhance this tool to calculate months and days using external libraries like `dateutil`.

### Example Usage

```
=== Age Calculator ===
Enter your birth year (YYYY): 1990
Enter your birth month (1-12): 12
Enter your birth day (1-31): 5
You are 32 years old.
```

### Requirements

- **Python 3.7+** (earlier versions may work but not recommended)
- No additional libraries required for the basic version.
  _(Optional)_ For advanced calculations like months/days difference, install `dateutil`:

```
pip install python-dateutil
```

### How it Works

1. The Script prompts for the user's **year, month, day** of birth.
2. It retrieves today's date from the system using the `datetime` module.
3. It calculates the difference in years and adjusts by one if the current month/day is earlier than the birth month/day.
4. Finally, it prints out the user's age or displays an error if the date is invalid.

### Possible Improvements

- **Month/Day Calculation:**
  Use `dateutil.relativedelta` to display the exact age in years, months, and days.
- **Future-Date Check:**
  If a user accidentally inputs a future birth date (e.g., 2050), display a warning.
- **GUI Version:**
  Integrate with `Tkinter` or `PyQt` to provide a graphical interface.
- **Web Version:**
  Build a simple Flask or FastAPI app to take birthdates and return ages via a web interface.
