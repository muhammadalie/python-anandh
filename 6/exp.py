def exp(n,m):
	if m==0:return 1
	else:return n*exp(n,m-1)

print exp(2,1200)

