a=[1,2,3,4]
def cumu(a):
	b=[]
	p=0
	for i in a:
		p+=i
		b.append(p)
	return b
print cumu(a)
		

