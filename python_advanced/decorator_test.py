def a_decorator(func):
    def wrapper():
        print(func.__name__, 'before...')
        func()
        print(func.__name__, 'after ...')

    return wrapper


@a_decorator
def f():
    print('function f...')


# a_decorator(f)()
f()


class FooDecorator(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(self.func.__name__, 'before...')
        self.func(*args, **kwargs)
        print(self.func.__name__, 'after...')


@FooDecorator
def foo(*args):
    for arg in args:
        print(arg)


foo('a', 'b', 'c', 1, 2, 3, True, False)