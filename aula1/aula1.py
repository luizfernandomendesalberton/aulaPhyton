# ==============================================
# AULA 1 - INTRODUÇÃO AO PYTHON
# ==============================================

print("🐍 Bem-vindo ao Python! 🐍")
print("=" * 40)

# ==============================================
# 1. VARIÁVEIS E TIPOS DE DADOS
# ==============================================

print("\n📦 1. VARIÁVEIS E TIPOS DE DADOS")
print("-" * 30)

# Números
idade = 25
altura = 1.75
salario = 3500.50

# Texto (strings)
nome = "João Silva"
profissao = "Programador"

# Booleano (True/False)
estudante = True
aposentado = False

# Exibindo os valores
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura}m")
print(f"Profissão: {profissao}")
print(f"Salário: R$ {salario}")
print(f"É estudante? {estudante}")

# Verificando tipos
print(f"\nTipo da variável 'nome': {type(nome)}")
print(f"Tipo da variável 'idade': {type(idade)}")
print(f"Tipo da variável 'altura': {type(altura)}")

# ==============================================
# 2. OPERAÇÕES MATEMÁTICAS
# ==============================================

print("\n🔢 2. OPERAÇÕES MATEMÁTICAS")
print("-" * 30)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b:.2f}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Resto da divisão: {a} % {b} = {a % b}")
print(f"Potência: {a} ** {b} = {a ** b}")

# ==============================================
# 3. TRABALHANDO COM STRINGS
# ==============================================

print("\n📝 3. TRABALHANDO COM STRINGS")
print("-" * 30)

frase = "Python é uma linguagem incrível!"
print(f"Frase original: '{frase}'")
print(f"Maiúscula: '{frase.upper()}'")
print(f"Minúscula: '{frase.lower()}'")
print(f"Tamanho da frase: {len(frase)} caracteres")
print(f"Primeira palavra: '{frase.split()[0]}'")
print(f"Contém 'Python'? {frase.count('Python') > 0}")

# ==============================================
# 4. ENTRADA DE DADOS DO USUÁRIO
# ==============================================

print("\n👤 4. INTERAÇÃO COM O USUÁRIO")
print("-" * 30)

# Descomente as linhas abaixo para testar interação
# usuario_nome = input("Digite seu nome: ")
# usuario_idade = input("Digite sua idade: ")
# print(f"Olá {usuario_nome}! Você tem {usuario_idade} anos.")

# Para demonstração, vou usar valores fixos
usuario_nome = "Maria"
usuario_idade = "30"
print(f"Simulação: Olá {usuario_nome}! Você tem {usuario_idade} anos.")

# ==============================================
# 5. ESTRUTURAS CONDICIONAIS (IF, ELIF, ELSE)
# ==============================================

print("\n🔀 5. ESTRUTURAS CONDICIONAIS")
print("-" * 30)

# Exemplo 1: Verificando idade
idade_pessoa = 18
print(f"Idade da pessoa: {idade_pessoa}")

if idade_pessoa >= 18:
    print("✅ Maior de idade - pode votar!")
else:
    print("❌ Menor de idade - não pode votar ainda")

# Exemplo 2: Classificação por nota
nota = 8.5
print(f"\nNota do aluno: {nota}")

if nota >= 9.0:
    print("📚 Conceito: EXCELENTE!")
elif nota >= 7.0:
    print("😊 Conceito: BOM!")
elif nota >= 6.0:
    print("😐 Conceito: REGULAR")
elif nota >= 4.0:
    print("😟 Conceito: INSUFICIENTE")
else:
    print("😞 Conceito: REPROVADO")

# Exemplo 3: Verificando múltiplas condições
temperatura = 25
chovendo = False

print(f"\nTemperatura: {temperatura}°C")
print(f"Está chovendo? {chovendo}")

if temperatura > 20 and not chovendo:
    print("🌞 Ótimo dia para sair!")
elif temperatura > 20 and chovendo:
    print("🌧️  Dia quente, mas está chovendo. Leve guarda-chuva!")
elif temperatura <= 20 and not chovendo:
    print("🧥 Dia frio, vista uma jaqueta!")
else:
    print("❄️  Dia frio e chuvoso. Melhor ficar em casa!")

# ==============================================
# 6. LOOPS E REPETIÇÕES
# ==============================================

print("\n🔄 6. LOOPS E REPETIÇÕES")
print("-" * 30)

# Loop FOR - contando de 1 a 5
print("Contagem com FOR:")
for i in range(1, 6):
    print(f"Número: {i}")

# Loop FOR com lista
frutas = ["maçã", "banana", "laranja", "uva"]
print(f"\nFrutas disponíveis:")
for fruta in frutas:
    print(f"🍎 {fruta}")

# Loop WHILE - contador regressivo
print(f"\nContador regressivo:")
contador = 5
while contador > 0:
    print(f"⏰ {contador}...")
    contador -= 1
print("🚀 Decolar!")

# ==============================================
# 7. LISTAS E OPERAÇÕES
# ==============================================

print("\n📋 7. TRABALHANDO COM LISTAS")
print("-" * 30)

# Criando listas
numeros = [1, 2, 3, 4, 5]
nomes = ["Ana", "Carlos", "Bruno", "Diana"]

print(f"Lista de números: {numeros}")
print(f"Lista de nomes: {nomes}")

# Operações com listas
numeros.append(6)  # Adiciona no final
print(f"Após adicionar 6: {numeros}")

numeros.insert(0, 0)  # Adiciona no início
print(f"Após adicionar 0 no início: {numeros}")

print(f"Primeiro nome: {nomes[0]}")
print(f"Último nome: {nomes[-1]}")
print(f"Total de nomes: {len(nomes)}")

# ==============================================
# 8. DICIONÁRIOS (CHAVE-VALOR)
# ==============================================

print("\n📚 8. TRABALHANDO COM DICIONÁRIOS")
print("-" * 30)

# Criando um dicionário
pessoa = {
    "nome": "Pedro Silva",
    "idade": 28,
    "profissao": "Engenheiro",
    "cidade": "São Paulo",
    "tem_filhos": False
}

print("Informações da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Acessando valores específicos
print(f"\nNome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']} anos")

# Adicionando nova informação
pessoa["email"] = "pedro@email.com"
print(f"Email adicionado: {pessoa['email']}")

# ==============================================
# 9. FUNÇÕES SIMPLES
# ==============================================

print("\n🔧 9. CRIANDO FUNÇÕES")
print("-" * 30)

def cumprimentar(nome):
    """Função que cumprimenta uma pessoa"""
    return f"Olá, {nome}! Seja bem-vindo(a)!"

def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    area = largura * altura
    return area

def eh_par(numero):
    """Verifica se um número é par"""
    return numero % 2 == 0

# Testando as funções
print(cumprimentar("Maria"))
print(f"Área do retângulo 5x3: {calcular_area_retangulo(5, 3)} m²")
print(f"O número 8 é par? {eh_par(8)}")
print(f"O número 7 é par? {eh_par(7)}")

# ==============================================
# 10. EXEMPLO PRÁTICO - CALCULADORA SIMPLES
# ==============================================

print("\n🧮 10. CALCULADORA SIMPLES")
print("-" * 30)

def calculadora(num1, num2, operacao):
    """Calculadora que realiza operações básicas"""
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"

# Testando a calculadora
print(f"10 + 5 = {calculadora(10, 5, '+')}")
print(f"10 - 5 = {calculadora(10, 5, '-')}")
print(f"10 * 5 = {calculadora(10, 5, '*')}")
print(f"10 / 5 = {calculadora(10, 5, '/')}")
print(f"10 / 0 = {calculadora(10, 0, '/')}")

print("\n🎉 Parabéns! Você completou a Aula 1 de Python!")
print("=" * 50)
