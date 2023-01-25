#
#    Implementação de Pilha com Alocação Encadeada em Python 3
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
# Essa classe será utilizada na pilha com alocação encadeada
#

# Definição da classe Nodo
class Nodo:
    
    #Método construtor
    def __init__(self, info):
        
        # O argumento 'info' representa uma infomação
        # qualquer a ser aplicada na classe Nodo
        self.info = info
        
        # O atributo anteriorNodo apontará para o nodo exatamente anterior ao
        # que está em processamento
        self.anteriorNodo = None

#
# Classe PilhaEncadeada
#
# Esta classe implementa uma pilha com alocação encadeada em Python 3. Nesse
# tipo de estrutura, a inicialização define uma única variável chamada "topo",
# que no início será None. Em seguida, operações de alocação, remoção e acesso
# sempre acontecem no último elemento adicionado, ou seja, no "topo" da pilha.
# Abaixo segue a implementação da classe com o construtor e os métodos de
# inserção, remoção e consulta
#

# Definição da classe PilhaEncadeada
class PilhaEncadeada:
    
    # Método construtor
    def __init__(self):
        
        # Ponteiro que aponta para o topo da pilha
        self.topo = None
    
    # Função de inserção de nodos na pilha
    # Lembre-se que a inserção ocorre apenas no topo da pilha
    #
    # nodo - o nodo a ser inserido na pilha
    def insereNodo(self, nodo):
        # Se o topo é None, quer dizer que não há elementos na pilha.
        # O nodo a ser adicionado então será o topo da pilha
        if not self.topo:
            self.topo = nodo
            return
        
        # Caso já existam elementos na pilha, basta fazer com que o ponteiro
        # para o nodo anterior ao que será adicionado aponte para o atual topo
        # da pilha e, em seguida, tornar o nodo a ser adicionado o próprio topo
        # desta pilha
        nodo.anteriorNodo = self.topo
        self.topo = nodo
        
        return

    # Função para remoção de um nodo
    # A remoção de um nodo também sempre ocorre no topo da pilha
    def removeNodo(self):
        # Se o topo é None, a pilha é vazia e não há o que remover
        if self.topo == None:
            print('ERROR\nPilha vazia!')
            return
        
        # Caso não seja vazia, guarda-se o topo atual e em seguida muda-se o
        # topo da pilha para o nodo exatamente anterior a ele. Isso removerá o
        # nodo topo da pilha
        nodoRemocao = self.topo
        self.topo = self.topo.anteriorNodo
        
        # Em seguida, com a referência guardada do antigo nodo topo da pilha,
        # apenas anula-se o ponteiro anteriorNodo dele
        nodoRemocao.anteriorNodo = None
        
        return

    # Função para acessar o nodo de uma pilha
    # Como as demais funções, o processamento se dá apenas no topo da pilha
    def acessaNodo(self):        
        # Se a pilha está vazia, não há o que ser acessado
        if self.topo == None:
            print('ERROR\nPilha vazia!')
            return
        
        # Caso a pilha não esteja vazia, imprime-se o conteúdo do topo da pilha
        print(self.topo.info)
        return

    # Função para imprimir o conteúdo de todos os nodos da pilha
    def imprimePilha(self):
        nodoAtual = self.topo
        
        while nodoAtual != None:
            print(nodoAtual.info, end = ' ')
            nodoAtual = nodoAtual.anteriorNodo
        print()
        return
