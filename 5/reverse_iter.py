class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.n > self.i:
            i = self.n
            self.n -= 1
            return i
	else:
            raise StopIteration()

y=yrange(3)
print y.next()
print y.next()
print y.next()
