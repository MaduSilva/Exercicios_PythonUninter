# >>>>> Condicional simples <<<<<
# Desenvolva um programa que lê dois valores numéricos inteiros e compara se o primeiro é
# maior do que o segundo, utilizando uma condicional simples.
# Caso seja verdadeiro ele imprime uma mensagem avisando

numero1 = int(input('Digite um valor inteiro: '))
numero2 = int(input('Digite um segundo valor inteiro: '))

if(numero1 > numero2):
    print('Sim é maior! :)') # Em python, identação é relevante


# >>>>> Condicional composta <<<<<
# Desenvolva um programa que lê um valor inteiro e descobre se ele é par ou impar

numero = int(input('Digite um valor inteiro: '))
if (numero % 2 == 0):
    print ('O numéro é par!')
else:
    print('O número é ímpar!')

# >>>>> Lógica Booleana <<<<<
x = True
y = False
print(not x) #é tipo o !x
print(not y)

x = True # and -> Uma vez false é false
y = False
print(x and y)

x = True # or -> Uma vez true é true
y = False
print(x or y)

x = 10
y = 1
res = not x > y # vai retornar false por causa do not
print(res)

x = 10
y = 1
z = 5.5
res = x > y or z == y # resulta true pois ao menos uma entrada é true
print(res)

# >>>>> Condicionais aninhadas <<<<<
# ou seja, várias condicionais juntas :p

salario = float(input('Qual é seu salário atual?: '))
ano_admissao = int(input('Qual seu ano de admissão na empresa?: '))
ano_atual = int(input('Em que ano estamos?: '))
tempo = ano_atual - ano_admissao
if (tempo > 10):
    bonus = salario * 0.3
else:
    if (tempo > 5 ):
        bonus = salario * 0.2
    else:
        bonus = salario * 0.1
print('Você tem {} anos dentro desta empresa.'.format(tempo))
print('Seu salário é de {}.'.format(salario))
print('E sua bonificação é de {}.'.format(bonus))
print('Salário final {}.'. format(bonus + salario))

# >>>>> Condicionais de múltipla escolha (elif) <<<<<
nome = input('Qual é seu nome?: ')
idade = int(input('Qual é sua idade?: '))
if nome == 'Madu':
    print('Olá, Madu!')
elif idade < 18:
    print('Você não é a Madu! E é menor de idade ainda por cima >:c é feio mentir!')
elif idade > 100:
    print('Diferente de você, a Madu não é imortal (ainda bem!)')

