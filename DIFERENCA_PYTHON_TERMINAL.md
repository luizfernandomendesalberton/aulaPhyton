# 🐍 DIFERENÇA: TERMINAL vs INTERPRETADOR PYTHON

## ❌ ERRO COMUM: Confundir onde executar comandos

### 📋 SITUAÇÃO ATUAL:
Você estava no **interpretador Python** (prompt `>>>`) e tentou executar um comando de terminal.

```
>>> pip install pandas
    ^^^^^^^
SyntaxError: invalid syntax
```

## ✅ SOLUÇÃO:

### 1️⃣ SAIR DO INTERPRETADOR PYTHON:
```python
>>> exit()
```
**OU** pressione `Ctrl + Z` depois `Enter` (Windows)
**OU** pressione `Ctrl + D` (Linux/Mac)

### 2️⃣ AGORA NO TERMINAL (prompt `PS C:\...>`):
```bash
python -m pip install pandas
```

## 📊 VISUAL DA DIFERENÇA:

### 🔴 INTERPRETADOR PYTHON (para código Python):
```
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")          # ✅ Código Python aqui
>>> x = 5 + 3                     # ✅ Código Python aqui
>>> pip install pandas            # ❌ ERRO! Comando de terminal aqui
```

### 🟢 TERMINAL/PROMPT (para comandos do sistema):
```
PS C:\Users\luizf\OneDrive\Documentos\aulaPython>
PS C:\Users\luizf\OneDrive\Documentos\aulaPython> python -m pip install pandas  # ✅ Comando de terminal aqui
PS C:\Users\luizf\OneDrive\Documentos\aulaPython> python main.py               # ✅ Comando de terminal aqui
PS C:\Users\luizf\OneDrive\Documentos\aulaPython> dir                          # ✅ Comando de terminal aqui
```

## 🎯 RESUMO RÁPIDO:

| Local | Prompt | Para que serve | Exemplos |
|-------|--------|----------------|----------|
| **Terminal** | `PS C:\...>` | Comandos do sistema, instalar pacotes | `python -m pip install pandas`<br>`python main.py`<br>`dir` |
| **Python** | `>>>` | Executar código Python | `print("Hello")`<br>`x = 5`<br>`import pandas` |

## 🔧 COMO PROCEDER AGORA:

1. **Saia do Python**: Digite `exit()` e pressione Enter
2. **Execute no terminal**: `python -m pip install pandas`
3. **Depois entre no Python novamente**: Digite `python`
4. **Agora pode usar pandas**: `import pandas as pd`

## 🚀 SEQUÊNCIA COMPLETA:
```
>>> exit()                                    # Sair do Python
PS C:\...> python -m pip install pandas      # Instalar pandas no terminal
PS C:\...> python                            # Entrar no Python novamente
>>> import pandas as pd                      # Usar pandas no Python
>>> print("Pandas instalado com sucesso!")  # Testar
```