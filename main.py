num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
  cont += 1
  soma += num
  num = int(input('Digite um número: '))
print('A soma dos números é: {} '.format(soma))
print('A quantidade de números digitados é: {}'.format(cont))
print('FIM')