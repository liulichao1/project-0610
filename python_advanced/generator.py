list_a = list(range(1, 11))

print(list_a)

list_a = [x ** 2 for x in range(1, 11)]

g_a = (x ** 2 for x in range(1, 5))

print(list_a)
print(type(g_a))

# print(next(g_a))
print(next(g_a))
print(next(g_a))
print(next(g_a))
print(next(g_a))

for n in g_a:
    print('n:',n)

