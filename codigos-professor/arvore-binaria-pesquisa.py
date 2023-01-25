#
#    Implementação de Árvore Binária de Pesquisa em Python 3
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
# Essa classe será utilizada na árvore bináriaria de pesquisa. Ela contém um
# atributo para a informação (info), outro para indicar o nodo pai (nodoPai), e
# dois ponteiros para indicar o nó filho da esquerda e o nó filho da direita
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
        
        # Ponteiro para o nodo filho da esquerda, que para a árvore binária de
        # pesquisa sempre terá a informação menor que a do nodo atual
        self.nodoFilhoEsquerda = None
        
        # Ponteiro para o nodo filho da direita, que para a árvore binária de
        # pesquisa sempre terá a informação maior que a do nodo atual
        self.nodoFilhoDireita = None
        

#
# Classe Árvore Binária de Pesquisa
#
# Esta classe implementa uma Árvore Binária de Pesquisa com alocação encadeada
# em Python 3. Para cada nodo da árvore binária de pesquisa há no máximo 2 nodos
# filhos possíveis. Ao contrário da árvore binária tradicional, na árvore
# binária de pesquisa há relação entre os nodos existentes. No caso, um nodo
# cuja informação é um número inteiro 'x' só poderá ter filhos à esquerda cujos
# valores em suas infos sejam '< x', e apenas terá filhos à direita cujos
# valores sejam '> x'. Com essa árvore é possível fazer buscas mais rápidas,
# pois há uma direcionamento claro, do que em outras estruturas de dados.
# Assim, a árvore assume uma topologia onde ela pode ser visualizada como
# Os métodos implementados são de inserção geral, remoção, busca e impressão.
# Maiores detalhes sobre cada método estão em suas respectivas descrições.
#

# Definição da classe ArvoreBinariaPesquisa
class ArvoreBinariaPesquisa:
    
    # Método construtor
    def __init__(self):
        
        # Ponteiro para o primeiro nodo raiz da árvore
        # do qual todos os demais derivarão
        self.raiz = None
    
    # Função para inserção de nodos na árvore
    # Se a árvore não tiver um nodo raiz, o primeiro nodo a ser inserido será a
    # raiz e a ele caberá particionar a árvore entre menores/maiores nodos que
    # forem inseridos posteriormente.
    #
    # A implementação é realizada de maneira recursiva para que o nodo seja
    # inserido no local correto da árvore, seguindo as relações existentes na
    # árvore binária de pesquisa
    #
    # nodo - nodo a ser inserido na árvore
    # nodoPai - nodo que será o pai do nodo a ser inserido, utilizado apenas
    # internamente pela função
    def insereNodo(self, nodo, nodoPai = ''):
        
        # Se não há raiz, então o nodo a ser
        # inserido será a raiz da árvore
        if not self.raiz:
            self.raiz = nodo
            return
        
        # Caso o nodoPai não tenha sido definido,
        # será utilizado a raiz da árvore
        if nodoPai == '':
            nodoPai = self.raiz
        
        # Nessa instrução verifica-se se o nodo a ser inserido tem uma info
        # menor que a info do nodoPai - caso sim, ele terá que ser inserido
        # na esquerda do nodo pai
        if nodo.info < nodoPai.info:
            
            # Se o nodoPai tem o nodoFilhoEsquerda vazio, então pode-se inserir
            # o nodo diretamente no espaço, criando as relações entre ponteiros
            # nos nodos
            if nodoPai.nodoFilhoEsquerda == None:
                nodo.nodoPai = nodoPai
                nodoPai.nodoFilhoEsquerda = nodo
                return
            
            # Caso contrário, chama-se recursivamente a função passando o nodo
            # e o nodoFilhoEsquerda do nodo pai para avaliar se o nodo a ser
            # inserido ficará na esquerda ou na direita do nodoFilhoEsquerda
            else:
                self.insereNodo(nodo, nodoPai.nodoFilhoEsquerda)
        
        # Caso o nodo a ser inserido tenha a info maior que a do nodoPai, então
        # ele deve ficar à direita deste
        if nodo.info > nodoPai.info:
            
            # Se o nodoFilhoDireita estiver vazio, aloca-se o nodo lá
            if nodoPai.nodoFilhoDireita == None:
                nodo.nodoPai = nodoPai
                nodoPai.nodoFilhoDireita = nodo
                return
            
            # Caso contrário, chamada recursiva para avaliar se esse nodo ficará
            # à esquerda ou à direita do nodoFilhoDireita
            else:
                self.insereNodo(nodo, nodoPai.nodoFilhoDireita)
        
        return

    # Função para remover de nodos na árvore
    # Podem ocorrer remoções tanto nas folhas quanto nos nodos internos.
    # É necessário manter a ordem da árvore para que ela continue com as
    # características de uma árvore binária de pesquisa - para tanto, será
    # necessário movimentar nodos na estrutura.
    #
    # Existem basicamente 3 tipos de remoções possíveis: quando o nodo é uma
    # folha; quando ele é interno com apenas 1 subárvore à direita ou à 
    # esquerda; e quando ele tem as duas subárvores.
    #
    # info - informação para buscar na árvore e remover o nodo que a contém
    # nodo - utilizado para chamadas recursivas para buscar o nodo
    def removeNodo(self, info, nodo = ''):
        
        # Na primeira chamada, assume-se que o nodo a ser verificado será a
        # própria raiz da árvore
        if nodo == '':
            nodo = self.raiz
        
        # Se o nodo verificado na iteração tiver a informação 
        # buscada, então ele é o nodo a ser removido
        if nodo.info == info:
            
            # Em seguida serão feitas as verificações do tipo de remoção. Nesse
            # primeiro caso, o mais simples, verifica-se o nodo não tem filhos -
            # no caso, ele será um nó folha e poderá ser removido facilmente
            # apagando-se as relações entre ele e o pai dele
            if nodo.nodoFilhoEsquerda == None and nodo.nodoFilhoDireita == None:
                
                if nodo.nodoPai.nodoFilhoEsquerda == nodo:
                    nodo.nodoPai.nodoFilhoEsquerda = None
                else:
                    nodo.nodoPai.nodoFilhoDireita = None
                    
                nodo.nodoPai = None
                
            # Caso não, verifica-se se o nodo tem apenas a subárvore da direita.
            # Nesse caso, os nós filhos da direita serão repassados como a nova
            # subárvore da direita do nó pai do nodo que será removido.
            elif nodo.nodoFilhoEsquerda == None and nodo.nodoFilhoDireita:
                if nodo.nodoPai.nodoFilhoEsquerda == nodo:
                    nodo.nodoPai.nodoFilhoEsquerda = nodo.nodoFilhoDireita
                else:
                    nodo.nodoPai.nodoFilhoDireita = nodo.nodoFilhoDireita
                    
                nodo.nodoFilhoDireita.nodoPai = nodo.nodoPai
                
                nodo.nodoPai = None
                nodo.nodoFilhoDireita = None
                
            # Como o caso anterior, entretanto para a situação onde o nodo tem
            # subárvore à esquerda
            elif nodo.nodoFilhoEsquerda and nodo.nodoFilhoDireita == None:
                if nodo.nodoPai.nodoFilhoEsquerda == nodo:
                    nodo.nodoPai.nodoFilhoEsquerda = nodo.nodoFilhoEsquerda
                else:
                    nodo.nodoPai.nodoFilhoDireita = nodo.nodoFilhoEsquerda
                    
                nodo.nodoFilhoEsquerda.nodoPai = nodo.nodoPai
                
                nodo.nodoPai = None
                nodo.nodoFilhoEsquerda = None
            
            # No caso mais complexo, verifica-se se o nodo tem as duas
            # subárvores. Aqui, o algoritmo pegará o maior nodo da subárvore da
            # esquerda e o utilizará no lugar do que será removido. Esse
            # movimento pode requerer uma série de outros movimentos, que ao
            # final manterão a característica principal da árvore binária de
            # pesquisa
            elif nodo.nodoFilhoEsquerda and nodo.nodoFilhoDireita:
                
                # Cria-se uma variável e atribui o
                # primeiro nodo da esquerda para ela
                nodoMaior = nodo.nodoFilhoEsquerda
                
                # Se há uma subárvore à direita daquele nodo, então há nodos
                # com valores maiores que o nodo atual. Varre-se a subárvore
                # em busca desse nodo
                if nodoMaior.nodoFilhoDireita:
                    while nodoMaior.info < nodoMaior.nodoFilhoDireita.info:
                        nodoMaior = nodoMaior.nodoFilhoDireita
                        
                        if nodoMaior.nodoFilhoDireita == None:
                            break
                
                # Quando encontrado, verifica-se se esse nodo tem subárvore à
                # esquerda: em caso afirmativo, ela será a nova subárvore à
                # direita do pai do nodo que será utilizado para substituir o
                # que será apagado
                if nodoMaior.nodoFilhoEsquerda and nodoMaior.nodoPai != nodo:
                    nodoMaior.nodoPai.nodoFilhoDireita = nodoMaior.nodoFilhoEsquerda
                    nodoMaior.nodoFilhoEsquerda.nodoPai = nodoMaior.nodoPai
                
                # Nesse bloco cria-se a relação entre o nodo que será utilizado
                # para substituir o que será removido (nodoMaior e nodo,
                # respectivamente) com o pai do nodo que será removido
                nodoMaior.nodoPai = nodo.nodoPai
                if nodo.nodoPai.nodoFilhoEsquerda == nodo:
                    nodo.nodoPai.nodoFilhoEsquerda = nodoMaior
                else:
                    nodo.nodoPai.nodoFilhoDireita = nodoMaior
                
                # Nesse bloco cria-se a relação entre o nodo que substituirá o
                # removido com a subárvore à direita deste
                nodoMaior.nodoFilhoDireita = nodo.nodoFilhoDireita
                nodo.nodoFilhoDireita.nodoPai = nodoMaior
                
                # Nesse bloco, cria-se a relação com a subárvore à esquerda do
                # nodo que será removido
                if nodo.nodoFilhoEsquerda != nodoMaior:
                    nodoMaior.nodoFilhoEsquerda = nodo.nodoFilhoEsquerda
                    nodo.nodoFilhoEsquerda.nodoPai = nodoMaior
                
                # Os três comandos a seguir tratam de anular
                # os ponteiros do nodo que será removido
                nodo.nodoPai = None
                nodo.nodoFilhoEsquerda = None
                nodo.nodoFilhoDireita = None
        
        # Caso a informação do nodo seja maior que a em busca
        elif nodo.info > info:
            # Verifica-se se há subárvore à esquerda (que tem valores menores)
            # para continuar as buscas e executa-se uma chamada recursiva
            if nodo.nodoFilhoEsquerda:
                self.removeNodo(info, nodo.nodoFilhoEsquerda)
            # Caso não, não há o que procurar e
            # a informação não existe na árvore
            else:
                print('ERROR\ninfo não existe!')
        
        # Caso a informação do nodo seja menor que a em busca
        elif nodo.info < info:
            # Verifica-se se há subárvore à direita (que tem valores maiores)
            # para continuar as buscas e executa-se uma chamada recursiva
            if nodo.nodoFilhoDireita:
                self.removeNodo(info, nodo.nodoFilhoDireita)
            # Caso não, não há o que procurar e
            # a informação não existe na árvore
            else:
                print('ERROR\ninfo não existe!')

        return

    # Função para buscar uma informação na árvore
    # A implementação é feita de maneira recursiva.
    #
    # info - informação a ser buscada na árvore
    # nodo - 'nodo base' da função, utilizado apenas nas chamadas recursivas
    def buscaInfo(self, info, nodo = ''):
        
        # resultado aqui funciona como uma variável para checar se a informação
        # foi encontrada ou não
        resultado = False
        
        # Na primeira chamada da função, nodo passará a ser a raiz da árvore
        if nodo == '':
            nodo = self.raiz
            
        # Verifica-se se o nodo já tem a informação buscada. Caso sim,
        # suspende-se a busca nesse ponto.
        if nodo.info == info:
            return True
        # Caso não, verifica-se se a informação no nodo é maior que a buscada
        # e se há árvore à esquerda - caso sim, avalia-se essa subárvore a
        # partir de uma chamada recursiva para o nodoFilhoEsquerda
        elif nodo.info > info and nodo.nodoFilhoEsquerda:
            resultado = self.buscaInfo(info, nodo.nodoFilhoEsquerda)
        # Para o caso onde a informação no nodo é menor que a buscada,
        # verifica-se se há árvore à direita e avalia-se essa subárvore a
        # partir de uma chamada recursiva para o nodoFilhoDireita
        elif nodo.info < info and nodo.nodoFilhoDireita:
            resultado = self.buscaInfo(info, nodo.nodoFilhoDireita)
        
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
