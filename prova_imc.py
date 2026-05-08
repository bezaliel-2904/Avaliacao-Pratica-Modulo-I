print("*************** Programa para cálculo de 'IMC' ***************")
nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
peso = float(input("Digite seu peso (kg):"))
altura = float(input("Digite sua altura(m):"))
print()
#fórmula do IMC
imc = peso / (altura ** 2)
print(f"\nSeu IMC é:{imc:.2f}")
# Classificação
if imc < 18.5:
        print("Senhor(a)",nome,"seu IMC é: ",imc,",portanto você está 'ABAIXO DO PESO' de acordo com os dados inseridos")
elif imc < 24.9:
        print("Senhor(a)",nome,"seu IMC é: ",imc,",portanto seu peso está 'ADEQUADO' de acordo com os dados inseridos")
elif imc < 29.9:
        print("Senhor(a)",nome,"seu IMC é: ",imc,",portanto você está com 'SOBREPESO' de acordo com os dados inseridos")
elif imc < 34.9:
        print("Senhor(a)",nome,"seu IMC é: ",imc,",portanto você está com 'OBESIDADE DE GRAU 1' de acordo com os dados inseridos")
elif imc < 39.9:
        print("Senhor(a)",nome,"seu IMC é: ",imc,",portanto você está com 'OBESIDADE DE GRAU 2' de acordo com os dados inseridos")
else:
        print("Senhor(a)",nome,"seu IMC é: ",imc,",portanto você está com 'OBESIDADE DE GRAU 3', nível EXTREMO de acordo com a tabela. CUIDE DE SUA SAÚDE")
print()
print("Obrigado por usar nosso programa!!!")
print()
print("Cuide de sua saúde!!!")

