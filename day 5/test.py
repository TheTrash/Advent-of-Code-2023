funcs = []
for i in range(10):
    funcs.append(lambda x, i=i: x+i)


print(funcs[-1](5))
print(funcs[1](5))