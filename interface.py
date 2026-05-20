import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Definitiva")
janela.configure(bg="black")

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

campo = tk.Entry(janela,font=("Arial", 20),justify="right")
campo.grid(columnspan=4,column=0, row=0, padx=10, pady=10,sticky="we")

#PRIMERA CAMADA

barra = tk.Button(janela, text="/", width=5, height=2, bg="orange",fg="white", activebackground="orange",activeforeground="white",relief="flat",bd=0)
barra.grid(column=3, row=1, padx=10, pady=10)

porc = tk.Button(janela, text="%", width=5, height=2, bg="#3b3b3b",fg="white", activebackground="#3b3b3b",activeforeground="white",relief="flat",bd=0)
porc.grid(column=2, row=1, padx=10, pady=10)

c = tk.Button(janela, text="C", width=5, height=2, bg="#3b3b3b",fg="white", activebackground="#3b3b3b",activeforeground="white",relief="flat",bd=0)
c.grid(column=1,row=1, padx=10, pady=10)

ce = tk.Button(janela, text="CE", width=5, height=2, bg="#3b3b3b",fg="white", activebackground="#3b3b3b",activeforeground="white",relief="flat",bd=0)
ce.grid(column=0,row=1, padx=10, pady=10)

#SEGUNDA CAMADA

vezes = tk.Button(janela, text="X", width=5, height=2, bg="orange",fg="white", activebackground="orange",activeforeground="white",relief="flat",bd=0)
vezes.grid(column=3,row=2, padx=10, pady=10)

nove = tk.Button(janela, text="9", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
nove.grid(column=2,row=2, padx=10, pady=10)

oito = tk.Button(janela, text="8", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
oito.grid(column=1,row=2, padx=10, pady=10)

sete = tk.Button(janela, text="7", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
sete.grid(column=0,row=2, padx=10, pady=10)

#TERCEIRA CAMADA  

menos = tk.Button(janela, text="-", width=5, height=2,bg="orange",fg="white", activebackground="orange",activeforeground="white",relief="flat",bd=0)
menos.grid(column=3,row=3, padx=10, pady=10)

seis = tk.Button(janela, text="6", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
seis.grid(column=2,row=3, padx=10, pady=10)

cinco = tk.Button(janela, text="5", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
cinco.grid(column=1,row=3, padx=10, pady=10)

quatro = tk.Button(janela, text="4", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
quatro.grid(column=0,row=3, padx=10, pady=10)

#TERCEIRA CAMADA

mais = tk.Button(janela, text="+", width=5, height=2,bg="orange",fg="white", activebackground="orange",activeforeground="white",relief="flat",bd=0)
mais.grid(column=3,row=4, padx=10, pady=10)

tres = tk.Button(janela, text="3", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
tres.grid(column=2,row=4, padx=10, pady=10)

dois = tk.Button(janela, text="2", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
dois.grid(column=1,row=4, padx=10, pady=10)

um = tk.Button(janela, text="1", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
um.grid(column=0,row=4, padx=10, pady=10)

#QUARTA CAMADA

soma = tk.Button(janela, text="=", width=5, height=2,bg="orange",fg="white", activebackground="orange",activeforeground="white",relief="flat",bd=0)
soma.grid(column=3,row=5, padx=10, pady=10)

ponto = tk.Button(janela, text=".", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
ponto.grid(column=2,row=5, padx=10, pady=10)

zero = tk.Button(janela, text="0", width=5, height=2,bg="#2d2d2d",fg="white", activebackground="#2d2d2d",activeforeground="white",relief="flat",bd=0)
zero.grid(columnspan=2,column=0,row=5, padx=5, pady=10,sticky="we")


janela.mainloop()