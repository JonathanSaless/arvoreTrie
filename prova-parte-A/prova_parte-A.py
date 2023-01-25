class nodo:
    def __init__(self, info):
        self.info = info

class lista_sequencial_circ:
    
    def __init__(self,tamanhoMax):
        self.lista = []
        self.indice = 0
        self.tamanho = tamanhoMax-1
        
    def inserirNoInicio(self, nodo):
        if self.indice>self.tamanho:
            print("Lista esta cheia!")
            return
        if self.indice==0:
            self.lista.append(None)
            self.lista[self.indice] = nodo
            self.indice+=1
            return
        for i in range(self.indice,-1,-1):
            if i == 0:
                self.lista.append(None)
                self.lista[i]=nodo
                self.indice+=1
                return
            self.lista[i] = self.lista[i-1]
            
    
    def inserirNoFinal(self, nodo):
        if self.indice>self.tamanho:
            print("Lista esta cheia!")
            return
        self.lista.append(None)
        self.lista[self.indice] = nodo
        self.indice+=1
        self.lista.append(None)
        self.lista[self.indice] = self.lista[0]
        

    def remover(self, info):
        if not self.lista:
            print('Lista Vazia\nNão há o que ser removido')
            return
        i=0
        while self.lista[i].info!=info:
            i+=1
            if self.lista[i]==self.lista[0]:
                print('Conteúdo não existe!')
                return
        self.indice-=1    
        for j in range(i,self.indice):
            self.lista[j] = self.lista[j+1]
        self.lista[self.indice] = self.lista[0]

    def buscaPosicao(self,i , conteudo):
        if self.indice==i:
            print("Valor nao encontrado")
            return
        if self.indice == 0:
            print("lista vazia")
            return
        else:
            if self.lista[i].info == conteudo:
                print("posicao:",i)
                return
            else:
                lista.buscaPosicao(i+1,conteudo)
        
    
    def imprimir(self):        
        for i in range(self.indice):
            print(self.lista[i].info, end = ' ')   
        print()

    def imprimirLista(a, n, ind): 
        aux = ind 
      
        while aux < n + ind : 
            print(a[(i % n)], end = " ") 
            aux = aux + 1

lista = lista_sequencial_circ(5)
lista.inserirNoInicio(nodo(99))
lista.inserirNoFinal(nodo(5))
lista.inserirNoFinal(nodo(10))
lista.inserirNoFinal(nodo(1))
lista.inserirNoFinal(nodo(41))
lista.inserirNoFinal(nodo(14))
lista.imprimir()
lista.remover(10)
lista.imprimir()
lista.remover(1)
lista.imprimir()
lista.inserirNoInicio(nodo(9))
lista.imprimir()
lista.buscaPosicao(0,41)