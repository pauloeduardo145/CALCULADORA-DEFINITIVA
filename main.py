from operacoes import *
from arquivos import *
from interface import *

historico = ler_historico()

def adicionar_historico(numero1, numero2, operacao, resultado):
        expressao = f"{numero1} {operacao} {numero2} = {resultado}"
        historico.append(expressao)
        salvar_arquivo(historico)

def listar_historico(historico):
    if historico:
        for i, tarefa in enumerate(historico, 1):
            print(f"{i}. {tarefa}")
    else:
            print("Não possui historico")

janela.mainloop()