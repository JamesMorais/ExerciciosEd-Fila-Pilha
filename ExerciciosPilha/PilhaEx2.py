class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def sao_iguais(self, outra_pilha):
        """
        Verifica se duas pilhas são iguais.
        """
        return self.items == outra_pilha.items