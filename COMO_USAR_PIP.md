# =========================================
# COMO USAR O PIP CORRETAMENTE NO SEU SISTEMA
# =========================================

## PROBLEMA IDENTIFICADO:
O comando `pip` está apontando para Python 3.13 (que tem problemas)
Mas o Python 3.12 está funcionando perfeitamente!

## SOLUÇÃO:
Use sempre: `python -m pip` em vez de apenas `pip`

## COMANDOS CORRETOS:

### 1. Verificar versão do pip:
python -m pip --version

### 2. Listar pacotes instalados:
python -m pip list

### 3. Instalar um pacote:
python -m pip install nome_do_pacote

### 4. Instalar pacote específico (exemplo):
python -m pip install requests
python -m pip install matplotlib
python -m pip install pandas

### 5. Desinstalar um pacote:
python -m pip uninstall nome_do_pacote

### 6. Atualizar um pacote:
python -m pip install --upgrade nome_do_pacote

### 7. Instalar a partir de arquivo requirements.txt:
python -m pip install -r requirements.txt

## EXEMPLOS PRÁTICOS:

# Instalar bibliotecas populares para Python:
python -m pip install matplotlib  # Para gráficos
python -m pip install pandas     # Para análise de dados
python -m pip install requests   # Para requisições HTTP
python -m pip install numpy      # Para cálculos numéricos

## VERIFICAÇÃO:
Seu Python 3.12 está funcionando perfeitamente!
Use sempre 'python -m pip' e tudo funcionará corretamente.

## VERSÕES INSTALADAS:
- Python: 3.12.4
- pip: Funcionando via 'python -m pip'