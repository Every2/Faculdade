import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self, capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('o vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
    
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('capacidade maxima atingida')
            return
        
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        
        