# ============================================
# 📚 Sistema de Biblioteca
# Autor: [Seu nome]
# Versão básica e funcional
# ============================================

from datetime import date

# ------------------------------
# 🧱 Classes principais
# ------------------------------

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({self.ano}) [{status}]"


class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} (Matrícula: {self.matricula})"


class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = date.today()
        self.data_devolucao = None

    def devolver(self):
        self.data_devolucao = date.today()
        self.livro.disponivel = True


# ------------------------------
# 📦 Estruturas de dados
# ------------------------------

livros = []
usuarios = []
emprestimos = []


# ------------------------------
# 📚 Funções do sistema
# ------------------------------

def listar_livros():
    if not livros:
        print("📭 Nenhum livro cadastrado.")
    else:
        print("\n📚 Lista de livros:")
        for i, livro in enumerate(livros):
            print(f"{i + 1}. {livro}")


def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    livros.append(Livro(titulo, autor, ano))
    print("✅ Livro cadastrado com sucesso!")


def editar_livro():
    listar_livros()
    if not livros:
        return
    try:
        indice = int(input("Número do livro para editar: ")) - 1
        livro = livros[indice]
        livro.titulo = input(f"Novo título ({livro.titulo}): ") or livro.titulo
        livro.autor = input(f"Novo autor ({livro.autor}): ") or livro.autor
        livro.ano = input(f"Novo ano ({livro.ano}): ") or livro.ano
        print("✏️ Livro atualizado com sucesso!")
    except (ValueError, IndexError):
        print("❌ Opção inválida.")


def remover_livro():
    listar_livros()
    if not livros:
        return
    try:
        indice = int(input("Número do livro para remover: ")) - 1
        livro = livros.pop(indice)
        print(f"❌ Livro '{livro.titulo}' removido com sucesso.")
    except (ValueError, IndexError):
        print("❌ Opção inválida.")


def cadastrar_usuario():
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    usuarios.append(Usuario(nome, matricula))
    print("✅ Usuário cadastrado com sucesso!")


def listar_usuarios():
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
    else:
        print("\n👥 Lista de usuários:")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario}")


def realizar_emprestimo():
    listar_livros()
    if not livros:
        return
    try:
        indice_livro = int(input("Número do livro: ")) - 1
        livro = livros[indice_livro]
        if not livro.disponivel:
            print("🚫 Este livro não está disponível.")
            return
        listar_usuarios()
        indice_usuario = int(input("Número do usuário: ")) - 1
        usuario = usuarios[indice_usuario]
        emprestimos.append(Emprestimo(livro, usuario))
        livro.disponivel = False
        print(f"📦 Livro '{livro.titulo}' emprestado para {usuario.nome}.")
    except (ValueError, IndexError):
        print("❌ Opção inválida.")


def devolver_livro():
    emprestimos_ativos = [e for e in emprestimos if e.data_devolucao is None]
    if not emprestimos_ativos:
        print("📭 Nenhum empréstimo ativo.")
        return

    print("\n🔄 Empréstimos ativos:")
    for i, e in enumerate(emprestimos_ativos):
        print(f"{i + 1}. {e.livro.titulo} - {e.usuario.nome}")

    try:
        indice = int(input("Número do empréstimo a devolver: ")) - 1
        emprestimo = emprestimos_ativos[indice]
        emprestimo.devolver()
        print(f"✅ Livro '{emprestimo.livro.titulo}' devolvido com sucesso.")
    except (ValueError, IndexError):
        print("❌ Opção inválida.")


# ------------------------------
# 🧭 Menu principal
# ------------------------------

def menu():
    while True:
        print("\n=== 📚 SISTEMA DE BIBLIOTECA ===")
        print("1. Listar livros")
        print("2. Cadastrar livro")
        print("3. Editar livro")
        print("4. Remover livro")
        print("5. Cadastrar usuário")
        print("6. Listar usuários")
        print("7. Realizar empréstimo")
        print("8. Devolver livro")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            cadastrar_livro()
        elif opcao == "3":
            editar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            cadastrar_usuario()
        elif opcao == "6":
            listar_usuarios()
        elif opcao == "7":
            realizar_emprestimo()
        elif opcao == "8":
            devolver_livro()
        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


# ------------------------------
# 🚀 Execução do programa
# ------------------------------

if __name__ == "__main__":
    menu()
