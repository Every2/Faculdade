def constant(n):
    print(n[0])

def linear(n):
    for i in n:
        print(i)

def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)

def combination(n):
    print(n[0])

    for i in range(5):
        print('test', i)

    for i in n:
        print(i)
        
    for i in n:
        print(i)

    print('Python')
    print('Python')
    print('Python')

lista = [1, 2, 3, 4]
constant(lista)
linear(lista)
quadratic(lista)
combination(lista)
