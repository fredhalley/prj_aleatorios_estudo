import tkinter as tk
from datetime import datetime

def finalizar_venda():
    desconto = 0
    nome1 = txt_nome_cliente.get("1.0", tk.END)
    nome = nome1.strip()
    valor1 = txt_valor_produto.get("1.0", tk.END)
    valor = valor1.strip()
    #VALIDADOR DO CAMPO txt_valor_produto PARA VERIFICAR SE SAO APENAS NUMEROS
    try:
        valor = int(valor)
    except ValueError:
        txt_venda.delete("1.0", "end")
        texto_final = "Por favor, insira um valor inteiro valido."
        txt_venda.insert("1.0", texto_final)
        return
    #
    ultima_compra = datetime(2023, 11, 10)
    data_atual = datetime.now()
    diferenca = data_atual - ultima_compra

    if int(diferenca.days) >= 30:
        desconto = 9
        valor_final = valor - ((valor * desconto) / 100)
        texto_final = "Cliente: {}\nDesconto: {}%\nValor do produto: {}\nValor com desconto: {}" .format(nome, desconto, valor, valor_final)
        txt_venda.insert("1.0", texto_final)
    else:
        valor_final = valor - ((valor * desconto) / 100)
        texto_final = "Cliente: {}\nDesconto: {}%\nValor do produto: {}\nValor com desconto: {}" .format(nome, desconto, valor, valor_final)
        txt_venda.insert("1.0", texto_final)

def limpar_campos():
    txt_nome_cliente.delete("1.0", "end")
    txt_valor_produto.delete("1.0", "end")
    txt_venda.delete("1.0", "end")

janela = tk.Tk()

janela.configure(bg="white")
janela.title("Comparação de datas da ultima compra do cliente com atual")
janela.geometry("420x310")

lb_nome = tk.Label(text="Nome do cliente:", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
lb_nome.grid(row=0, column=0, padx=10, pady=10, columnspan=1, sticky='NSEW')

txt_nome_cliente = tk.Text(width=30, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
txt_nome_cliente.grid(row=0, column=1, padx=10, pady=10, columnspan=3, sticky='NSEW' )

lb_valor_produto = tk.Label(text="Valor do produto:", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
lb_valor_produto.grid(row=1, column=0, padx=10, pady=10, columnspan=1, sticky='NSEW')

txt_valor_produto = tk.Text(width=10, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
txt_valor_produto.grid(row=1, column=1, padx=10, pady=10, columnspan=1, sticky='NSEW' )

txt_venda = tk.Text(width=30, height=5, font=('Microsoft YaHei UI light', 10, 'bold'))
txt_venda.grid(row=2, column=0, padx=10, pady=10, columnspan=4, sticky='NSEW' )

botao_final_venda = tk.Button(text="Finalizar Venda", width=10, command=finalizar_venda, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#57a1f8', fg='white')
botao_final_venda.grid(row=3, column=0, padx=10, pady=10, columnspan=4, sticky='NSEW')

botao_limpar_campos = tk.Button(text="Limpar Campos", width=10, command=limpar_campos, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#57a1f8', fg='white')
botao_limpar_campos.grid(row=4, column=0, padx=10, pady=10, columnspan=4, sticky='NSEW')

janela.mainloop()