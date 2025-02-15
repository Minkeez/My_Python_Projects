import tkinter as tk
from tkinter import ttk, messagebox
import sys

from conversion_unit import CONVERSION_FACTORS, TEMPERATURE_CONVERSIONS

class UnitConverterApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Unit Converter (Tkinter Demo)")
    self.geometry("500x250")

    # Main frame
    main_frame = ttk.Frame(self, padding=10)
    main_frame.pack(fill="both", expand=True)

    # 1) FROM-UNIT label & combobox
    ttk.Label(main_frame, text="From Unit:").grid(row=0, column=0, sticky="w")
    self.from_unit_var = tk.StringVar()
    self.from_unit_combo = ttk.Combobox(main_frame, textvariable=self.from_unit_var)
    self.from_unit_combo.grid(row=0, column=1, padx=5, pady=5)

    # Populate 'from_unit' options from dictionary
    all_from_units = sorted(set(pair[0] for pair in CONVERSION_FACTORS.keys()))
    self.from_unit_combo["values"] = list(all_from_units)

    # Bind event to update 'to_unit' options dynamically
    self.from_unit_combo.bind("<<ComboboxSelected>>", self.update_to_unit_options)

    # 2) TO-UNIT label & combobox
    ttk.Label(main_frame, text="To Unit:").grid(row=1, column=0, sticky="w")
    self.to_unit_var = tk.StringVar()
    self.to_unit_combo = ttk.Combobox(main_frame, textvariable=self.to_unit_var)
    self.to_unit_combo.grid(row=1, column=1, padx=5, pady=5)

    # 3) VALUE label & entry
    ttk.Label(main_frame, text="Value:").grid(row=2, column=0, sticky="w")
    self.value_var = tk.StringVar()
    ttk.Entry(main_frame, textvariable=self.value_var).grid(row=2, column=1, padx=5 ,pady=5)

    # 4) Convert button
    convert_btn = ttk.Button(main_frame, text="Convert", command=self.perform_conversion)
    convert_btn.grid(row=3, column=0, columnspan=2, pady=10)

    # 5) Result label
    self.result_label = ttk.Label(main_frame, text="Result: ")
    self.result_label.grid(row=4, column=0, columnspan=2, sticky="w")

    # 6) Manage Conversions button
    manage_btn = ttk.Button(main_frame, text="Manage Conversions", command=self.open_manage_window)
    manage_btn.grid(row=5, column=0, columnspan=2, pady=5)

    # 7) Exit button
    exit_btn = ttk.Button(main_frame, text="Exit", command=self.exit_app)
    exit_btn.grid(row=6, column=0, columnspan=2, pady=5)
  
  def update_to_unit_options(self, event):
    """ Dynamically populate to_unit based on chosen from_unit. """
    from_unit = self.from_unit_var.get()
    # Filter dictionary keys that match this from_unit
    possible_to_units = sorted([
      pair[1] for pair in CONVERSION_FACTORS.keys() if pair[0] == from_unit
    ])
    self.to_unit_combo["values"] = possible_to_units

  def perform_conversion(self):
    """ Perform the multiplicative conversion using CONVERSION_FACTORS. """
    from_unit = self.from_unit_var.get()
    to_unit = self.to_unit_var.get()
    val_str = self.value_var.get()

    # Validate
    if not from_unit or not to_unit:
      messagebox.showerror("Error", "Please select both 'from' and 'to' units.")
      return
    
    try:
      value = float(val_str)
    except ValueError:
      messagebox.showerror("Error", "Please enter a valid numeric value.")
      return
    
    # Lookup
    key = (from_unit, to_unit)
    if key not in CONVERSION_FACTORS:
      messagebox.showerror("Error", f"No conversion found for '{from_unit}' to '{to_unit}'.")
      return
    
    factor = CONVERSION_FACTORS[key]
    result = value * factor

    self.result_label.config(text=f"Result: {value} {from_unit} = {result:.4f} {to_unit}")

  def open_manage_window(self):
    """ Open a separate window to add, edit, or remove conversions, and list them. """
    ManageConversionWindow(self)

  def exit_app(self):
    self.destroy()
    sys.exit()
  
class ManageConversionWindow(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.title("Manage Conversions")
    self.geometry("400x400")
    self.parent = parent

    main_frame = ttk.Frame(self, padding=10)
    main_frame.pack(fill="both", expand=True)

    # From unit
    ttk.Label(main_frame, text="From Unit:").grid(row=0, column=0, sticky="w")
    self.from_unit_entry = ttk.Entry(main_frame)
    self.from_unit_entry.grid(row=0, column=1, padx=5, pady=5)

    # To unit
    ttk.Label(main_frame, text="To Unit:").grid(row=1, column=0, sticky="w")
    self.to_unit_entry = ttk.Entry(main_frame)
    self.to_unit_entry.grid(row=1, column=1, padx=5, pady=5)

    # Factor
    ttk.Label(main_frame, text="Factor:").grid(row=2, column=0, sticky="w")
    self.factor_entry = ttk.Entry(main_frame)
    self.factor_entry.grid(row=2, column=1, padx=5, pady=5)

    # Buttons
    add_btn = ttk.Button(main_frame, text="Add/Update", command=self.add_or_update_conversion)
    add_btn.grid(row=3, column=0, padx=5, pady=5)

    remove_btn = ttk.Button(main_frame, text="Remove", command=self.remove_conversion)
    remove_btn.grid(row=3, column=1, padx=5, pady=5)

    list_btn = ttk.Button(main_frame, text="List All", command=self.list_all_conversions)
    list_btn.grid(row=4, column=0, columnspan=2, pady=5)

    # Text area tp show conversions
    self.output_text = tk.Text(main_frame, height=10, width=40)
    self.output_text.grid(row=5, column=0, columnspan=2, pady=5)
  
  def add_or_update_conversion(self):
    """ Add a new (from_unit, to_unit) factor or update if it exists. """
    from_unit = self.from_unit_entry.get().strip().lower()
    to_unit = self.to_unit_entry.get().strip().lower()
    factor_str = self.factor_entry.get().strip()

    if not from_unit or not to_unit or not factor_str:
      messagebox.showerror("Error", "Please fill in all fields.")
      return
    
    try:
      factor = float(factor_str)
    except ValueError:
      messagebox.showerror("Error", "Factor must be a valid number.")
      return
    
    # Update global dictionary
    CONVERSION_FACTORS[(from_unit, to_unit)] = factor

    # For the reverse direction, you might or might not add it automatically.
    # That depends on your design. 
    # e.g. if you want symmetrical conversions, do:
    # CONVERSION_FACTORS[(to_unit, from_unit)] = 1.0 / factor

    messagebox.showinfo("Success", f"Conversion ({from_unit} -> {to_unit}) set to factor {factor}.")

    # Clear fields
    self.from_unit_entry.delete(0, tk.END)
    self.to_unit_entry.delete(0, tk.END)
    self.factor_entry.delete(0, tk.END)

    # Refresh parent's combobox if needed
    all_from_units = sorted(set(pair[0] for pair in CONVERSION_FACTORS.keys()))
    self.parent.from_unit_combo["values"] = list(all_from_units)
  
  def remove_conversion(self):
    """ Remove an existing (from_unit, to_unit) factor. """
    from_unit = self.from_unit_entry.get().strip().lower()
    to_unit = self.to_unit_entry.get().strip().lower()

    key = (from_unit, to_unit)
    if key in CONVERSION_FACTORS:
      del CONVERSION_FACTORS[key]
      messagebox.showinfo("Success", f"Removed conversion for '{from_unit}' -> '{to_unit}'.")
    else:
      messagebox.showerror("Error", f"No conversion found for '{from_unit}' -> '{to_unit}'.")

    # Optionally remove reverse if you added it automatically
    # reverse_key = (to_unit, from_unit)
    # if reverse_key in CONVERSION_FACTORS:
    #     del CONVERSION_FACTORS[reverse_key]

    # Clear fields
    self.from_unit_entry.delete(0, tk.END)
    self.to_unit_entry.delete(0, tk.END)
    self.factor_entry.delete(0, tk.END)

    # Refresh parent's combobox if needed
    all_from_units = sorted(set(pair[0] for pair in CONVERSION_FACTORS.keys()))
    self.parent.from_unit_combo["values"] = list(all_from_units)

  def list_all_conversions(self):
    """ Display all keys and factors in the output_text box. """
    self.output_text.delete("1.0", tk.END)
    self.output_text.insert(tk.END, "All Current Multiplicative Conversions:\n\n")
    for (src, tgt), factor in sorted(CONVERSION_FACTORS.items()):
      self.output_text.insert(tk.END, f"{src} -> {tgt} : {factor}\n")

def main():
  app = UnitConverterApp()
  app.mainloop()

if __name__ == "__main__":
  main()