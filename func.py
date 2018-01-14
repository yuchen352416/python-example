import math

def cipher(a, b, c):
	if not isinstance(a,(int, float)):
		raise TypeError("a is not number!")
	elif a == 0:
		raise TypeError("a is zero")
	if not isinstance(b,(int, float)):
		raise TypeError("b is not number!")
	if not isinstance(c,(int, float)):
		raise TypeError("c is not number!")
	flag = b * b - 4 * a * c
	if flag < 0:
		return None
	elif flag == 0: 
		return -b / (2 * a)
	else:
		number1 = (-b + math.sqrt(flag)) / (2 * a)
		number2 = (-b - math.sqrt(flag)) / (2 * a)
		return (number1, number2)
