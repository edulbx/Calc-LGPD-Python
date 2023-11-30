#calculadora lgpd python
#exemplo simples usando a biblioteca tkinter

import tkinter as tk
from tkinter import ttk

def calcular_multa():
    valor_base = float(valor_base_entry.get())
    agravantes = float(agravantes_combo.get())
    atenuantes = float(atenuantes_combo.get())

    multa =  valor_base * (1 + agravantes - atenuantes)

    resultado_label.config(text=f"valor da Multa: R$ {multa:.2f}")

#vamos criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de multas da LGPD")

#vamos criar e configurar o container: 
container = ttk.Frame(janela, padding=20)
container.pack()

#vamos criar os elementos da interface
titulo_label = ttk.Label(container, text="Caulculadora de Multas da LGPD", font=("Arial", 14))
titulo_label.grid(column=0, row=0,  columnspan=2)

valor_base_label = ttk.Label(container,text="Valor base da Multa:")
valor_base_label.grid(column=0, row=1)

valor_base_entry = ttk.Entry(container)
valor_base_entry.grid(column=1, row=1)

agravantes_label = ttk.Label(container, text= "Agravantes:")
agravantes_label.grid(column=0, row=2)

agravantes_combo  = ttk.Combobox(container, value=["1.00", "2.00", "3.00"])
agravantes_combo.set("1.00")
agravantes_combo.grid(column=1, row=2)   
    
atenuantes_label = ttk.Label(container, text="Atenuantes:")
atenuantes_label.grid(column=0, row=3)
    
atenuantes_combo = ttk.Combobox(container, values=["1.00", "2.00", "3.00"])
atenuantes_combo.set("1.00")
atenuantes_combo.grid(column=1, row=3)

calcular_button = ttk.Button(container, text="Calcular Multa", command=calcular_multa)
calcular_button.grid(column=0, row=4, columnspan=2)

resultado_label= ttk.Label(container, text="")
resultado_label.grid(column=0, row=5, columnspan=2)

#vamor iniciar a janela da aplicação
janela.mainloop()
    


                            

