a=[2,4,2,3,3]
def uni(a):
	b=[]
	c=[]
	
	for i in a:
		if i not in b:
			b.append(i)
	print b
print uni(a)
