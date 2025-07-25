import sys

def check_even_odd(value):
	if value % 2 == 0:
		print("Value is even")
	else:
		print("Value is odd")

if len(sys.argv) > 2:
	print("AssertionError: More than one argument given")
elif len(sys.argv) == 2:
	try:
		value = int(sys.argv[1])
		check_even_odd(value)
	except ValueError:
		print("AssertionError: Argument is not an integer")
