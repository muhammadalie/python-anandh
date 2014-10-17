a=[3,5,1,4]
def max(a):
	x=a[0]
	for i in a:
		if i>x:x=i		
	return x
print max(a)
