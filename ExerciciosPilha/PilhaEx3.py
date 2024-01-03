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

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]

    def tamanho(self):
        return len(self.items)

    def inverter(self):
        self.items = self.items[::-1]

# Exemplo de uso:
minha_pilha = Pilha()
minha_pilha.empilhar(1)
minha_pilha.empilhar(2)
minha_pilha.empilhar(3)

print("Pilha original:", minha_pilha.items)

minha_pilha.inverter()

print("Pilha invertida:", minha_pilha.items)
