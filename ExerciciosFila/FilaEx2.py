def inverte_fila(fila):


  pilha = []
  fila_invertida = []

  # Insere todos os elementos da fila F1 na pilha.
  for elemento in fila:
    pilha.append(elemento)

  # Remove os elementos da pilha e insere na fila F2, na ordem inversa.
  while pilha:
    fila_invertida.append(pilha.pop())

  return fila_invertida


def main_fila_ex2():


  tamanho = int(input("Digite o tamanho da fila: "))
  fila = []

  for i in range(tamanho):
    numero = int(input("Digite o número a ser inserido na posição {}: ".format(i)))
    fila.append(numero)

  fila_invertida = inverte_fila(fila)

  print("Fila original:")
  for elemento in fila:
    print(elemento)

  print("Fila invertida:")
  for elemento in fila_invertida:
    print(elemento)


if __name__ == "__main__":
  main_fila_ex2()