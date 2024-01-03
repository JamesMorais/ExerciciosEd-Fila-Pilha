class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()

    def esta_vazia(self):
        return len(self.items) == 0

    def apagar_tudo(self):
        self.items = []

# Função principal que executa as ações descritas
def editor_texto(entrada):
    pilha = Pilha()

    for caractere in entrada:
        if caractere == '#':
            pilha.desempilhar()
        elif caractere == '@':
            pilha.apagar_tudo()
        else:
            pilha.empilhar(caractere)

    return ''.join(pilha.items)

# Exemplo de uso
entrada = "abc#d@ef"
resultado = editor_texto(entrada)
print("Texto final:", resultado)
