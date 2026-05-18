import tkinter as tk
from operacoes import somar, subtrair, multiplicacao, divisao

janela = tk.Tk()

janela.title("Calculadora Definitiva")
janela.geometry("300x200")

label = tk.Label(janela, text="Digite um valor")
label.pack()

label1 = tk.Label(janela, text="a")
label1.pack()

def set_texto(valor):
    label1.config(text=valor)

botao1 = tk.Button(janela, text="1", command=lambda: set_texto("1"))
botao1.pack(pady=5)


botao2 = tk.Button(janela, text="2", command=lambda: set_texto("2"))
botao2.pack(pady=5)

janela.mainloop()