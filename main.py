from operacoes import somar, subtrair, multiplicacao, divisao

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