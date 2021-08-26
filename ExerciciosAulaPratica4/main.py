# Aula prática 4 aaaaaaaaaaaaaaa D:

for i in range(3, 13, 1):
    print(i)

i = 3
while (i < 13):
    print(i)
    i += 1

for i in range(0, 9, 2):
    print(i)

i = 0
while (i <= 9):
    print(i)
    i += 2

# Problemas T-T
# Algoritmo que lê dois valores e pergunta pro usuário qual operação ele quer realizar ( +, -, *, /, e sair)
# Exibe na tela o resultado
# Repete até o usuário pedir pra sair

print('Calculadora')
print(' + Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja realizar?')
if op == '+' or op == '-' or op == '*' or op=='/':
    x = int(input('Digite o primeiro valor: '))
    y = int(input('Digite o segundo valor: '))

while (op != 's'):
    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
    else:
        print('Operação inválida!')

    op = input('Qual operação deseja realizar?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

print('Encerrando o programa...')

# Exercício 2 - Caixa eletrônico
# Algoritmo que leia o valor e imprima a quantidade de cédulas necessárias
# para pagar esse valor
# cédulas de 100, 50, 20, 10, 5 e 1

valor = int(input('Digite o valor inteiro em R$: '))

while True:
    if valor >= 100:
        cedulas100 = valor // 100 # // é a divisão pegando só a parte inteira
        valor = valor - cedulas100 * 100
        print('Cédulas de 100: {}'.format(cedulas100))
        if not valor:
            break
    if valor >= 50:
        cedulas50 = valor // 50 # // é a divisão pegando só a parte inteira
        valor = valor - cedulas50 * 50
        print('Cédulas de 50: {}'.format(cedulas50))
        if not valor:
            break
    if valor >= 20:
        cedulas20 = valor // 20 # // é a divisão pegando só a parte inteira
        valor = valor - cedulas20 * 20
        print('Cédulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10 # // é a divisão pegando só a parte inteira
        valor = valor - cedulas10 * 10
        print('Cédulas de 10: {}'.format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5 # // é a divisão pegando só a parte inteira
        valor = valor - cedulas5 * 5
        print('Cédulas de 5: {}'.format(cedulas5))
        if not valor:
            break
    if valor:
        cedulas1 = valor
        print('Cédulas de 1: {}'.format(cedulas1))
        break


# Exercicio 3 - Cinema :)
total = 0
dinheiro = 0

while True:
    idade = input('Qual é a sua idade?')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado: {}'.format(dinheiro))
print('Média arrecadada: {}'.format(media))
