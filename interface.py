import tkinter as tk

janela = tk.Tk()

janela.title("Interface")
janela.geometry("300x200")

Entry()

label = tk.Label(janela, text="Olá, Mundo")
label.pack()

janela.mainloop()