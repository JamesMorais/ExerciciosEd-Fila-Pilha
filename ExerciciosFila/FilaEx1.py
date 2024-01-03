def fila_ordenada(fila):

  for i in range(len(fila) - 1):
    if fila[i] > fila[i + 1]:
      return False
  return True


def main_verifica_ordem_da_fila():


  tamanho = int(input("Digite o tamanho da fila: "))
  fila = []

  for i in range(tamanho):
    numero = int(input("Digite o número a ser inserido na posição {}: ".format(i)))
    fila.append(numero)

  if fila_ordenada(fila):
    print("A fila está ordenada de forma crescente.")
  else:
    print("A fila não está ordenada de forma crescente.")


if __name__ == "__main__":
  main_verifica_ordem_da_fila()