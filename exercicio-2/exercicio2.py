class nodo:
    def __init__(self, info):
        self.info = info
        self.proxNo = None

class fila_encadeada():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def inserir(self, nodo):
        if not self.primeiro:
            self.primeiro = nodo
            self.ultimo = nodo
            return
        self.ultimo.proxNo = nodo
        self.ultimo = nodo
        return
    
    def comprimento(self):
        comp = 0
        atualf = self.primeiro
        while atualf:
            atualf = atualf.proxNo
            comp+=1
        print("Comprimento da fila: {}".format(comp))
       
    def imprimir(self):
        if not self.primeiro:
            print("Fila vazia")
            return
        atualf = self.primeiro
        while atualf:
            print(atualf.info, end = ' ')
            atualf = atualf.proxNo
        print()
        
class lista_encadeada():
    def __init__(self):
        self.raiz = None

    def insereNoInicio(self, nodo):
        if not self.raiz:
            self.raiz = nodo
            return
        nodo.proxNo = self.raiz
        self.raiz = nodo

    def insereNoFinal(self, nodo):
        if not self.raiz:
            self.raiz = nodo
            return
        atual = self.raiz
        while atual.proxNo:
            atual = atual.proxNo
        atual.proxNo = nodo

    def removerDoInicio(self):
        if not self.raiz:
            return print("Lista já está vazia!")
        self.raiz = self.raiz.proxNo

    def varrer(self):
        while self.raiz:
            self.raiz = self.raiz.proxNo
            
    def imprimir(self):
        atual = self.raiz
        while atual:
            print(atual.info, end = ' ')
            atual = atual.proxNo
        print()
        return
    
    def imprimirRec(self):
        if self.raiz:
            print(self.raiz.info, end = ' ')
            aux = self.raiz  #para não perder o valor do self.raiz
            self.raiz = self.raiz.proxNo
            self.imprimirRec()
            self.raiz = aux
            aux = None
        else:
            print()
        
    def ordem(self):
        atual = self.raiz
        while atual.proxNo:
            if atual.info<=atual.proxNo.info:
                atual = atual.proxNo
                continue
            else:
                return print("Lista nao esta em ordem crescente!")
        print("Lista esta em ordem crescente!")

    def copiaVet(self, vet):
        for i in range(len(vet)):
            self.insereNoFinal(nodo(vet[i]))

    def copiaVetRec(self, vet, i): 
        if (i==len(vet)):
            return
        else:
            self.insereNoFinal(nodo(vet[i]))
            i+=1
            self.copiaVetRec(vet,i)
            
    def contarCelulas(self):
        atual = self.raiz
        cont = 0
        while atual:
            atual = atual.proxNo
            cont+=1
        print("Qtd de celulas: {}".format(cont))

    def contarRec(self, cont):
        if self.raiz:
            cont+=1
            aux = self.raiz
            self.raiz = self.raiz.proxNo
            self.contarRec(cont)
            self.raiz = aux
            aux = None
        else:
            print('Qtd de celulas (Rec): {}'.format(cont))  

    def copia(self):
        atual = self.raiz
        lista2 = lista_encadeada()
        while atual:
            lista2.insereNoFinal(nodo(atual.info))
            atual = atual.proxNo
        print('Nova lista:', end = " ")
        lista2.imprimir()

    def copiaRec(self , lista2):
        if self.raiz:
            lista2.insereNoFinal(nodo(self.raiz.info))   
            aux = self.raiz
            self.raiz = self.raiz.proxNo
            self.copiaRec(lista2)
            self.raiz = aux
        else:
            print('Nova lista (Rec):', end = ' ')
            lista2.imprimir()
            
    def trocarPos(self, ind, ind2):
        atual = self.raiz
        valor1 = 0
        valor2 = 0
        if ind>ind2:
            for i in range(ind+1):
                if i==ind:
                    valor1 = atual.info
                if i==ind2:
                    valor2 = atual.info
                atual = atual.proxNo
        else:
            for i in range(ind2+1):
                if i==ind:
                    valor1 = atual.info
                if i==ind2:
                    valor2 = atual.info
                atual = atual.proxNo
        atual = self.raiz
        n = 0
        while atual:
            if n==ind:
                atual.info = valor2
            if n==ind2:
                atual.info = valor1
            atual = atual.proxNo
            n+=1
        
    def endereco(self):
        n = 0
        atual = self.raiz
        while atual:
            atual = atual.proxNo
            n+=1
        atual = self.raiz
        for i in range(int(n/2)):
            atual = atual.proxNo
        print('Endereço do valor mais proximo do meio: {}'.format(atual))

    def conteudoMinimo(self):
        atual = self.raiz
        menor = atual.info
        while atual:
            if atual.info<menor:
                menor = atual.info
            atual = atual.proxNo
        print('Conteudo minimo: {}'.format(menor))

    def conteudoMinRec(self, menor):
        if self.raiz:
            aux = self.raiz
            self.raiz = self.raiz.proxNo
            if aux.info<menor:
                menor = aux.info
            self.conteudoMinRec(menor)
            self.raiz = aux
        else:
            print('Conteudo minimo (Rec): {}'.format(menor))

print('***Lista Encadeada***')
lista = lista_encadeada()
lista.insereNoInicio(nodo(2))
lista.insereNoInicio(nodo(4))
lista.insereNoInicio(nodo(0))
lista.insereNoFinal(nodo(6))
lista.insereNoFinal(nodo(7))
lista.insereNoFinal(nodo(8))
lista.imprimir()
lista.ordem()
lista.contarCelulas()
lista.removerDoInicio()
lista.removerDoInicio()
lista.imprimir()
lista.ordem()
lista.contarCelulas()
lista.varrer()
vetor = [7,2,5,6]
lista.copiaVet(vetor)
lista.imprimir()
lista.copia()
lista.trocarPos(3,1)
lista.imprimir()
lista.endereco()
lista.conteudoMinimo()
cont = 0
lista.contarRec(0)
lista.imprimirRec()
listaa = lista_encadeada()
lista.copiaRec(listaa)
lista.varrer()
vetor2 = [5,6,3,2]
lista.copiaVetRec(vetor2,0)
lista.imprimir()
lista.conteudoMinRec(9999999999)

print('***Fila Encadeada***')
fila = fila_encadeada()
fila.inserir(nodo(1))
fila.inserir(nodo(4))
fila.inserir(nodo(1))
fila.inserir(nodo(0))
fila.imprimir()
fila.comprimento()


