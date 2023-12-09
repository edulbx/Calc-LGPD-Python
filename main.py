# LGPD Calculator Python
# using the tkinter library

import tkinter as tk
from tkinter import ttk

def calculate_penalty():
    base_value = float(base_value_entry.get())
    aggravating_factors = float(aggravating_combo.get())
    mitigating_factors = float(mitigating_combo.get())

    penalty =  base_value * (1 + aggravating_factors - mitigating_factors)

    result_label.config(text=f"Penalty value: R$ {penalty:.2f}")

# Let's create the main window
window = tk.Tk()
window.title("LGPD Penalty Calculator")

# Let's create and configure the container:
container = ttk.Frame(window, padding=20)
container.pack()

# Let's create the interface elements
title_label = ttk.Label(container, text="LGPD Penalty Calculator", font=("Arial", 14))
title_label.grid(column=0, row=0,  columnspan=2)

base_value_label = ttk.Label(container, text="Base Penalty Value:")
base_value_label.grid(column=0, row=1)

base_value_entry = ttk.Entry(container)
base_value_entry.grid(column=1, row=1)

aggravating_label = ttk.Label(container, text= "Aggravating Factors:")
aggravating_label.grid(column=0, row=2)

aggravating_combo  = ttk.Combobox(container, values=["1.00", "2.00", "3.00"])
aggravating_combo.set("1.00")
aggravating_combo.grid(column=1, row=2)   
    
mitigating_label = ttk.Label(container, text="Mitigating Factors:")
mitigating_label.grid(column=0, row=3)
    
mitigating_combo = ttk.Combobox(container, values=["1.00", "2.00", "3.00"])
mitigating_combo.set("1.00")
mitigating_combo.grid(column=1, row=3)

calculate_button = ttk.Button(container, text="Calculate Penalty", command=calculate_penalty)
calculate_button.grid(column=0, row=4, columnspan=2)

result_label= ttk.Label(container, text="")
result_label.grid(column=0, row=5, columnspan=2)

# Let's start the application window
window.mainloop()
