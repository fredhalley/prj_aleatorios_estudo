import tkinter as tk
import keyboard
import time
import pygetwindow as gw

def ativar_janela_firefox():
    firefox_window = gw.getWindowsWithTitle("Mozilla Firefox")
    if firefox_window:
        firefox_window[0].activate()

def hashtag_treinamento():
    try:
        ativar_janela_firefox()
        keyboard.press_and_release("ctrl + t")
        time.sleep(1)
        keyboard.write("https://portalhashtag.com/")
        keyboard.press_and_release("enter")
        feedback_label.config(text="HASHTAG TREINAMENTOS realizado com sucesso.")
    except Exception as e:
        feedback_label.config(text=f"Erro: {str(e)}")

def youtube_videos():
    try:
        ativar_janela_firefox()
        keyboard.press_and_release("ctrl + t")
        time.sleep(1)    
        keyboard.write("https://www.youtube.com/watch?v=VKp-K8Mem_I")
        keyboard.press_and_release("enter")
        feedback_label.config(text="YOUTUBE VIDEOS realizado com sucesso.")
    except Exception as e:
        feedback_label.config(text=f"Erro: {str(e)}")

janela = tk.Tk()

janela.configure(bg="white")
janela.title("Biblioteca KEYBOARD")
janela.geometry("225x200")

botao_hashtag = tk.Button(text="HASHTAG TREINAMENTO", width=20, command=hashtag_treinamento, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#32CD32', fg='white')
botao_hashtag.grid(row=1, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

botao_youtube = tk.Button(text="YOUTUBE VIDEOS", width=20, command=youtube_videos, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#32CD32', fg='white')
botao_youtube.grid(row=2, column=0, padx=20, pady=20, columnspan=3, sticky='NSEW')

feedback_label = tk.Label(text="", fg="red")
feedback_label.grid(row=3, column=0, columnspan=3, pady=10)

janela.mainloop()
