#exploring Collatz sequenze

def collatz(number):
	if number % 2 == 0: #even number
		result = number // 2 #integer division
	else: #odd number
		result = 3 * number + 1
		
	print(result)
	return result

numero = int(input("Inserisci il numero di cui vuoi visualizzare la successione di Collatz \n"))
risultato = collatz(numero)

while risultato !=1:
	risultato = collatz(risultato)
		
	
