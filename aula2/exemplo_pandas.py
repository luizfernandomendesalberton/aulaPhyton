# ==============================================
# EXEMPLO PRÁTICO COM PANDAS E MATPLOTLIB
# ==============================================

import pandas as pd
import matplotlib.pyplot as plt

print("Testando Pandas e Matplotlib!")
print("=" * 40)

# Criando dados de exemplo
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Idade': [25, 30, 35, 28, 32],
    'Salário': [5000, 6500, 7000, 5800, 6200],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo', 'Rio de Janeiro']
}

# Criando DataFrame
df = pd.DataFrame(dados)

print("\nDADOS CRIADOS:")
print(df)

# ==============================================
# DEMONSTRAÇÃO: ALTERANDO VARIÁVEIS
# ==============================================

print("\n" + "="*50)
print("DEMONSTRAÇÃO: ALTERANDO VARIÁVEIS APÓS IMPRIMIR")
print("="*50)

# Variável simples - valor inicial
salario_inicial = 5000
print(f"\n1. Salário inicial: R$ {salario_inicial}")

# Alterando o valor da variável
salario_inicial = salario_inicial + 1000  # Aumento de R$ 1000
print(f"   Após aumento: R$ {salario_inicial}")

# Exemplo com string
nome_funcionario = "João"
print(f"\n2. Nome inicial: {nome_funcionario}")
nome_funcionario = "João Silva"  # Adicionando sobrenome
print(f"   Nome completo: {nome_funcionario}")

# Exemplo com lista
idades = [25, 30, 35]
print(f"\n3. Idades originais: {idades}")
idades.append(28)  # Adicionando nova idade
print(f"   Após adicionar idade: {idades}")

# Exemplo com DataFrame - alterando dados
print(f"\n4. ALTERANDO DADOS NO DATAFRAME:")
print(f"   Salário do Bruno antes: R$ {df.loc[df['Nome'] == 'Bruno', 'Salário'].values[0]}")

# Alterando o salário do Bruno
df.loc[df['Nome'] == 'Bruno', 'Salário'] = 7500
print(f"   Salário do Bruno depois: R$ {df.loc[df['Nome'] == 'Bruno', 'Salário'].values[0]}")

# Mostrando a tabela atualizada
print(f"\n5. TABELA ATUALIZADA:")
print(df)

print(f"\nESTATÍSTICAS RECALCULADAS:")
print(f"Idade média: {df['Idade'].mean():.1f} anos")
print(f"Salário médio: R$ {df['Salário'].mean():.2f}")
print(f"Pessoa mais velha: {df.loc[df['Idade'].idxmax(), 'Nome']} ({df['Idade'].max()} anos)")
print(f"Maior salário: {df.loc[df['Salário'].idxmax(), 'Nome']} (R$ {df['Salário'].max()})")

print(f"\nPESSOAS POR CIDADE:")
cidade_counts = df['Cidade'].value_counts()
for cidade, quantidade in cidade_counts.items():
    print(f"{cidade}: {quantidade} pessoa(s)")

# Salvando dados em CSV
df.to_csv('funcionarios.csv', index=False)
print(f"\nDados salvos em 'funcionarios.csv'")

# Criando gráfico simples
plt.figure(figsize=(10, 6))

# Gráfico 1: Idade vs Salário
plt.subplot(1, 2, 1)
plt.scatter(df['Idade'], df['Salário'], color='blue', alpha=0.7)
plt.xlabel('Idade')
plt.ylabel('Salário (R$)')
plt.title('Idade vs Salário')
plt.grid(True, alpha=0.3)

# Gráfico 2: Salários por pessoa
plt.subplot(1, 2, 2)
plt.bar(df['Nome'], df['Salário'], color='green', alpha=0.7)
plt.xlabel('Nome')
plt.ylabel('Salário (R$)')
plt.title('Salários por Pessoa')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('grafico_funcionarios.png', dpi=150, bbox_inches='tight')
plt.show()




print(f"\nGráfico salvo como 'grafico_funcionarios.png'")
print("\nPandas e Matplotlib funcionando perfeitamente!")