class Test(object):

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            t = self.i
            self.i = self.i + 1
            return t
        else:
            raise StopIteration('StopIteration...')


o = Test(10)


for i in o:
    print(i)
