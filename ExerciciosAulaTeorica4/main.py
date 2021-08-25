# Aula 4
# while, for, laços de repetição aninhados

# estrutura de repetição while (enquanto)
# repete o bloco de instruções

x = 1
while(x <= 5): # < iterador ou variável de controle
    print(x)
    x = x + 1

x = 0
while(x <= 99):
    print(x)
    x = x + 1

# variáveis contadoras e acumuladoras
# exercício com contador, imprimindo números pares
inicial = int(input('Qual é o valor inicial?: '))
final = int(input('Qual é o valor final?: '))
x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1

#exercicio com acumulador
soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}ª nota: '.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print('Média final: {}'.format(media))

# características e recursos avançados de laços em python
soma = 0
cont = 1
while( cont <= 5):
    x = int(input('Digite o {}ª número: '.format(cont)))
    soma += x # soma = soma + x
    cont += 1 # cont = cont + 1
print('Somatório: {}'.format(soma))

# validando dados de entrada
x = int(input('Digite um valor maior do que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
print('Você digitou {}. Programa encerrado.'.format(x))

# instrução break, encerra o laço de repetição
print('Sim mestre, digite uma mensagem que irei repetir: ')
print('Caso queira sair, é só digitar "sair".')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Okay mestre, saindo...')

# instrução continue, volta para o ínicio do laço
while True:
    nome = input('Como você se chama?')
    if (nome != 'Soobin'):
        continue
    senha = input('Digite sua senha: ')
    if (senha == 'TomorrowByTodoro'):
        break
print('Acesso liberado, logando...')

# valores truthy e falsey - condição que usa verdadeiro e falso sem ser booleano
nome = ''
while not nome:
    nome = input('Digite seu nome: ')
valor = int(input('Digite um número qualquer: '))
if valor:
    print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero')

# Estrutura de repetição for
# for(para)
# for i (iterador, variável qualquer) in range ( 6 ) :
# para i no intervalo de 6

for i in range(6):
    print(i)

# podemos definir o valor inicial do iterador? sim!
# podemos definir o passo? sim!

# for i in range(0 , 6 , 1):
# para i no intervalo de 0 até 6 num passo unitário

for i in range(0,6,1):
    print(i)

for i in range(10, 0, -2):
    print(i)

# while e for é bem parecido :)

# estruturas de repetição aninhada
tabuada = 1
while tabuada <= 10:
    print('TABUADA DO {}: '.format(tabuada))
    for i in range(1, 11,1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1