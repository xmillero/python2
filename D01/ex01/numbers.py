def p1():
	file = 'numbers.txt'

	with open(file, 'r') as f:
		for line in f:
			r = line.replace(',', '\n')
			print (r)

if __name__ == '__main__' :
	p1()