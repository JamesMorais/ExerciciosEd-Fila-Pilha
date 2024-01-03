class Pilha:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.itens = []

    def empty(self):
        return len(self.itens) == 0

    def is_empty(self):
        return self.empty()

    def is_full(self):
        return len(self.itens) == self.tamanho_maximo

    def push(self, item):
        if not self.is_full():
            self.itens.append(item)
            print(f"{item} foi adicionado à pilha.")
        else:
            print("A pilha está cheia. Não é possível adicionar mais itens.")

    def pop(self):
        if not self.is_empty():
            item_removido = self.itens.pop()
            print(f"{item_removido} foi removido da pilha.")
            return item_removido
        else:
            print("A pilha está vazia. Não é possível remover itens.")

    def top(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            print("A pilha está vazia. Não há topo.")

# Exemplo de uso:
pilha = Pilha(5)

pilha.push(1)
pilha.push(2)
pilha.push(3)

print(f"Topo da pilha: {pilha.top()}")

pilha.pop()

print(f"Topo da pilha após remoção: {pilha.top()}")
