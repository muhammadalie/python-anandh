def revline(a):
	f=open(a).readlines()
	for i in f:
		print i[::-1]
