def treemap(fun,obj,n=None):
	if n is None:
		n=[]

	for i in obj:
		if isinstance(i,list):
			n.append(treemap(fun,i))
			
		else:
			n.append(fun(i))
	return n

print treemap(lambda x: x*x,[1, 2, [3, 4, [5]]])
