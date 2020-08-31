# PRIMEIROS EXEMPLOS #

print('Primeiro Programa')
1+2

## TIPOS BÁSICOS

print(True) # verdadeiro
print(False) # falso
print(1.2+1) ## Float
print('Aqui eu falo na minha lingua!') ## String
print("Tb funciona") ## Com aspas duplas
print('Você é ' +3 * 'muito ' + 'legal') ## mistura de numeros e letras
print(3 + '3') ## erro de ambiguidade
print([1, 2, 3]) ## lista(array)
print({'nome' : 'Pedro', 'idade' : 22}) ## lista chave / dicionario
print(None) # Ausencia de valor (null)

# VARIÁVEIS

a = 10
b = 5.2

print(a+b)

a = 'Agora sou uma string'
print(a)

# COMENTÁRIOS

# Minhas variáveis
salario = 3450.45
despesas - 2456.2

'''
A ideia e calcular o
quanto vai sobrar no
final do mes!
'''

print(salario - despesas)

#print('Fim')
print('Fim de verdade') #comentário aqui tb vale!

# OPERADORES ARITMÉTICOS

print(2 + 3) # adição
print(4 - 7) # subtração
print(2 * 5.3) # multiplicação
print(9.4 / 3) # divisão

print(9.4 // 3) # divisão inteira
print(2 ** 8) # exponenciação
print(10 % 3) # resto da divisão

a= 12
b = a

print(a + b)

# Desafio 

salario = 3450.45
despesas - 2456.2

#Resposta

percentual_comprometido = despesas / salario * 100

# Operadores relacionais

3 > 4 # 3 maior que 4
4 >= 3 # 4 maior ou igual a 3
1 < 2 # 1 menor que 2
3 <= 1 # 3 menor ou igual a 1
3 != 2 # 3 diferente de 2
3 == 3 # 3 igual a 3
2 == '3' # inteiro e string

# Operadores de atribuição

a = 3 # a recebe 3
a = a + 7 # a recebe o valor da soma de a + 7
a += 5 # acrescentando 5 ao valor de a
a -= 3 # decrescenta 3 ao valor de a
a *= 2 # variavel a multiplicada por 2
a /= 4 # variavel a dividida por 4
a %= 4 # resto da divisao
a **= 8 # valor de a exponenciado a 8
a //= 256 # divisão inteira

# Operadores Lógicos

True or False

7!= 3 and 2 > 3 # sete é diferente de 3 mas 2 é menor que 3 = false

# Tabela verdade do AND

True and True # verdadeiro
True and False # false
False and True # false
False and False # false

# Tabela verdade do OR

True or True # true 
True or False # true
False or True # true
False or False # false

# Tabela verdade do XOR

True != True # false
True != False # true
False != True # true
False != False # false

# Operador de Negação (unário)

not True
not False

not 0
not 1
not not -1
not not True

#Cuidado!

True & False
False | True
True ^ False

# um pouco de realidade

saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
meta

# Desafio Operadores Lógicos

# Os trabalhos
trabalho_terca = False
trabalho_quinta = False

'''
- Confirmado os 2: TV 50' + Sorvete
- Confirmado apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa

'''
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta #xor
mais_saudavel = not sorvete

print('Tv50={} Tv32={} Sorvete={} Saudável{}'. format(tv_50, tv_32, sorvete, mais_saudavel))

# Operadores unários

a = 3
a += 1
a -= 1

# Operadores ternários

esta_chuvendo = True
print (' Hoje estou com as roupas ' + ('secas.' , 'molhadas.') [esta_chuvendo])

print ('Hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.'))

# Mais operadores

# Operador de Membro

lista =[1, 2, 3, 'Ana', 'Carla']

2 in lista
'Ana' not in lista

#Operador de indentidade

x = 3
y = x
z = 3

x is y
y is z
x is not z

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a is lista_b
lista_b is lista_c
lista_a is not lista_c

# Bultins

type(1)

__builtins__.type('Fala Galera!')
__builtins__.print(10/3)

__builtins__. help(__builtins__.dir)
 
# dir([object]) -> lista de strings
dir() # mostrar o que ta dentro do escopo global do builtins

# Convrsão de Tipos

2 + 3
'2' + '3'
2 + '3'
print(2 + '3')

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

print(type(str(a)))

# Coerção automática

10 / 2
type(10 / 2)
10 / 3
10 // 3
type(10 // 3)
10 // 3.3
type(10 // 3.3)

# Tipos Numéricos

dir(int)
dir(float)

a = 5
b = 2.5
a / b 
a + b
a * b

type(a)
type(b)
type(a - b)

b.is_integer()
5.0.is_integer()

dir(int)
int.__add__(2, 3)
2 + 3

(-2).__abs__()

(-3.6).__abs__()
dir(float)
abs(-3.6)

# Decimal

from decimal import Decimal, getcontext
Decimal(1) / Decimal(7)

getcontext().prec = 4 # quantas casas decimais  
Decimal(1) / Decimal(7)

Decimal.max(Decimal(1), Decimal(7)) # qual é maior
dir(Decimal)

# Tipo String

dir(str)
nome = 'Saulo Pedro'
nome
nome[0] # indice para cada letra 
#strings sao imutaveis

# erro de sintaxe 'marca d'agua' 

"Dias D'Avila" == 'Dias D\'Avila'
texto = 'Textos entre apostrófos pode ter "aspas"'

doc = """ texto com multiplas
... linhas"""
print('Texto com multiplas \n... linhas') # \n quebra linhas e \t tab

nome = 'Ana Paula'
nome[0]
nome[6] # começa do inicio da palavra pra direita
nome[-3] # começa do final da palavra pra esquerda
nome[4:] # acessa um intervalo
nome[-5:]
nome[:3] # do inicio ate o intervalo 3, mas o final não entra

nome[2:5] # intervalo

numeros = '123456789'
numeros
numeros[::] # pega todos os numeros
numeros[::2] # vai de 2 em 2
numeros[1::2] # começando do 1 indo de 2 a 2
numeros[::-1] # ao contrário

# Operador membro na String

frase = 'Python é uma linguagem excelente'
'py' not in frase # py não esta na frase?
'ing' in frase # ing está na frase?
len(frase) # tamanho da frase

frase.lower() # colocar toda a frase em minusculo
frase.upper() # colocar toda a frase em maiusculo

frase = frase.upper()

frase.split() # quebrar a frase em espaços
frase.split('E') # quebrando a frase com a letra E

a = '123'
b = 'de Oliveira 4'
a + b
a.__add__(b)

# Listas

lista = []
type(lista)
dir(lista)
help(list)
len(lista) # tamanho da lista
lista.append(1)
lista.append(5) # adicionar valor a lista
lista
len(lista)

nova_lista = [1, 5, 'Ana', 'Bia']
nova_lista
nova_lista.remove(5) # removendo o item 5 e não o indice 5
nova_lista.reverse() # reverte a ordem da lista

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
lista.index('Guilherme')

lista[2]
1 in lista
'Rebeca' in lista
'Pedro' not in lista

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
lista[1:3]# o 3 não entra, vai ate o 2
lista[1:-1] 
lista[1:]
lista[:-1]
lista[:]
lista[::2]
lista[::-1]
del lista[2] # elimina o indice 2
del lista[1:]

# Tupla - não pode ser modificada

tupla = tuple()
tupla = ()
typle(tupla)
tupla = ('um',) # quando houver apenas 1 elemento, colocar virgula no final
tupla[0] # acessar elementos da tuple
cores = ('verde', 'amarelo', 'azul', 'branco')

cores.index('amarelo') # posição de amarelo na tupla
cores.count('azul') # quantos elementos de azul tem na tupla
len(cores)

# Dicionarios - chaves e valor

pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
type(pessoa)
len(pessoa) # quantidade de pares

pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]

pessoa.keys() #  pegar as chaves
pessoa.values () # pegar os valores
pessoa.items() # pegar os itens
pessoa.get('idade')

pessoa = {'nome' : 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa.pop('idade') # lê o valor e remove do dicionário
pessoa.update({'idade': 40, 'sexo': 'M'}) # adicionar index
del pessoa['cursos']
pessoa.clear() # limpa todo o dicionário

# Conjuntos

a = {1, 2, 3}
type(a)
a = set('cod3r') # cria um conjunto com essas letras
print('3' in a, 4 not in a)

{1, 2, 3} == {3, 2, 1, 3} # são iguais

#operacoes

c1= {1, 2}
c2= {2, 3}
c1.union(c2) # união dos 2 conjuntos, cria um terceiro conjunto
c1. intersection(c2) # pega oq sao comum entre os 2 conjuntos
c1.update(c2) # altera o conjunto 1 a partir dos elementos do conjunto 2

c2 <= c1 # c2 é subconjunto de c1? sim
c1 >= c2 # c1 é superconjunto de c2? sim

{1, 2, 3} - {2} # pega a diferença dos 2 conjuntos

# Interpolar

nome, idade = 'Ana', 30

print('Nome: %s Idade: %d' % (nome, idade)) # %s pra string . %d para inteiros.
print('Nome: {0} Idade: {1}' .format(nome, idade))











  














 
 


 










 

