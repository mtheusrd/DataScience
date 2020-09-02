# Calculadora do Theuzin
# Menu Inicial
print('**************************************************')
print('*       BEM VINDO A CALCULADORA DO THEUZIN       *')
print('*------------------------------------------------*')
print('*       ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS       *')
print('*             1 - ADICAO                         *')
print('*             2 - SUBTRACAO                      *')
print('*             3 - DIVISÃO                        *')
print('*             4 - MULTIPLICACAO                  *')
print('*             0 - SAIR DO SISTEMA                *')
print('************************************************** \n \n')

# Escolha da Opção
opcao = int(input('Qual operação você deseja fazer?  '))

if opcao == 1:
	num1 = int(input('Digite o primeiro número: ')) 
	num2 = int(input('Digite o segundo número: '))
	total = num1 + num2
	print('O Resultado final foi : %d' %total)
elif opcao == 2:
	num1 = int(input('Digite o primeiro número: ')) 
	num2 = int(input('Digite o segundo número: '))
	total = num1 - num2
	print('O Resultado final foi : %d' %total)
elif opcao == 3:
	num1 = float(input('Digite o primeiro número: ')) 
	num2 = float(input('Digite o segundo número: '))
	total = num1 / num2
	print('O Resultado final foi : %.2f' %total)
elif opcao == 4:
	num1 = int(input('Digite o primeiro número: ')) 
	num2 = int(input('Digite o segundo número: '))
	total = num1 * num2
	print('O Resultado final foi : %d' %total)
elif opcao == 0:
	exit()
else: print('Opção Inválida! ')
