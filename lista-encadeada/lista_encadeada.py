#FILA ENCADEADA
#NÃO CONSEGUIR FAZER AS DE RECURSIVIDADES
class nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

class fila_encadeada():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def inserir(self, nodo):
        if not self.primeiro:
            self.primeiro = nodo
            self.ultimo = nodo
            return
        self.ultimo.prox = nodo
        self.ultimo = nodo
        return
    def excluir(self):
        if not self.primeiro:
            print("Fila vazia")
            return 
        aux = self.primeiro.prox
        self.primeiro.prox = None
        self.primeiro = aux
        return
    def imprimir(self):
        if not self.primeiro:
            print("Fila vazia")
            return
        atual = self.primeiro
        while atual:
            print(atual.info, end = ' ')
            atual = atual.prox
        return 
    def contar(self):
        i = 0
        atual = self.primeiro
        while True:
            if atual==None:
                print()
                return print("Tamanho: {}".format(i))            
            atual = atual.prox
            i+=1

    def altura(self, item):
        i = 0
        maximo=0
        atual = self.primeiro
        while atual:            
            atual = atual.prox
            maximo+=1
        atual = self.primeiro
        while True:
            i+=1
            if item == atual.info:
                return print("Altura: {}".format(maximo-i))
            atual = atual.prox

    def profundidade(self, item):
        i = 0
        atual = self.primeiro
        while True:
            i+=1
            if item == atual.info:
                return print("Profundidade: {}".format(i-1))
            atual = atual.prox

    def crescente(self):    
        atual = self.primeiro
        while atual:
            if not atual.prox:
                break
            if (atual.info>atual.prox.info):
                return print("Lista não está em ordem crescente!")          
            atual = atual.prox
        print("Lista está em ordem crescente!")

    def comparar(self, fila2):
        lista1 = self.primeiro
        lista2 = fila2.primeiro
        while lista1:
            if not lista2:
                break
            if lista1.info == lista2.info:
                lista1 = lista1.prox
                lista2 = fila2.primeiro
                continue
            lista2 = lista2.prox
        if not lista1:
            print("Listas são iguais!")        
        else:
            print("Listas são diferentes!")
         
        
fila = fila_encadeada()
fila2 = fila_encadeada()
fila.inserir(nodo(3))
fila.inserir(nodo(5))
fila.inserir(nodo(7))
fila.inserir(nodo(10))
fila.inserir(nodo(54))
fila2.inserir(nodo(54))
fila2.inserir(nodo(3))
fila2.inserir(nodo(5))
fila2.inserir(nodo(10))
fila2.inserir(nodo(7))
fila.imprimir()
print()
fila2.imprimir()
fila.contar()
fila.altura(7)
fila2.altura(7)
fila.profundidade(7)
fila2.profundidade(7)
fila.crescente()
fila2.crescente()
fila.comparar(fila2)
