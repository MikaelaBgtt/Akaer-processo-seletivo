botas = []
cont = 0
try:
  while True:
    limite = int(
      input("Entre com uma quantidade de pares de bota recebidos: "))
    for i in range(limite):
      bota = input(
        "Coloque uma numeração de 30 até 60 e o lado correspondente ao pé - D para direito e E para esquerdo (Ex: 44 L): "
      ).split()
      botas.append(bota)
    for i in range(len(botas) - 1):
      if botas[i][1] != botas[i + 1][1]:
        if botas[i][0] == botas[i + 1][0]:
          cont += 1
    print(cont, " pares de botas encontrados")
    botas = []
    cont = 0
except EOFError:
  pass