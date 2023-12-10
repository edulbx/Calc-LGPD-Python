# LGPD Calculator Python
# using the tkinter library

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg

# Função para validar 
def validate_integer(value, action, field_name):
    if action == '1':  
        try:
            # Tentar converter o valor para int
            int_value = int(value)
            # Verificar se está no intervalo desejado
            if 1 <= int_value <= 100:
                return True
            else:
                msg.showerror("Erro", f"{field_name} deve ser um número inteiro entre 1 e 100.")
                return False
        except ValueError:
            msg.showerror("Erro", f"Por favor, insira um valor numérico inteiro para {field_name}.")
            return False
    return True


# ... (seu código anterior)

# ...

# ... (seu código anterior)

def calculate_penalty():
    revenue_value = float(revenue_value_entry.get())

    # Getting values for agravantes
    reincidencia_especifica = float(espec_value_entry.get()) if espec_value_entry.get() else 0
    reincidencia_generica = float(generic_value_entry.get()) if generic_value_entry.get() else 0
    medida_orientation = float(orientation_descumprida_value_entry.get()) if orientation_descumprida_value_entry.get() else 0
    medida_corretiva = float(corrective_descumprida_value_entry.get()) if corrective_descumprida_value_entry.get() else 0

    # Getting values for mitigantes
    cessacao_infração = float(cessação_combo.get()) if cessação_combo.get() else 0
    politica_boas_praticas = float(bpratica_combo.get()) if bpratica_combo.get() else 0
    implementacao_medidas = float(imple_medidas.get()) if imple_medidas.get() else 0

    # Cálculos
    aggravating_factors = 0
    mitigating_factors = 0

    aggravating_factors += revenue_value * 0.10 * reincidencia_especifica if reincidencia_especifica <= 4 else revenue_value * 0.40
    aggravating_factors += revenue_value * 0.05 * reincidencia_generica if reincidencia_generica <= 4 else revenue_value * 0.20
    aggravating_factors += revenue_value * 0.30 * medida_orientation if medida_orientation <= 3 else revenue_value * 0.90
    aggravating_factors += revenue_value * 0.20 * medida_corretiva

    mitigating_factors += revenue_value * 0.15 * cessacao_infração if cessacao_infração <= 3 else revenue_value * 0.50
    mitigating_factors += revenue_value * 0.25 * politica_boas_praticas if politica_boas_praticas == "Sim" else 0
    mitigating_factors += revenue_value * 0.35 * implementacao_medidas if implementacao_medidas == "casos em que houver cooperação ou boa-fé por parte do infrator." else 0

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
title_label.grid(column=0, row=0,  columnspan=2)

title_label = ttk.Label(container, text="Dados do cliente", font=("Arial", 14))
title_label.grid(column=0, row=1,  columnspan=2)

#Faturamento da empresa
revenue_value_label = ttk.Label(container, text="Faturamento:")
revenue_value_label.grid(column=0, row=2) 

revenue_value_entry = ttk.Entry(container)
revenue_value_entry.grid(column=1, row=2)

title_label = ttk.Label(container, text="Informaçãos sobre a infração", font=("Arial", 14))
title_label.grid(column=0, row=3,  columnspan=2)

#Infração média ou grave
type_infração_label = ttk.Label(container, text= "Média ou Grave:")
type_infração_label.grid(column=0, row=4)
#----valores
type_infração_combo  = ttk.Combobox(container, values=["Média", "Grave"])
type_infração_combo.set("Tipo de infração")
type_infração_combo.grid(column=1, row=4)  

#Nível da infração
level_infração_label = ttk.Label(container, text= "Nível da Infração:")
level_infração_label.grid(column=0, row=5)
#----valores
level_infração_combo  = ttk.Combobox(container, values=["0", "1", "2", "3"])
level_infração_combo.set("Nível da infração")
level_infração_combo.grid(column=1, row=5)  


title_label = ttk.Label(container, text="Agravantes", font=("Arial", 14))
title_label.grid(column=0, row=6,  columnspan=2)


#Quantidade de reincidencia - agravantes
# Especifica
espec_label = ttk.Label(container, text= "Reincidencia especifica:")
espec_label.grid(column=0, row=7)
#----valores
espec_value_entry = ttk.Entry(container)
espec_value_entry.grid(column=1, row=7)
vcmd_reincidencia = (window.register(validate_integer), '%P', '%d', 'Reincidência Específica')
espec_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_reincidencia)
espec_value_entry.grid(column=1, row=7)

# generica
generic_label = ttk.Label(container, text= "Reincidencia especifica:")
generic_label.grid(column=0, row=8)
#----valores
generic_value_entry = ttk.Entry(container)
generic_value_entry.grid(column=1, row=8)
vcmd_reincidencia_generica = (window.register(validate_integer), '%P', '%d', 'Reincidência Genérica')
generic_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_reincidencia_generica)
generic_value_entry.grid(column=1, row=8)


# Medida Orientação ou Preventiva Descumprida
orientation_descumprida_label = ttk.Label(container, text= "Medida Orientação ou Preventiva Descumprida:")
orientation_descumprida_label.grid(column=0, row=9)
#----valores
orientation_descumprida_entry = ttk.Entry(container)
orientation_descumprida_entry.grid(column=1, row=9)
vcmd_orientation_descumprida = (window.register(validate_integer), '%P', '%d', 'Medida Orientação ou Preventiva Descumprida')
orientation_descumprida_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_orientation_descumprida)
orientation_descumprida_value_entry.grid(column=1, row=9)


# Medida Corretiva Descumprida
corrective_descumprida_label = ttk.Label(container, text= "Medida Corretiva Descumprida:")
corrective_descumprida_label.grid(column=0, row=10)
#----valores
corrective_descumprida_value_entry = ttk.Entry(container)
corrective_descumprida_value_entry.grid(column=1, row=10)

vcmd_corrective_descumprida = (window.register(validate_integer), '%P', '%d', 'Medida Corretiva Descumprida')
corrective_descumprida_value_entry = ttk.Entry(container, validate='key', validatecommand=vcmd_corrective_descumprida)
corrective_descumprida_value_entry.grid(column=1, row=10)


title_label = ttk.Label(container, text="Atenuantes", font=("Arial", 14))
title_label.grid(column=0, row=11,  columnspan=2)


#Atenuantes
#Cessação da infração
cessação_label = ttk.Label(container, text= "Cessação da infração:")
cessação_label.grid(column=0, row=12)
#----valores
cessação_combo  = ttk.Combobox(container, values=["cessada antes da instauração do procedimento preparatório da ANPD", 
                                                  "cessada após a instauração do procedimento preparatório e antes da instauração do processo administrativo sancionador;", 
                                                  "cessada após a instauração do processo administrativo sancionador e antes da decisão de primeira instância no âmbito do processo" ])
cessação_combo.set("Marque o nível da infração")
cessação_combo.grid(column=1, row=12)  

#Politica de boas práticas
bpratica_label = ttk.Label(container, text= "Politica de boas práticas:")
bpratica_label.grid(column=0, row=13)
#----valores
bpratica_combo  = ttk.Combobox(container, values=["Sim", "Não"])
bpratica_combo.set("Marque o nível da infração")
bpratica_combo.grid(column=1, row=13) 

#Implementação de Medidas
imple_medidas_label = ttk.Label(container, text= "Implementação de Medidas:")
imple_medidas_label.grid(column=0, row=14)
#----valores
imple_medidas  = ttk.Combobox(container, values=["medidas forem comprovadas antes da instauração do procedimento preparatório ou processo administrativo sancionador pela ANPD;", 
                                                 "medidas forem comprovadas após a instauração do procedimento preparatório e antes da instauração do processo administrativo sancionado", 
                                                 "casos em que houver cooperação ou boa-fé por parte do infrator."])
imple_medidas.set("Marque o nível da infração")
imple_medidas.grid(column=1, row=14) 

#botão para calculo
calculate_button = ttk.Button(container, text="Calculate Penalty", command=calculate_penalty)
calculate_button.grid(column=0, row=15, columnspan=2)

result_label= ttk.Label(container, text="")
result_label.grid(column=1, row=15, columnspan=2)

# Let's start the application window
window.mainloop()
