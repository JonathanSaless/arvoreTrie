#
#    Implementação de Árvore Binária em Python 3
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
# Essa classe será utilizada na árvore bináriaria. Ela contém um atributo para a
# informação (info), outro para indicar o nodo pai (nodoPai), e dois ponteiros
# para indicar o nó filho da esquerda e o nó filho da direita
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
        
        # Ponteiro para o nodo filho da esquerda
        self.nodoFilhoEsquerda = None
        
        # Ponteiro para o nodo filho da direita
        self.nodoFilhoDireita = None
        

#
# Classe Árvore Binária
#
# Esta classe implementa uma Árvore Binária com alocação encadeada em Python 3.
# Nesse tipo de estrutura, o número máximo de filhos que um nodo pode ter é 2.
# Assim, a árvore assume uma topologia onde ela pode ser visualizada como
# dividida entre esquerda e direita, para qualquer nodo que se observa. Os
# métodos implementados são de inserção na raiz e geral, remoção, busca e
# impressão. Maiores detalhes sobre cada método estão em suas respectivas
# descrições.
#

# Definição da classe ArvoreBinaria
class ArvoreBinaria:
    
    # Método construtor
    def __init__(self):
        
        # Ponteiro para o primeiro nodo raiz da árvore
        # do qual todos os demais derivarão
        self.raiz = None
    
    # Função para inserção de nodo na raiz da árvore
    # Como é uma árvore binária, permitiremos que o nodo raiz seja inserido
    # apenas uma vez e não possa ser modificado
    #
    # nodo - nodo a ser inserido na fila
    def insereNodoRaiz(self, nodo):
        
        # Se a raiz é None, quer dizer que a árvore é vazia.
        # Então apenas coloca-se o nodo na raiz da árvore.
        if not self.raiz:
            self.raiz = nodo
        
        # Caso contrário, a raiz já existe e impedimos-na de ser modificada
        else:
            print('ERROR\nÁrvore já tem raiz!')
                
        return
    
    # Função para inserção de nodos na árvore
    # No caso, é necessário saber qual nodo será inserido, qual será o nodo
    # pai, e se o nodo a ser inserido ficará na esquerda ou direita do pai
    #
    # nodo - nodo a ser inserido na árvore
    # nodoPai - nodo que será o pai do nodo a ser inserido
    # lado - lado onde o nodo será inserido: 0 para a esquerda, 1 para a direita
    def insereNodo(self, nodo, nodoPai, lado):
        
        # A chamada abaixo faz uso da função buscaInfo para verificar se o
        # nodoPai existe na árvore. Caso não, não é possível processar a
        # operação.
        if not self.buscaInfo(nodoPai.info):
            print('ERROR\nNodo tem filhos!')
            return
        
        # Se o nodoPai existe, verifica-se se o lado a ser adicionado está
        # vazio. Caso sim, o nodo pode ser adicionado àquele lado.
        if lado == 0 and nodoPai.nodoFilhoEsquerda == None:
            nodo.nodoPai = nodoPai
            nodoPai.nodoFilhoEsquerda = nodo
        elif lado == 1 and nodoPai.nodoFilhoDireita == None:
            nodo.nodoPai = nodoPai
            nodoPai.nodoFilhoDireita = nodo
        else:
            print('ERROR\nLado do nodoPai já ocupado!')
        
        return

    # Função para remover de nodos na árvore
    # No caso, foi desenvolvido apenas a remoção de nodos folha da árvore.
    # Outros tipos de nodos não serão removidos.
    #
    # nodo - nodo a ser removido da árvore
    def removeNodo(self, nodo):
        
        # Verifica se o nodo tem filhos - caso sim, ele não pode ser removido
        if nodo.nodoFilhoDireita or nodo.nodoFilhoEsquerda:
            print('ERROR\nNodo tem filhos!')
        
        # Caso não tenha filhos, é um nodo folha e portanto pode ser removido
        else:
            if nodo.nodoPai.nodoFilhoDireita == nodo:
                nodo.nodoPai.nodoFilhoDireita = None
            else:
                nodo.nodoPai.nodoFilhoEsquerda = None
            
            nodo.nodoPai = None
        
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
            
        # Verifica-se se o nodo já tem a informação buscada. Caso sim,
        # suspende-se a busca nesse ponto.
        if nodo.info == info:
            return True
        
        # Caso a informação buscada não esteja lá, verifica se o nodo tem
        # nodoFilhoEsquerda e, caso afirmativo, envia-o recursivamente para
        # a função
        if nodo.nodoFilhoEsquerda:
            resultado = self.buscaInfo(info, nodo.nodoFilhoEsquerda)
        
        # Se o resultado na busca a esquerda for positivo, retorna a função
        # obteve sucesso
        if resultado:
            return resultado
        
        # Caso a informação não esteja nos nós da esquerda, verifica-se o nó da
        # direita, que caso exista será passado recursivamente para a função
        if nodo.nodoFilhoDireita:
            resultado = self.buscaInfo(info, nodo.nodoFilhoDireita)
        
        # Finaliza a função caso tenha sido achado o valor no lado direito
        # (retornando True) ou caso não tenha sido encontrado na estrutura
        # (False)
        return resultado

    # Função para imprimir o conteúdo de todos os nodos da árvore
    # Aqui é implementada uma busca em profundidade, da esquerda para a direita.
    # A implementação é feita de maneira recursiva.
    def imprimeArvore(self, nodo = ''):
        
        if nodo == '':
            nodo = self.raiz
        
        print(nodo.info, end = ' ')
        
        if nodo.nodoFilhoEsquerda:
            self.imprimeArvore(nodo.nodoFilhoEsquerda)
        
        if nodo.nodoFilhoDireita:
            self.imprimeArvore(nodo.nodoFilhoDireita)
        
        if nodo == self.raiz:
            print()
        
        return
