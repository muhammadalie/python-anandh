def reverse(a,r=None):
	if r is None:
		r=[]		
	for i in a[::-1]:
		if isinstance(i,list):
			r.append(reverse(i))
		else:
			r.append(i)
		
	return r	

print reverse([[1, 2], [3, [4, 5]], 6])
