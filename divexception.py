def div(a, b):
	try:
		return a/b
	except ZeroDivisionError:
		print("Can not divide by zero")
		return ""
	except TypeError:
		print("Unsupported type. Did you use string?")
		return ""


print(div(10,2))
print(div(3,0))
print(div(9,3))
print(div("4",5))
print(div("4",0))
