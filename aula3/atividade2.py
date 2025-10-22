# 1. 📊 Comparação entre dois valores numéricos
x = float(input("Informe o valor X: "))
y = float(input("Informe o valor Y: "))

if x > y:
    print(f"Valor {x} é maior que valor {y}")
elif x < y:
    print(f"Valor {x} é menor que valor {y}")
else:
    print("Os valores de X e Y são iguais")

# 2. 📝 Comparação entre dois textos
texto1 = input("Informe o primeiro texto: ")
texto2 = input("Informe o segundo texto: ")

if texto1 == texto2:
    print("Os valores informados são iguais")
else:
    print(f"Valor '{texto1}' é diferente do valor '{texto2}'")

# 3. 👶👨🧓 Verificação de idade
idade = int(input("Informe sua idade: "))

if idade < 18:
    print("Você é menor de idade")
elif idade < 60:
    print("Você é adulto")
else:
    print("Você é idoso")

# 4. 🔁 Loop for de 1 a 10
print("Loop for de 1 até 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 5. 🔄 Loop while de 1 a 10
print("Loop while de 1 até 10:")
contador = 1
while contador <= 10:
    print(contador, end=" ")
    contador += 1
print()

# 6. 📚 Dicionário com chave, valor e índice
dados = {'a': 'primeiro', 'b': 'segundo', 'c': 'terceiro', 'd': 'quarto', 'e': 'quinto'}

print("Índice | Chave | Valor")
for indice, (chave, valor) in enumerate(dados.items()):
    print(f"{indice}      | {chave}     | {valor}")

# 7. 🧮 Filtrar e imprimir valores específicos em ordem
numeros = [9, 25, 5, 6, 5815, 985, 1, 22, 2, 7, 3]
valores_desejados = [1, 2, 5, 6]

# Criar nova lista contendo apenas os valores desejados e na ordem certa
resultado = [valor for valor in valores_desejados if valor in numeros]

print("Valores filtrados:", resultado)
