def operacoes():
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def divisao(a, b):
        if b == 0:
            print("Erro: Divisão por zero")
        return a / b
    
    def multiplicacao(a, b):
        return a * b

    print("Calculadora em PYTHON")
    print("Operações utilizaveis: +, -, *, /")

    numero1 = float(input("Digite o primeiro numero: "))
    operacao = input("Digite a operação: ")
    numero2 = float(input("Digite o segundo numero: "))

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

operacoes()