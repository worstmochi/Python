print("Calculadora Simples")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4 - Divisão")

escolha = input("Operação (1/2/3/4): ")

if escolha == '1':
    print("Resultado:", num1 + num2)
elif escolha == '2':
    print("Resultado:", num1 - num2)
elif escolha == '3':
    print("Resultado:", num1 * num2)
elif escolha == '4':
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: Divisão por zero!")
else:
    print("Operação inválida.")