# LGPD Calculator Python
# using the tkinter library

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg

# Func to validate data input
def validate_integer(value, action, field_name):
    if action == '1':  
        try:
            # Try to convert the value to int
            int_value = int(value)
            # Set the range
            if 1 <= int_value <= 100:
                return True
            else:
                msg.showerror("Error", f"{field_name} needs to be an Integer between 1 and 100.")
                return False
        except ValueError:
            msg.showerror("Error", f"Please enter a number for {field_name}.")
            return False
    return True

def calculate_penalty():
    revenue_value = float(revenue_value_entry.get())

    # Getting values for aggravating
    specific_recidivism = float(espec_value_entry.get()) if espec_value_entry.get() else 0
    generic_recidivism = float(generic_value_entry.get()) if generic_value_entry.get() else 0
    orientation_measure = float(orientation_disobeyed_value_entry.get()) if orientation_disobeyed_value_entry.get() else 0
    corrective_measure = float(corrective_disobeyed_value_entry.get()) if corrective_disobeyed_value_entry.get() else 0

    # Getting values for mitigating
    cessation_infraction = cessation_combo.get() if cessation_combo.get() else "None"
    good_practices_policy = good_practices_combo.get() if good_practices_combo.get() else "None"
    implementation_measures = imple_measures.get() if imple_measures.get() else "None"

    # Additional factor for medium or severe infraction
    infraction_type = type_infraction_combo.get()
    infraction_factor = 0.10 if infraction_type == "Medium" else 0.20

    # Calculations
    aggravating_factors = 0
    mitigating_factors = 0

    # Aggravating
    aggravating_factors += revenue_value * infraction_factor  # Medium or Severe Infraction
    aggravating_factors += revenue_value * 0.10 * specific_recidivism if specific_recidivism <= 4 else revenue_value * 0.40
    aggravating_factors += revenue_value * 0.05 * generic_recidivism if generic_recidivism <= 4 else revenue_value * 0.20
    aggravating_factors += revenue_value * 0.30 * orientation_measure if orientation_measure <= 3 else revenue_value * 0.90
    aggravating_factors += revenue_value * 0.20 * corrective_measure

    # Mitigating
    if cessation_infraction == "ceased before the initiation of the preparatory procedure by ANPD":
        mitigating_factors += revenue_value * 0.75
    elif cessation_infraction == "ceased after the initiation of the preparatory procedure and before the initiation of the administrative sanctioning process":
        mitigating_factors += revenue_value * 0.50
    elif cessation_infraction == "ceased after the initiation of the administrative sanctioning process and before the decision of the first instance within the process":
        mitigating_factors += revenue_value * 0.30

    if good_practices_policy == "Yes":
        mitigating_factors += revenue_value * 0.20

    if implementation_measures == "measures are proven before the initiation of the preparatory procedure or administrative sanctioning process by ANPD;":
        mitigating_factors += revenue_value * 0.20
    elif implementation_measures == "measures are proven after the initiation of the preparatory procedure and before the initiation of the administrative sanctioning process":
        mitigating_factors += revenue_value * 0.10
    elif implementation_measures == "cases where there is cooperation or good faith on the part of the offender.":
        mitigating_factors += revenue_value * 0.05

    penalty = revenue_value * (1 + aggravating_factors - mitigating_factors)
    result_label.config(text=f"Penalty value: R$ {penalty:.2f}")

# Let's create the main window
window = tk.Tk()
window.title("LGPD Penalty Calculator")

# Let's create and configure the container:
container = ttk.Frame(window, padding=50)
container.pack()

# Let's create the interface elements
title_label = ttk.Label(container, text="LGPD Penalty Calculator", font=("Arial", 14))
title_label.grid(column=0, row=0, columnspan=2)

title_label = ttk.Label(container, text="Client Data", font=("Arial", 14))
title_label.grid(column=0, row=1, columnspan=2)

# Company Revenue
revenue_value_label = ttk.Label(container, text="Revenue:")
revenue_value_label.grid(column=0, row=2) 

revenue_value_entry = ttk.Entry(container)
revenue_value_entry.grid(column=1, row=2)

title_label = ttk.Label(container, text="Information about the infraction", font=("Arial", 14))
title_label.grid(column=0, row=3, columnspan=2)

# Medium or Severe Infraction
type_infraction_label = ttk.Label(container, text="Medium or Severe:")
type_infraction_label.grid(column=0, row=4)

type_infraction_combo = ttk.Combobox(container, values=["Medium", "Severe"])
type_infraction_combo.set("Infraction Type")
type_infraction_combo.grid(column=1, row=4)  

# Infraction Level
level_infraction_label = ttk.Label(container, text="Infraction Level:")
level_infraction_label.grid(column=0, row=5)

level_infraction_combo = ttk.Combobox(container, values=["0", "1", "2", "3"])
level_infraction_combo.set("Infraction Level")
level_infraction_combo.grid(column=1, row=5)  

title_label = ttk.Label(container, text="Aggravating Factors", font=("Arial", 14))
title_label.grid(column=0, row=6, columnspan=2)

# Quantity of Recidivism - Aggravating
# Specific
espec_label = ttk.Label(container, text="Specific Recidivism:")
espec_label.grid(column=0, row=7)

espec_value_entry = ttk.Entry(container)
espec_value_entry.grid(column=1, row=7)
vcmd_reincidencia = (window.register(validate_integer), '%P', '%d', 'Specific Recidivism')
espec_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_reincidencia)
espec_value_entry.grid(column=1, row=7)

# Generic
generic_label = ttk.Label(container, text="Generic Recidivism:")
generic_label.grid(column=0, row=8)

generic_value_entry = ttk.Entry(container)
generic_value_entry.grid(column=1, row=8)
vcmd_reincidencia_generica = (window.register(validate_integer), '%P', '%d', 'Generic Recidivism')
generic_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_reincidencia_generica)
generic_value_entry.grid(column=1, row=8)

# Failure to Comply with Orientation or Preventive Measure
orientation_disobeyed_label = ttk.Label(container, text="Failure to Comply with Orientation or Preventive Measure:")
orientation_disobeyed_label.grid(column=0, row=9)

orientation_disobeyed_entry = ttk.Entry(container)
orientation_disobeyed_entry.grid(column=1, row=9)
vcmd_orientation_disobeyed = (window.register(validate_integer), '%P', '%d', 'Failure to Comply with Orientation or Preventive Measure')
orientation_disobeyed_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_orientation_disobeyed)
orientation_disobeyed_value_entry.grid(column=1, row=9)

# Failure to Comply with Corrective Measure
corrective_disobeyed_label = ttk.Label(container, text="Failure to Comply with Corrective Measure:")
corrective_disobeyed_label.grid(column=0, row=10)

corrective_disobeyed_value_entry = ttk.Entry(container)
corrective_disobeyed_value_entry.grid(column=1, row=10)

vcmd_corrective_disobeyed = (window.register(validate_integer), '%P', '%d', 'Failure to Comply with Corrective Measure')
corrective_disobeyed_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_corrective_disobeyed)
corrective_disobeyed_value_entry.grid(column=1, row=10)

title_label = ttk.Label(container, text="Mitigating Factors", font=("Arial", 14))
title_label.grid(column=0, row=11, columnspan=2)

# Mitigating
# Cessation of the Infraction
cessation_label = ttk.Label(container, text="Cessation of the Infraction:")
cessation_label.grid(column=0, row=12)

cessation_combo = ttk.Combobox(container, values=[
    "ceased before the initiation of the preparatory procedure by ANPD",
    "ceased after the initiation of the preparatory procedure and before the initiation of the administrative sanctioning process",
    "ceased after the initiation of the administrative sanctioning process and before the decision of the first instance within the process"
])
cessation_combo.set("Mark the infraction level")
cessation_combo.grid(column=1, row=12)  

# Good Practices Policy
good_practices_label = ttk.Label(container, text="Good Practices Policy:")
good_practices_label.grid(column=0, row=13)

good_practices_combo = ttk.Combobox(container, values=["Yes", "No"])
good_practices_combo.set("Mark the infraction level")
good_practices_combo.grid(column=1, row=13) 

# Implementation of Measures
imple_measures_label = ttk.Label(container, text="Implementation of Measures:")
imple_measures_label.grid(column=0, row=14)

imple_measures = ttk.Combobox(container, values=[
    "measures are proven before the initiation of the preparatory procedure or administrative sanctioning process by ANPD;",
    "measures are proven after the initiation of the preparatory procedure and before the initiation of the administrative sanctioning process",
    "cases where there is cooperation or good faith on the part of the offender."
])
imple_measures.set("Mark the infraction level")
imple_measures.grid(column=1, row=14) 

# Button for calculation
calculate_button = ttk.Button(container, text="Calculate Penalty", command=calculate_penalty)
calculate_button.grid(column=0, row=15, columnspan=2)

result_label= ttk.Label(container, text="")
result_label.grid(column=1, row=15, columnspan=2)

# Let's start the application window
window.mainloop()
