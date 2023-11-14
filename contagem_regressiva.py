import tkinter as tk
import time

def contagem_regressiva():
    tempo1 = txt_tempo.get("0.0", tk.END)
    tempo = tempo1.strip()

    try:
        tempo = int(tempo)
    except ValueError:
        print("Por favor, insira um valor inteiro valido.")
        return

    for numero in range(int(tempo), -1, -1):
        txt_contador.delete("1.0", "end")
        txt_contador.insert("0.0", numero)     
        janela.update()   
        print(numero)
        time.sleep(1)

    #print(tempo)
    print("Contagem Regressiva")

def zerar_campo():
    txt_tempo.delete("1.0", tk.END)
    txt_contador.delete("1.0", tk.END)
    print("Zerar campos")

janela = tk.Tk()

janela.configure(bg="white")
janela.title("Contagem Regressiva")
janela.geometry("200x300")

lb_tempo = tk.Label(text="Tempo em segundos", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
lb_tempo.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW')

txt_tempo = tk.Text(width=10, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
txt_tempo.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW' )

lb_0 = tk.Label(text="", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
lb_0.grid(row=2, column=1, padx=10, pady=10)

txt_contador = tk.Text(width=3, height=1, font=('Microsoft YaHei UI light', 30, 'bold'), border=0)
txt_contador.grid(row=2, column=2, padx=10, pady=10, columnspan=3, sticky='NSEW')

botao_timer = tk.Button(text="Iniciar Contagem", width=10, command=contagem_regressiva, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#57a1f8', fg='white')
botao_timer.grid(row=7, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW')

botao_timer = tk.Button(text="Limpar Campos", width=10, command=zerar_campo, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#57a1f8', fg='white')
botao_timer.grid(row=8, column=0, padx=10, pady=10, columnspan=3, sticky='NSEW')

texto_padrao = 5
txt_tempo.insert("1.0", texto_padrao)

janela.mainloop()