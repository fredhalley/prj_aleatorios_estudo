import tkinter as tk
import time
import locale

def data_formatada():
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    tempo_em_struct = time.localtime()
    tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_em_struct)
    txt_visual.delete("1.0", tk.END)
    txt_visual.insert("1.0", tempo_formatado.encode('utf-8').decode('utf-8'))   
    #print("TESTE BOTAO DATA")

janela = tk.Tk()

#janela.configure(bg="white")
janela.title("Formatação de tempo")
janela.geometry("300x200")

txt_visual = tk.Text(width=30, height=3, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, wrap=tk.WORD)
txt_visual.grid(row=0, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

botao_data = tk.Button(text="Data atual", width=20, command=data_formatada, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#32CD32', fg='white')
botao_data.grid(row=1, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

janela.mainloop()