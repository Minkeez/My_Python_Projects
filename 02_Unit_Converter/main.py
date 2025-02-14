import sys
from conversion_unit import CONVERSION_FACTORS, TEMPERATURE_CONVERSIONS

def show_menu():
  print("=== UNIT CONVERTER ===")
  print("1) Length")
  print("2) Weight")
  print("3) Volume")
  print("4) Time")
  print("5) Speed")
  print("6) Digital Storage")
  print("7) Temperature")
  print("8) Exit")

def convert_multiplicative(category_name):
  """
  This function handles any conversion that is purely multiplicative
  (e.g., length, weight, volume, etc.), based on CONVERSION_FACTORS.
  """
  print(f"=== {category_name} Conversion ===")
  print("Available units might include (m, km, ft, mi, kg, lb, etc.) depending on the dictionary.")
  src_unit = input("From unit: ").lower().strip()
  target_unit = input("To unit: ").lower().strip()
  
  try:
    value = float(input("Enter value: "))
  except ValueError:
    print("Invalid value.")
    return

  key = (src_unit, target_unit)
  if key in CONVERSION_FACTORS:
    factor = CONVERSION_FACTORS[key]
    result = value * factor
    print(f"{value} {src_unit} = {result:.4f} {target_unit}\n")
  else:
    print(f"Conversion from '{src_unit}' to '{target_unit}' not found.\n")

def convert_temperature():
  """
  This function handles temperature conversions using TEMPERATURE_CONVERSIONS
  (offset-based). E.g., f, f->c, c->k, etc.
  """

  print("=== Temperature Conversion ===")
  print("Available units: C, F, K")

  src_unit = input("From unit (C/F/K): ").lower().strip()
  target_unit = input("To unit (C/F/K): ").lower().strip()

  try:
    value = float(input("Enter temperature value: "))
  except ValueError:
    print("Invalid value.")
    return
  
  key = (src_unit, target_unit)
  if key in TEMPERATURE_CONVERSIONS:
    func = TEMPERATURE_CONVERSIONS[key]
    result = func(value)
    print(f"{value}°{src_unit.upper()} = {result:.2f}°{target_unit.upper()}\n")
  else:
    print(f"Temperature conversion from '{src_unit}' to '{target_unit}' not found.\n")

def main():
  while True:
    show_menu()
    choice = input("Choose a category: ")

    if choice == '1':
      convert_multiplicative("Length")
    elif choice == '2':
      convert_multiplicative("Weight")
    elif choice == '3':
      convert_multiplicative("Volume")
    elif choice == '4':
      convert_multiplicative("Time")
    elif choice == '5':
      convert_multiplicative("Speed")
    elif choice == '6':
      convert_multiplicative("Digital Storage")
    elif choice == '7':
      convert_temperature()
    elif choice == '8':
      print("Exiting the program.")
      sys.exit()
    else:
      print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
  main()
