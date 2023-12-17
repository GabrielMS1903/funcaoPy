def joao(peso, altura):
 conta = (peso / altura )
 return conta

numero = joao(56, 1.70)
print(numero)


def op(num1, num2, operacao):
 if operacao == 2:
  return num1 - num2
 elif operacao == 1:
   return num1 + num2
 elif num2 > num1:
  return num1 * num2
 elif num1 > num2: 
  return num1 / num2

resultado = op(10, 2, 1)
print(resultado)
