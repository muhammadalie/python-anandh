def tail(a):
	f=open(a).readlines()
	for i in range(1,11):
		print f[-i]
