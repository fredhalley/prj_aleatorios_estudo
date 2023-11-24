import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_grafico():
    # Seus dados
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Criar o gráfico
    plt.plot(x, y)
    plt.title('Exemplo de Gráfico')

    # Criar a tela Tkinter
    janela_grafico = tk.Toplevel(root)
    janela_grafico.title('Gráfico Matplotlib em Tkinter')

    # Incorporar o gráfico na interface gráfica Tkinter
    canvas = FigureCanvasTkAgg(plt.gcf(), master=janela_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Criar a janela principal Tkinter
root = tk.Tk()
root.title("Exemplo Matplotlib em Tkinter")

# Botão para plotar o gráfico
botao_plotar = tk.Button(root, text="Plotar Gráfico", command=plot_grafico)
botao_plotar.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
