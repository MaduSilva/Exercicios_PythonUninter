# Aula Teorica 5 :)
# Funções
# Quando eu chamo uma função, o bloco de código dele é chamado, pensa que é parecido com o component do react

# sintaxe - def realce ( ) :
# tradução - definition nomedafuncao () :

def menu():
    print('|' , '__' * 10, '|' )
    print('|', '__' * 10, '|')

menu()
print('          MENU')
menu()

# parametros em funções
# sintaxe - def nomedafuncao(nomedavariavel):

def menu2(s1):
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')
    print(s1)
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')

menu2('          Madu')

def sub2(x, y):
    res = x - y
    print(res)

sub2(5, 7) # o x e o y são substituidos pelo 5 e pelo 7

def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    print(res)

soma3(1,2,3)
soma3(1,2)  # z foi omitido
soma3(1) # y e z são omitidos
soma3() # x, y e z são omitidos

# exercício 1 - adapte bordas ao tamanho da palavra
def borda(s1):
    tam = len(s1)
    # só imprime se existir algum caractere
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

borda('Olá mundo!')
borda('Soobin Center')
borda('Assista Tokyo Revengers, é muito bom!')

# escopo de variáveis
# determina onde uma variavel pode ser utilizada dentro do programa
# esquema de variaveis globais e locais
def comida():
    print(ovos)

ovos = 12
comida()
##################################
def comida():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6 # a variavel ovos não consegue ser acessada

comida()
###################################
def comida():
    ovos = 'variável local de comida'
    print(ovos)

def bacon():
    ovos = 'variável local de bacon'
    print(ovos)
    comida()
    print(ovos)

ovos = 'variável global'
bacon()
print(ovos)

###################################
# instrução global

def comida():
    global ovos
    ovos = 'comida'

ovos = 'global'
comida()
print(ovos)

# Retorno de valores em funções
# procedimento (procedure) - uma rotina sem retorno
# função - uma rotina com retorno

#exercicio - função para validar valores
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam <min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

x = valida_string('Digite uma string: ', 10, 30)
print( 'Você digitou a string: {}. \n Dado válido. Encerrando o programa...'.format(x))

# Recursos avançados com funções
# Exceções em programas (ZeroDivisionError, ValueError, IndexError, etc)

# Tratando dados para evitar exceções

while True:
    try:
        x = int(input('Por favor digite um número: '))
        break
    except ValueError:
        print('Número inválido. Tente novamente...')

# exemplo 2
def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Oops! Erro de divisão por zero...')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Executará sempre!')

print(div())