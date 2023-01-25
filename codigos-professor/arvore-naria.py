#
#    Implementação de Árvore N-Ária em Python 3
#    Copyright (C) 2017, Filipe Saraiva <saraiva@ufpa.br>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#
# Classe Nodo
#
# Implementa um Nodo, uma classe simples que guarda qualquer informação
#
# Essa classe será utilizada na árvore N-Ária. Ela contém um atributo para a
# informação (info), outro para indicar o nodo pai (nodoPai), e uma lista
# para guardar os nodos filhos dela (nodoFilhos)
#

# Definição da classe Nodo
class Nodo:
    
    #Método construtor
    def __init__(self, info):
        
        # O argumento 'info' representa uma infomação
        # qualquer a ser aplicada na classe Nodo
        self.info = info
        
        # O atributo nodoPai guarda o nodo exatamente anterior (um nível acima)
        # a qual o nodo criado se relaciona
        self.nodoPai = None
        
        # Uma lista inicialmente vazia com todos os nodos filhos desse nodo
        self.nodosFilhos = []
        

#
# Classe Árvore N-Ária
#
# Esta classe implementa uma Árvore N-Ária com alocação encadeada em Python 3.
# Nesse tipo de estrutura, não há limite para o número de filhos que dado nodo
# pode ter na árvore (daí o termo "N-Ária"). Os métodos implementados são de
# inserção na raiz e geral, remoção, busca e impressão. Maiores detalhes sobre
# cada método estão em suas respectivas descrições.
#

# Definição da classe ArvoreNAria
class ArvoreNAria:
    
    # Método construtor
    def __init__(self):
        
        # Ponteiro para o primeiro nodo raiz da árvore
        # do qual todos os demais derivarão
        self.raiz = None
    
    # Função para inserção de nodos na raiz da árvore
    #
    # nodo - nodo a ser inserido na fila
    def insereNodoRaiz(self, nodo):
        
        # Se a raiz é None, quer dizer que a árvore é vazia.
        # Então apenas coloca-se o nodo na raiz da árvore.
        if not self.raiz:
            self.raiz = nodo
        
        # Caso contrário, a raiz anterior se tornará filha da nova raiz.
        # Essa operação é realizada com os comandos abaixo
        else:
            self.raiz.nodoPai = nodo
            nodo.nodosFilhos.append(self.raiz)
            self.raiz = nodo
                
        return
    
    # Função para inserção de nodos na árvore
    # No caso, é necessário saber qual nodo será inserido e qual será o nodo
    # pai desse nodo. Todas essas informações devem ser providas na chamada da
    # função
    #
    #
    # nodo - nodo a ser inserido na árvore
    # nodoPai - nodo que será o pai do nodo a ser inserido
    def insereNodo(self, nodo, nodoPai):
        
        # A chamada abaixo faz uso da função buscaInfo para verificar se o
        # nodoPai existe na árvore. Caso não, não é possível processar a
        # operação.
        if not self.buscaInfo(nodoPai.info):
            print('nodoPai não existe!')
            return
        
        # Se o nodoPai existe, basta configurá-lo para ser o pai do
        # nodo a ser inserido e atribuir o nodo a ser inserido como
        # filho do nodo pai
        nodo.nodoPai = nodoPai
        nodoPai.nodosFilhos.append(nodo)
        
        return

    # Função para remover de nodos na árvore
    # No caso, foi desenvolvido apenas a remoção de nodos folha da árvore.
    # Outros tipos de nodos não serão removidos.
    #
    # nodo - nodo a ser removido da árvore
    def removeNodo(self, nodo):
        
        # Verifica se o nodo tem filhos - caso sim, ele não pode ser removido
        if nodo.nodosFilhos:
            print('ERROR\nNodo tem filhos!')
        
        # Caso não tenha filhos, é um nodo folha e portanto pode ser removido
        else:
            # Nos comandos abaixo é buscado o índice do nodo a ser removido na
            # lista de filhos do nodo pai dele
            posicao = 0
            for encontraNodo in nodo.nodoPai.nodosFilhos:
                if encontraNodo != nodo:
                    posicao += 1
                else:
                    break
            
            # Encontrado o índice, deslocamos-no para o final da lista
            for i in range(posicao, len(nodo.nodoPai.nodosFilhos) - 1):
                nodo.nodoPai.nodosFilhos[i], nodo.nodoPai.nodosFilhos[i + 1] = nodo.nodoPai.nodosFilhos[i + 1], nodo.nodoPai.nodosFilhos[i]
            
            # Aqui ocorre a remoção propriamente
            nodo.nodoPai.nodosFilhos.pop()
        
        return

    # Função para buscar uma informação na árvore
    # Aqui é implementada uma busca em profundidade, da esquerda para a direita.
    # A implementação é feita de maneira recursiva.
    #
    # info - informação a ser buscada na árvore
    # nodo - 'nodo base' da função, utilizado apenas nas chamadas recursivas
    def buscaInfo(self, info, nodo = ''):
        
        # resultado aqui funciona como uma variável para checar se a informação
        # foi encontrada ou não
        resultado = False
        
        # Na primeira chamada da função nodo passará a ser a raiz da árvore
        if nodo == '':
            nodo = self.raiz
        
        # Verifica-se se o nodoAtual já tem a informação buscada. Caso sim,
        # suspende-se a busca nesse ponto.
        nodoAtual = nodo
        if nodoAtual.info == info:
            return True
        
        # Nesse caso busca-se recursivamente pelos filhos do nodoAtual a
        # informação desejada. Se for encontrado, resultado será True e
        # a busca pode ser suspensa.
        for i in nodoAtual.nodosFilhos:
            resultado = self.buscaInfo(info, i)
            if resultado:
                break
        
        return resultado

    # Função para imprimir o conteúdo de todos os nodos da árvore
    # Aqui é implementada uma busca em profundidade, da esquerda para a direita.
    # A implementação é feita de maneira recursiva.
    def imprimeArvore(self, nodo = ''):
        
        if nodo == '':
            nodo = self.raiz
            
        nodoAtual = nodo
        
        if nodoAtual == self.raiz:
            print(nodoAtual.info, end = ' ')
            
        for i in nodoAtual.nodosFilhos:
            print(i.info, end = ' ')
            self.imprimeArvore(i)
        
        if nodoAtual == self.raiz:
            print()
        
        return
