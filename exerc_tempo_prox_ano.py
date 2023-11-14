import tkinter as tk
import time
import locale

def data_formatada():
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    tempo_atual = time.localtime()
    tempo_ano_novo = (tempo_atual.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)
    segundos_restantes = int(time.mktime(tempo_ano_novo) - time.mktime(tempo_atual))
    #CALCULO DE TEMPO EM SEGUNDOS
    segundos_por_minuto = 60
    segundos_por_hora = 60 * 60
    segundos_por_dia = 24 * 60 * 60
    #CALCULANDO A QUANTIDADE DE DIAS E O RESTO DOS SEGUNDOS
    dias, resto_segundos = divmod(segundos_restantes, segundos_por_dia)
    horas, resto_segundos = divmod(resto_segundos, segundos_por_hora)
    minutos, segundos = divmod(resto_segundos, segundos_por_minuto)
    print(dias)
    print(horas)
    print(minutos)
    print(segundos)
    var_tempo = ("{} dias, {} horas, {} minutos, {} segundos".format(dias, horas, minutos, segundos))
    #tempo_ano_novo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_ano_novo)
    #tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_atual)
    txt_visual.delete("1.0", tk.END)
    txt_visual.insert("1.0", var_tempo) 
    print(tempo_ano_novo)  
    print("TESTE BOTAO DATA")

janela = tk.Tk()

janela.configure(bg="white")
janela.title("Tempo para o proximo Ano")
janela.geometry("320x200")

txt_visual = tk.Text(width=30, height=3, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, wrap=tk.WORD)
txt_visual.grid(row=0, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

botao_data = tk.Button(text="Data atual", width=20, command=data_formatada, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#32CD32', fg='white')
botao_data.grid(row=1, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

janela.mainloop()