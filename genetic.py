import random


def verificaTriangulo(a1, a2, a3):
	if(a1<a2+a3 and a2<a1+a3 and a3<a2+a1):
		return 1
	else:
		return 0
def verificaRetangulo(a1, a2, a3):
	t1 = (a1*a1) + (a2*a2)
	t2 = (a2*a2) + (a3*a3)
	t3 = (a1*a1) + (a3*a3)

	r1 = t1-(a3*a3)
	r2 = t2-(a1*a1)
	r3 = t3-(a2*a2)

	r1 = abs(r1)
	r2 = abs(r2)
	r3 = abs(r3)

	fitScore = r1+r2+r3

	return fitScore

def fitness(a,b,c):
	a = abs(a)
	b = abs(b)
	c = abs(c)





if __name__ == '__main__':
	
	with open('triangulos.txt', 'w') as file:
		lista = {}
		cont = 0

		while(cont<100):
			
			aresta1 = random.uniform(1, 10)
			aresta2 = random.uniform(1, 10)
			aresta3 = random.uniform(1, 10)


			if(verificaTriangulo(aresta1, aresta2, aresta3)):
				fitScore = verificaRetangulo(aresta1, aresta2, aresta3)
				lista[fitScore] = [aresta1, aresta2, aresta3]
				cont += 1
				file.write(str(aresta1) + ' ' + str(aresta2) + ' ' + str(aresta3) + '\n')
		
		lista = sorted(lista)



	x = 0 
	for item in lista:
		x = x + 1
		print(str(x) + ' ' + str(item))
	