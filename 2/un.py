a=["python", "java", "Python", "Java"]
#a=[1,3,4,5]
def lensort(a):
	a.sort(key=lambda s:s.lower())
	return
lensort(a)
def uni(a):
	lensort(a)
	b=[] 
	j=-1
	for i in a:
		b.append(i)
		j+=1
		#b[0]=i
			
	return b 

print uni(a) 
