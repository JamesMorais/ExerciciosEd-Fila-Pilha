class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia")

def calcular_posfixa(expressao):
    pilha = Pilha()

    for token in expressao.split():
        if token.isdigit():
            pilha.empilhar(int(token))
        else:
            segundo_operando = pilha.desempilhar()
            primeiro_operando = pilha.desempilhar()

            if token == '+':
                resultado = primeiro_operando + segundo_operando
            elif token == '-':
                resultado = primeiro_operando - segundo_operando
            elif token == '*':
                resultado = primeiro_operando * segundo_operando
            elif token == '/':
                resultado = primeiro_operando / segundo_operando
            else:
                raise ValueError("Operador inválido: {}".format(token))

            pilha.empilhar(resultado)

    if not pilha.vazia():
        return pilha.desempilhar()
    else:
        raise ValueError("Expressão posfixa inválida")