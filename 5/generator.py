def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

pyt=((x,y,z) for z in (integers()) for y in xrange(z) for x in range(y) if 
		x*x+y*y==z*z)

print take(10,pyt)

