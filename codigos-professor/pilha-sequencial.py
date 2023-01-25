#
#    Implementação de Pilha com Alocação Sequencial em Python 3
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
# Essa classe será utilizada na pilha com alocação sequencial
#

# Definição da classe Nodo
class Nodo:
    
    #Método construtor
    def __init__(self, info):
        
        # O argumento 'info' representa uma infomação
        # qualquer a ser aplicada na classe Nodo
        self.info = info

#
# Classe PilhaSequencial
#
# Esta classe implementa uma pilha com alocação sequencial em Python 3. Nesse
# tipo de estrutura, defini-se na inicialização o tamanho máximo de memória a
# ser reservada para a estrutura. As operações de inserção, remoção e consulta
# sempre ocorrem no "topo" da pilha, ou seja, sempre no mesmo índice. Abaixo
# segue a implementação da classe com o construtor e seus principais métodos de
# inserção, remoção e consulta
#

# Definição da classe PilhaSequencial
class PilhaSequencial:
    
    # Método construtor
    #
    # tamanhoMaximo - o tamanho máximo de índices a ser previamente alocado
    def __init__(self, tamanhoMaximo):
        
        # Cria uma pilha vazia de nome "pilha" no construtor
        self.pilha = []
        
        # Ponteiro que aponta para o próximo índice da pilha, que chamaremos
        # de "topo da pilha"
        self.topo = 0
        
        # Tamanho máximo que a pilha suportará, representando a alocação de
        # memória prévia. Subtraimos 1 do tamanho máximo para casar com o
        # índice da pilha (que lembramos, varia de 0 ao tamanho máximo - 1)
        self.tamanhoMaximo = tamanhoMaximo - 1
    
    # Função de inserção de nodos na pilha
    # Lembre-se que a inserção ocorre apenas no topo da pilha
    #
    # nodo - o nodo a ser inserido na pilha
    def insereNodo(self, nodo):
        
        # Verifica se o topo da pilha não aponta para um espaço maior que
        # o previamente alocado no construtor. Caso sim, imprime mensagem
        # de erro
        if self.topo > self.tamanhoMaximo:
            print('ERROR\nPilha com tamanho máximo permitido')
            return
        
        # self.pilha.append(None) aloca memória para ser utilizada a seguir
        self.pilha.append(None)
        self.pilha[self.topo] = nodo
        self.topo += 1
        
        return

    # Função de remoção de nodo da pilha
    # A remoção ocorre apenas no topo da pilha
    def removeNodo(self):
        
        # Verifica se a pilha tem tamanho 0 - caso sim, não há o que remover
        # da pilha e retornaremos uma mensagem de erro
        if self.topo == 0:
            print('ERROR\nPilha vazia!')
            return
        
        self.pilha.pop()
        self.topo -= 1
        return

    # Função para imprimir o conteúdo do nodo do topo da pilha
    # O conteúdo acessado em uma pilha sempre é o que está no topo
    def acessaNodo(self):
        
        # Verifica se a pilha tem tamanho 0 - caso sim, não há o que
        # consultar e será retornada uma mensagem de erro
        if self.topo == 0:
            print('ERROR\nPilha vazia!')
            return
        
        print(self.pilha[self.topo - 1].info)
        return

    # Função para imprimir o conteúdo de todos os nodos da pilha
    # Essa função é meramente informativa e não necessariamente está
    # presente em implementações de pilha
    def imprimePilha(self):
        for i in self.pilha:
            print(i.info, end = ' ')
        print()
        return
