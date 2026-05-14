from operacoes import somar, subtrair, multiplicacao, divisao
from arquivos import ler_historico, salvar_arquivo

historico = ler_historico()
while True:
    print("Calculadora em PYTHON")
    print("Operações utilizaveis: +, -, *, /")

    print("1. Somar")
    print("2. Sair")

    opcao = input("Escolha...")

    if opcao == "1":
        numero1 = float(input("Digite o primeiro numero: "))
        operacao = input("Digite a operação: ")
        numero2 = float(input("Digite o segundo numero: "))
        salvar_arquivo(historico)
        
        if operacao == "+":
            print("Resultado:", somar(numero1, numero2))
        elif operacao == "-":
            print("Resultado:", subtrair(numero1, numero2))
        elif operacao == "*":
            print("Resultado:", multiplicacao(numero1, numero2))
        elif operacao == "/":
            print("Resultado:", divisao(numero1, numero2))
        else:
            print("Operação invalida!")

    elif opcao == "2":
        salvar_arquivo(historico)
        break
    

def adicionar_historico():
        historico.append(ler_historico())

def listar_historico():
    if historico:
        for i, tarefa in enumerate(historico, 1):
            print(f"{i}. {tarefa}")
    else:
            print("Não possui historico")