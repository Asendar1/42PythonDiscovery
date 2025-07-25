def NULL_not_found(object : any) -> int:
	if object is None:
		print(f"{type(object).__name__}: {object} {type(object)}")
		return 0
	if type(object).__name__ == "float":
		print(f"{type(object).__name__}: {object} {type(object)}")
		return 0
	if type(object).__name__ == "int":
		print(f"{type(object).__name__}: {object} {type(object)}")
		return 0
	if type(object).__name__ == "str" and object == "":
		print(f"{type(object).__name__}: {object} {type(object)}")
		return 0
	if object is False:
		print(f"{type(object).__name__}: {object} {type(object)}")
		return 0
	else:
		print("Type not found")
		return 1

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
