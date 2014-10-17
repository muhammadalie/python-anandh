a=["hello", "ali", "assa"]
def lensort(a):
	a.sort(key=lambda x: len(x))
	return

lensort(a)
print a
