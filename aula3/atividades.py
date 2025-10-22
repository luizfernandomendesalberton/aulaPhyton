# 1. 🔢 Variáveis de vários tipos com print() e type()
inteiro = 10
decimal = 3.14
booleano = True
texto = "Olá, mundo!"
nulo = None
bytes_var = b"exemplo"
bytearray_var = bytearray(b"exemplo")

print(inteiro, type(inteiro))
print(decimal, type(decimal))
print(booleano, type(booleano))
print(texto, type(texto))
print(nulo, type(nulo))
print(bytes_var, type(bytes_var))
print(bytearray_var, type(bytearray_var))

# 2. 📋 Lista com 5 números
numeros = [5, 2, 9, 1, 7]
print("Tamanho da lista:", len(numeros))
print("Ordem crescente:", sorted(numeros))
print("Ordem decrescente:", sorted(numeros, reverse=True))

# 3. 🔘 Tupla com 3 cores
cores = ("vermelho", "azul", "verde")
print("Primeira cor:", cores[0])
print("azul aparece", cores.count("azul"), "vez(es)")
print("Índice de 'verde':", cores.index("verde"))

# 4. 🌀 Set com elementos repetidos
conjunto = {1, 2, 2, 3, 4, 4, 5}
print("Set sem duplicatas:", conjunto)  # Os elementos duplicados são ignorados

# 5. 🗂 Dicionário com nome, idade, curso
pessoa = {
    "nome": "Ana",
    "idade": 22,
    "curso": "Engenharia"
}
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Curso:", pessoa["curso"])

# 6. 📅 Data usando datetime.date()
import datetime
data_hoje = datetime.date.today()
print("Data de hoje:", data_hoje)

# 7. ➕ Soma e concatenação com f-string
a = 10
b = 5
print(f"Soma: {a + b}")

nome = "João"
sobrenome = "Silva"
print(f"Nome completo: {nome} {sobrenome}")
