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

    container = tk.Frame(janela, padx=20, pady=20)
    container.pack()

    #vamos criar os elementos da interface

    titulo_label = tk.Label(container, text="Caulculadora de Multas da LGPD", font=("Arial", 14))
    titulo_label.pack()

    valor_base_label = tk.Label(container,text="Valor=base da Multa:")
    valor_base_label.pack()

    valor_base_entry = tk.Entry(container)
    valor_base_entry.pack()

    agravantes_label = tk.Label(container, text= "agravantes:")
    agravantes_label.pack()

    agravantes_combo  = ttk.Combobox(container, value=["1.00", "2.00", "3.00"])
    agravantes_combo.set("1.00")
    agravantes_combo.pack()   
    
    atenuantes_label = tk.Label(container, text="atenuantes:")
    atenuantes_label.pack()
    
    atenuantes_combo = ttk.Combobox(container, values=["1.00", "2.00", "3.00"])
    atenuantes_combo.set("1.00")
    atenuantes_combo.set

    calcular_button = tk.Button(container, text="Calcular Multa", command=calcular_multa)
    calcular_button.pack()

    resultado_label= tk.Label(container, text="")
    resultado_label.pack()

    #vamor iniciar a janela da aplicação
    janela.mainloop()
                            

