limite = int(input(""))
guarda = 0
numero = []
for i in range(limite-1):
   numero.append(int(input("Digite alguns numeros: ")))
soma = ((len(numero)+1) * ((len(numero)+1) + 1)) // 2
soma2 = sum(numero)
falta = soma - soma2
print("O número que falta é: ", falta)