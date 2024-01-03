class Lista:
    def __init__(self):
        self.array = []

    def append(self, elemento):
        self.array.append(elemento)

    def tamanho(self):
        return len(self.array)

    def imprime(self):
        print(self.array)

    def concatenar(self, outra_lista):
        nova_lista = Lista()
        nova_lista.array = self.array + outra_lista.array
        return nova_lista

    def dividir(self, indice):
        if 0 <= indice < len(self.array):
            parte1 = Lista()
            parte2 = Lista()
            parte1.array = self.array[:indice]
            parte2.array = self.array[indice:]
            return parte1, parte2
        else:
            raise ValueError("Índice de divisão inválido")

    def copiar(self):
        nova_lista = Lista()
        nova_lista.array = self.array.copy()
        return nova_lista

    def pesquisar(self, elemento):
        return elemento in self.array
