def prod(m,n):
	if(cmp(m,n)==1):
		if n==0: return n
		return m+prod(m,n-1)
	else:
		if m==0: return m
		return n+prod(m-1,n)

print prod(9,17)
