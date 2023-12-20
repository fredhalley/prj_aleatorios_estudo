import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import requests
import json
#Lista de Moedas configuradas
moedas = [("USD-BRL", "Dolar Americano"), 
          ("EUR-BRL", "Euro"), 
          ("GBP-BRL", "Libra Esterlina"), 
          ("ARS-BRL", "Peso Argentino"),
          ("BTC-BRL", "Bitcoin/Real"),
          ("LTC-BRL", "Litecoin/Real"),
          ("JPY-BRL", "Iene Japonês"),
          ("CHF-BRL", "Franco Suiço"),
          ("CNY-BRL", "Yuan Chinês"),
          ("ETH-BRL", "Ethereum")
]
#
def converter_moeda():
    entry_resultado.delete("1.0", tk.END)
    valor_conversao1 = entry_valor_moeda_1.get()
    valor_conversao = valor_conversao1.strip()
    moeda_conversao1 = combobox.get()
    moeda_conversao = moeda_conversao1.strip()    
    for codigo, nome in moedas:
        if nome == moeda_conversao:
            moeda_conversao = nome
            codigo_moeda = codigo
            break
    else:
        moeda_conversao = "Não selecionada"
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/{}' .format(codigo_moeda))
    cotacoes_dic = cotacoes.json()
    moeda_alt = codigo_moeda.replace("-", "")
    valor_conversao = valor_conversao.replace(",", ".")
    bid = cotacoes_dic[moeda_alt]['bid']
    valor_convertido = float(valor_conversao) / float(bid)
    texto_final = ("Valor a converter: R${:.2f}\nMoeda Selecionada: {}\nValor da Moeda: {:.2f}\n\nValor Convertido: {:.2f}".format(float(valor_conversao), moeda_conversao, float(bid), float(valor_convertido)))
    entry_resultado.insert("1.0", texto_final)
    print("Conversor de Moedas")

# Criar a janela principal
root = tk.Tk()
#Configuração da tela principal
root.configure(bg="white")
root.title("API - Conversor de Moeda")
root.geometry("325x300")
#Label da aplicação da tela principal
label_moeda_1 = tk.Label(root, text="Valor em Real:", bg="white")
label_moeda_1.grid(row=0, column=0, padx=10, pady=10,sticky='NSEW')
label_moeda_2 = tk.Label(root, text="Converter para:", bg="white")
label_moeda_2.grid(row=1, column=0, padx=10, pady=10,sticky='NSEW')
#Campos de texto da tela principal
entry_valor_moeda_1 = tk.Entry(root, width=30)
entry_valor_moeda_1.grid(row=0, column=1, padx=10, pady=10, sticky='NSEW')
#Combobox para uma lista no formato de tupla
combobox = ttk.Combobox(root, values=[item[1] for item in moedas])
combobox.grid(row=1, column=1, padx=10, pady=10,sticky='NSEW')
combobox.current(0)
#Botão para conversão da tela principal
btn_converter = tk.Button(root, text="Converter Moeda", command=converter_moeda, border=0)
btn_converter.grid(row=2, column=0, padx=10, pady=10, sticky='NSEW', columnspan=2)
#Campo de Texto para apresentar o resultado na tela principal
entry_resultado = scrolledtext.ScrolledText(root, width=10, height=5, font=('Microsoft YaHei UI light', 10, 'bold'))
entry_resultado.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='NSEW')

# Iniciar o loop principal
root.mainloop()