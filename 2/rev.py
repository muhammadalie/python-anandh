a=[1,2,3,4]
def rev(a):
	b=[]
	for i in range(1,len(a)+1):
		b.append(a[-i])
	return b
print rev(a)	
