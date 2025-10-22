nome = "luiz fernando"
idade =27
altura = 1.75
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}m")
print("*" * 50)

nomealuno = input("Digite o nome do aluno: ")
idadedoaluno = int(input("Digite a idade do aluno: "))
alturadoaluno = float(input("Digite a altura do aluno (em metros): "))
nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
nota3 = float(input("Digite a nota 3 do aluno: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Aluno: {nomealuno}, Idade: {idadedoaluno}, Altura: {alturadoaluno}m, Média das notas: {media:.2f}")
if media >= 7.0:
    print("Status: Aprovado")
else:
    print("Status: Reprovado")
print("*" * 50)