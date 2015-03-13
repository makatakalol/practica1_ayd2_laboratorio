def suma(valor1,valor2):
	if validar_numero(valor1) == 0 and validar_numero(valor2) == 0:
		total = valor1+valor2
		return total
	else:
		return "error"

def resta(valor1,valor2):
	total = valor1-valor2
	return total

def multiplicacion(valor1,valor2):
	total = valor1*valor2
	return total

def division(valor1,valor2):
	if valor2 == 0:
		return "error"
	else:
		total = valor1/valor2
		return total

def validar_numero(val): #funcion para validar que el valor es numerico
	valor = str(val)
	largo = len(valor)
	numeros = 0
	nonumeros = 0
	for x in range(largo):
		if 47<ord(valor[x])<57 or ord(valor[x])==45:
			numeros += 1
		else:
			nonumeros += 1
	return nonumeros
