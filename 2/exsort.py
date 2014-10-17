a=['a.c','b.py','c.c','r.txt','m.py']
def exsort(a):
	b=[]
	for i in a:
		b.append(i.strip('*.'))
	return b
print exsort(a)
