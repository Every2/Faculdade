import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
    
    def insere(self, valor):
        if self.ultima_posicao is self.capacidade - 1:
            print('Capacidade máxima foi atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

vetor = VetorNaoOrdenado(5)
vetor.insere(2)
vetor.insere(4)
vetor.insere(7)
vetor.insere(8)
vetor.pesquisar(2)