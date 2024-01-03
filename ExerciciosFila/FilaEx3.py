from collections import deque

class Livro:
    def __init__(self, nome, disponibilidade=True):

        self.nome = nome
        self.disponibilidade = disponibilidade
        self.fila_espera = deque()

class Biblioteca:
    def __init__(self):

        self.livros = {}

    def cadastra_livro(self, nome):

        if nome not in self.livros:
            self.livros[nome] = Livro(nome)
            print(f"Livro '{nome}' cadastrado com sucesso.")
        else:
            print(f"Livro '{nome}' já cadastrado.")

    def retira_livro(self, nome):

        if nome in self.livros:
            livro = self.livros[nome]
            if livro.disponibilidade:
                livro.disponibilidade = False
                return f"Livro '{nome}' retirado com sucesso."
            elif livro.fila_espera:
                proximo_na_fila = livro.fila_espera.popleft()
                livro.disponibilidade = False
                return f"Livro '{nome}' não disponível. '{proximo_na_fila}' retirou da fila de espera."
            else:
                return f"Livro '{nome}' não disponível. Nenhum usuário na fila de espera."
        else:
            return f"Livro '{nome}' não encontrado."

    def devolve_livro(self, nome):

        if nome in self.livros:
            livro = self.livros[nome]
            livro.disponibilidade = True
            if livro.fila_espera:
                proximo_na_fila = livro.fila_espera.popleft()
                return f"Livro '{nome}' devolvido. '{proximo_na_fila}' retirou da fila de espera."
            else:
                return f"Livro '{nome}' devolvido. Não há pessoas na fila de espera."
        else:
            return f"Livro '{nome}' não encontrado."

def main_biblioteca():
    biblioteca = Biblioteca()

    while True:
        print("\n----- Menu Biblioteca -----")
        print("1. Cadastrar Livro")
        print("2. Retirar Livro")
        print("3. Devolver Livro")
        print("4. Sair")

        escolha = input("Digite sua escolha (1-4): ")

        if escolha == "1":
            nome_livro = input("Digite o nome do livro a cadastrar: ")
            biblioteca.cadastra_livro(nome_livro)
        elif escolha == "2":
            nome_livro_retirar = input("Digite o nome do livro a retirar: ")
            print(biblioteca.retira_livro(nome_livro_retirar))
        elif escolha == "3":
            nome_livro_devolver = input("Digite o nome do livro a devolver: ")
            print(biblioteca.devolve_livro(nome_livro_devolver))
        elif escolha == "4":
            print("Encerrando o programa!")
            break
        else:
            print("Escolha inválida. Digite um número entre 1 e 4.")

if __name__ == "__main__":
    main_biblioteca()
