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
