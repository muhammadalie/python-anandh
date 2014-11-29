def rev(a):
	f=open(a)
	g=f.readlines()
	for i in range(len(g)):
		 print g[-(i+1)]
