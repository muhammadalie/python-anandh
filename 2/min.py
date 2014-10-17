a=[3,2,1,4]
def min(a):
	x=a[0]
	for i in a:
		if i<x:x=i		
	return x
print min(a)
