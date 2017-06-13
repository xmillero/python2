def my_var():
	a = 42
	msg = "est de type"
	print(a, msg, type(a))

	a = "42"
	msg = "est de type"
	print(a, msg, type(a))

	a = "quarante-deux"
	msg = "est de type"
	print(a, msg, type(a))

	a = 42.0
	msg = "est de type"
	print(a, msg, type(a))

	a = True
	msg = "est de type"
	print(a, msg, type(a))

	a = [42]
	msg = "est de type"
	print(a, msg, type(a))

	a = {42: 42}
	msg = "est de type"
	print(a, msg, type(a))

	a = (42, )
	msg = "est de type"
	print(a, msg, type(a))

	a = set()
	msg = "est de type"
	print(a, msg, type(a))

if __name__ == '__main__' :
	my_var()