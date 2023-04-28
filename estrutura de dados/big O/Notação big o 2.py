def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

def lista2():
    return range(1000)

l = lista2()
for i in l:
    print(i)

print(lista1())