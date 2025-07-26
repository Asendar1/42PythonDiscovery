import sys

def string_info(string):
	__doc__ = "Gives info about the string provided"

	upper = 0
	lower = 0
	digit = 0
	space = 0
	pun = 0

	for c in string:
		if (c.isupper()):
			upper += 1
		elif (c.islower()):
			lower += 1
		elif (c.isdigit()):
			digit += 1
		elif (c.isspace()):
			space += 1
		else:
			pun += 1

	print(f"The text contains {len(string)} characters")
	print(f"Uppercase: {upper}")
	print(f"Lowercase: {lower}")
	print(f"Digits: {digit}")
	print(f"Spaces: {space}")
	print(f"Punctuation: {pun}")

if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("AssertionError: More than one argument given")
	elif len(sys.argv) == 2:
		string_info(sys.argv[1])
	elif len(sys.argv) == 1:
		args = input("Please provide a string: ")
		string_info(args)

