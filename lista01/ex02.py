import math

def main():
    numero = input('Informe o numero: ')
    opcao = int(input('1- ARREDONDAR o número ou 2- TRUNCAR o número? '))
    n_casas = int(input('Quantas casas decimais de precisão? '))

    numero_aprox = separador(numero, opcao, n_casas)
    if (opcao == 1):
    	print('O número correspondente, aproximado por arredondamento é: {:.3f}'.format(numero_aprox))
    else:
    	print('O número correspondente, aproximado por truncamento é: {}'.format(numero_aprox))


# Função que realiza o tratamento inicial do dado, separando a parte inteira
# da parte fracionária:
def separador(n, op, qtd_casas):
	parte_inteira = ""
	parte_fracionaria = ""
	cont = 0
	cont2 = 0

	# pegando a parte inteira do número
	for bit in range(len(n)):
		if (n[bit] == '.'):
			break
		else:
			parte_inteira = parte_inteira + n[bit]
			cont += 1

	# pegando a parte fracionária
	for bit in range(cont+1, len(n)):
		parte_fracionaria = parte_fracionaria + n[bit]
		cont2 += 1

	# bloco para o truncamento:
	if (op == 2):
		frac_auxiliar = truncate(parte_fracionaria, qtd_casas)
		numero_final = parte_inteira + '.' + frac_auxiliar
		return(numero_final)

	# bloco que realiza arredondamento por aproximação com
	# quantidade x de casas decimais:
	num_aprox = round((float(n)), qtd_casas)
	return(num_aprox)


# Função que realiza o truncamento de fato:
def truncate(pt_fracionaria, n_casas):
	frac_auxiliar = ""

	for bit in range(0, n_casas):
		frac_auxiliar = frac_auxiliar + pt_fracionaria[bit]

	return(frac_auxiliar)


# Chamada à função principal
if __name__ == '__main__':
    main()