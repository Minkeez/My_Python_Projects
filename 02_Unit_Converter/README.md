# Unit Converter

A versatile command-line program to convert values between various units, including **length, weight, volume, time, speed, digital storage, and temperature** (C, F, K).

---

### Overview

This **Unit Converter** uses a dictionary-based approach for most multiplicative conversions (e.g., meters to feet, kilograms to pounds) and a function-based approach for temperature conversions (which require an offset).

### Features

1. **Dictionary Lookup**
  - For categories like length, weight, volume, time, speed, and digital storage, conversions are purely multiplicative.
  - A dictionary (`CONVERSION_FACTORS`) maps each (`from_unit, to_unit`) pair to a **factor**.
2. **Offset-based Temperature**
  - A separate dictionary (`TEMPERATURE_CONVERSIONS`) stores **functions** that handle offsets (C ↔ F ↔ K).
3. **Modular Design**
  - The main logic is in `main.py`, while conversion factors and functions are in `main.py`.
  - Easily extended by adding more (`from_unit, to_unit`) pairs to the dictionaries or more categories.
4. **Command-Line Menu**
  - A simple menu lets you choose which category of unit conversion you want to perform.

### Usage
1. **Run** `main.py`:
```
python main.py
```
2. **Select a category** from the menu:
```
=== UNIT CONVERTER ===
1) Length
2) Weight
3) Volume
4) Time
5) Speed
6) Digital Storage
7) Temperature
8) Exit
Choose a category:
```
3. **Enter source unit, target unit, and value** when prompted.
#### Example (Length)
```
=== Length Conversion ===
Available units might include (m, km, ft, mi, kg, lb, etc.) depending on the dictionary.
From unit: m
To unit: ft
Enter value: 10
10.0 m = 32.8084 ft
```
#### Example (Temperature)
```
=== Temperature Conversion ===
Available units: C, F, K
From unit (C/F/K): c
To unit (C/F/K): f
Enter temperature value: 30
30.0°C = 86.00°F
```

### Adding More Conversions
- **Multiplicative** (length, weight, etc.):
  - In `conversion_unit.py`, add an try to `CONVERSION_FACTORS`, for example:
  ```
  ("yd", "ft"): 3.0,
  ("ft", "yd"): 1/3.0,
  ```
- **Temperature** (offset-based, e.g., Rankine, Réaumur, etc.):
  - Add a function in `conversion_unit.py` and then map it in `TEMPERATURE_CONVERSIONS`.

### Possible Enhancements
- **Validation**: Check whether the user's units are in a known list before looking up the dictionary.
- **Error Handling**: Suggest possible units if a conversions not found.
- **GUI Version**: Implement a graphical interface with dropdown menus (TKinter, PyQt). (like I do.)
- **Web API**: Create a simple Flask or FastAPI backend to perform conversions.
- **Logging**: Record each conversion into a log file or database.
- **Automated Tests**: Use `unittest` or `pytest` to ensure each dictionary entry is correct.
