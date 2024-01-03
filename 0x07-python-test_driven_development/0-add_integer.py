#!/usr/bin/python3

"""
	this  module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
	"""
	Function that adds two integer and/ or numbers
	
	args:
		a: first number
		b: second number
	Returns:
		the addition of the twi numbers
	
	Raises:
		TypeError: if a or b aren't integer and /or numbers

"""

	if not isinstance(a, int) and not isinstance(a,float):
		raise TypeError("a must be an integer")
	if not isinstance(b,int) and not isinstance(a,float)
		raise TypeError("b must be an integer")
	a = int(a)
	b = int(b)
	return (a+b)


