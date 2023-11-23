import tkinter as tk
from datetime import datetime
#
def data_aniversario():
    data_niver1 = txt_data_aniversario.get("1.0", tk.END)
    data_niver = data_niver1.strip()
    #Tratar o campo de data de nascimento caso o usuario nao o preencha
    if data_niver == "":
        txt_visual.delete("1.0", tk.END)
        texto_alerta = "Se faz necessario preencher o campo com a data de nascimento."
        txt_visual.insert("1.0", texto_alerta)
    else:
        pass
    #
    data_nascimento = datetime.strptime(data_niver, "%d/%m/%Y")
    data_nascimento_formatada = data_nascimento.strftime("%d/%m/%Y")
    data_atual = datetime.now()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")
    #Calculo para determinar a idade do usuario
    idade = data_atual.year - data_nascimento.year
    mes_atual = data_atual.month
    dia_atual = data_atual.day
    mes_nascimento = data_nascimento.month
    dia_nascimento = data_nascimento.day
    if mes_nascimento > mes_atual:
        idade -= 1
    elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
        idade -= 1
    #
    texto_final = "Data de nascimento: {}\nData Atual: {}\nIdade: {}".format(data_nascimento_formatada, data_atual_formatada, idade)
    txt_visual.delete("1.0", tk.END)
    txt_visual.insert("1.0", texto_final)
#
janela = tk.Tk()
#
janela.configure(bg="white")
janela.title("Analise Aniversario")
janela.geometry("310x200")

lbl_data = tk.Label(text="Data de Nascimento:", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
lbl_data.grid(row=0, column=0, padx=10, pady=10)

txt_data_aniversario = tk.Text(width=15, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
txt_data_aniversario.grid(row=0, column=1, padx=10, pady=10, columnspan=3, sticky='NSEW')

txt_visual = tk.Text(width=30, height=3, font=('Microsoft YaHei UI light', 10, 'bold'), border=1, wrap=tk.WORD)
txt_visual.grid(row=1, column=0, padx=20, pady=20, columnspan=4, sticky='NSEW')

botao_data = tk.Button(text="Data atual", width=20, command=data_aniversario, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#32CD32', fg='white')
botao_data.grid(row=2, column=0, padx=20, pady=20, columnspan=4, sticky='NSEW')

janela.mainloop()