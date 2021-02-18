# Função principal
def main():
	x = float(input('Informe um número real: '))
	x2 = float(input('Informe o valor da aproximação do número anterior: '))

	print('O valor do erro ABSOLUTO é, aproximadamente: {:.8f}'.format(erro_abs(x, x2)))
	print('O valor do erro RELATIVO é, aproximadamente: {:.8f}'.format(erro_relativo(x, x2)))


# Função que calcula o erro relativo:
def erro_relativo(x, x2):
	if (x == 0):
		print('AVISO: não é possível calcular o erro relativo, pois o primeiro número informado deve ser DIFERENTE de zero')
	else:
		if ((x - x2) < 0):
			modulo = (x - x2)*(-1)
			e = modulo/x
		else:
			modulo = (x - x2)
			e = modulo/x

	return(e)


# Função que calcula o erro absoluto:
def erro_abs(x, x2):
	if ((x - x2) < 0):
		modulo = (x - x2)*(-1)
	else:
		modulo = (x - x2)

	return(modulo)


# Chamada à função principal:
if __name__ == '__main__':
	main()