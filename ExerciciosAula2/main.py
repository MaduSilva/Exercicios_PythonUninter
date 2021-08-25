print(1 + 2 + 3 + 4 + 5),  # Soma normal e simples
print((23 + 19 + 31) / 3),  # Fazendo uma média, primeiro faz a soma dos 3 numeros depois divide por 3
print(403 // 73),  # Fazendo uma divisão normal
print(403 % 73),  # Fazendo uma divisão mas retornando o resto dela (chamado de MOD)

print(2**10), # 2 elevado a 10 potencia
print(abs(54 - 57)) # valor absoluto da diferença entre 54 e 57
print(min(34, 29, 31))# menor valor entre 34, 29 e 31

a = 3 # atribuir o valor inteiro 3 a variavel A, sinal de = significa atribuição
b = 4 # variavel b recebe 4
c = a*a + b*b # variavel que recebe a.a e b.b

s1 = 'ant' # criando strings
s2 = 'bat'
s3 = 'cod'

print (s1 + ' ' + s2 + ' ' + s3) # vai printar ant bat cod, as '' servem de espacinho

print ( 10 * (s1 + ' '))

print ( (s1 + ' ') + (2 * (s2 + ' ')) + (3*(s3 + ' ')))

print (7 * (s1 + ' ' + s2 + ' '))

print (5 * (s2 + s2 + s3 + ' '))

# usuario insere o valor do produto e o desconto que vai colocar nele
# o programa faz o desconto e mostra no fim pro usuario

preco = float(input('Insira o valor do produto:'))
p = float(input('Insira o desconto que vai ser aplicado no produto (0-100):'))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {} . Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

# programa que pergunta a quantidade km percorrido por um carro alugado pelo usuario, assim como
# a quantidade de dias pelos quais o carro foi alugado. Calcula o preço a pagar, sabendo que o carro
#Custa 60 reais por dia e 15 centavos pro km rodado


qtdPercorrida  = int(input('Insira quantos km o carro percorreu:'))
qtdDias  = int(input('Insira quantos dias o carro foi alugado:'))

precoDistancia = qtdPercorrida * 0.15
precoDias = qtdDias * 60
precoFinal = precoDistancia + precoDias

print('Você correu {} KM e Alugou o carro por {} dias.'.format(qtdPercorrida, qtdDias))
print('Valor dos KM: {}. Valor dos dias: {}'.format(precoDistancia, precoDias))
print('Você deverá um valor total de {}'.format(precoFinal))

# Cria uma variavel que receba uma frase qualquer, depois cria outra variavel contendo
# metade da string digitada, imprime na tela somente os dois ultimos caracteres da segunda
# variavel do tipo string


frase = input('Digite uma frase:')
tam = len(frase) # len calcula o tamanho da frase
frase2 = frase[:int(tam/2)]
print(frase2[-2:])

# fim :)