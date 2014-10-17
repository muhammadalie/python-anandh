
cube = lambda x: x ** 3
fxy = lambda f,x,y: f(x)+f(y)
#print cube(2)
print fxy(cube, 2, 3)

print fxy(lambda x: x ** 3, 2, 3)

