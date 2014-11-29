def permute(a,r=None):
	if r is None:
		r=[]
	for i in a:
		permute(r.append(i))
		
		
	return r	

print permute([1,2,3])
