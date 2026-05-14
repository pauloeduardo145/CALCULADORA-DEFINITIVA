from operacoes import somar, subtrair, multiplicacao, divisao
from arquivos import ler_historico, salvar_arquivo

historico = ler_historico()

while True:

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



    print("Calculadora em PYTHON")
    print("Operações utilizaveis: +, -, *, /")

    print(historico)

    print("1. Somar")
    print("2. Sair")

    opcao = input("Escolha...")

    if opcao == "1":

        resultado = None

        numero1 = float(input("Digite o primeiro numero: "))
        operacao = input("Digite a operação: ")
        numero2 = float(input("Digite o segundo numero: "))

        if operacao == "+":
            resultado = somar(numero1, numero2)
            print("Resultado:", resultado)
            salvar_arquivo(historico)
        elif operacao == "-":
            resultado = subtrair(numero1, numero2)
            print("Resultado:", resultado)
            salvar_arquivo(historico)
        elif operacao == "*":
            resultado = multiplicacao(numero1, numero2)
            print("Resultado:", resultado)
            salvar_arquivo(historico)            
        elif operacao == "/":
            resultado = divisao(numero1, numero2)
            print("Resultado:", resultado)
            salvar_arquivo(historico)
        else:
            print("Operação invalida!")
        
        adicionar_historico(numero1, numero2, operacao, resultado)
        listar_historico(historico)



    elif opcao == "2":
        print("Vai salvar...", historico)
        salvar_arquivo(historico)
        break
    

