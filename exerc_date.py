import tkinter as tk
from datetime import datetime, timedelta

def data_formatada():
    dias = txt_dias.get("1.0", tk.END)

    try:
        dias1 = int(dias)
    except ValueError:        
        erro = "Por favor, insira um valor inteiro valido."
        txt_visual.delete("1.0", tk.END)
        txt_visual.insert("1.0", erro)
        return

    data_atual = datetime.now()
    data_futura = data_atual + timedelta(days=int(dias))
    data_passado = data_atual - timedelta(days=int(dias))
    format_texto = ("Data atual: {}\nData Futuro: {}\nData Passado: {}".format(data_atual.date(), data_futura.date(), data_passado.date()))
    txt_visual.delete("1.0", tk.END)
    txt_visual.insert("1.0", format_texto)
    print("Data Formatada")

janela = tk.Tk()

janela.configure(bg="white")
janela.title("Teste da Biblioteca DATE")
janela.geometry("300x225")

txt_dias = tk.Text(width=10, height=1, font=('Microsoft YaHei UI light', 10, 'bold'), border=1, wrap=tk.WORD)
txt_dias.grid(row=0, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

txt_visual = tk.Text(width=30, height=3, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, wrap=tk.WORD)
txt_visual.grid(row=1, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

botao_data = tk.Button(text="Data atual", width=20, command=data_formatada, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#32CD32', fg='white')
botao_data.grid(row=2, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

texto_padrao = 10
txt_dias.insert("1.0", texto_padrao)

janela.mainloop()