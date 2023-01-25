# coding=utf-8
#
#    Implementacao de Fila com Alocacao Encadeada em Python 3
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
# Implementa um Nodo, uma classe simples que guarda qualquer informacao
#
# Essa classe sera utilizada na fila com alocacao encadeada
#

# Definicao da classe Nodo
class Nodo:

    #Método construtor
    def __init__(self, info):

        # O argumento 'info' representa uma infomação
        # qualquer a ser aplicada na classe Nodo
        self.info = info

        # O atributo anteriorNodo apontara para o nodo exatamente anterior ao
        # que esta em processamento
        self.anteriorNodo = None


#
# Classe FilaEncadeada
#
# Esta classe implementa uma fila com alocação encadeada em Python 3. Nesse
# tipo de estrutura, defini-se na inicialização um ponteiro para o "primeiro"
# nodo da fila e um outro para o "último". As operações de inserção e remoção
# são realizadas respectivamente em extremos opostos da fila (a inserção sendo
# sempre ao final e a remoção e consulta no início da fila). Segue a
# implementação da classe e os já citados métodos
#

# Definição da classe FilaEncadeada
class FilaEncadeada:

    # Método construtor
    def __init__(self):
        # Ponteiro para o primeiro nodo da fila
        self.primeiroNodo = None

        # Ponteiro para o último nodo da fila
        self.ultimoNodo = None

    # Função para inserção de nodos na fila. Lembre-se que ele sempre ocorre
    # ao final da fila
    #
    # nodo - nodo a ser inserido na fila
    def insereNodo(self, nodo):

        # Se o primeiroNodo é None, quer dizer que a fila é vazia.
        # Adiciona-se o nodo setando tanto o primeiro quanto o último nodo
        # para ele
        if not self.primeiroNodo:
            self.primeiroNodo = nodo
            self.ultimoNodo = nodo
            return

        # Caso a fila já tenha algum elemento, atualiza-se o ponteiro
        # anteriorNodo do atual último nodo para o nodo que será inserido, e
        # em seguida torna o nodo a ser inserido o último da fila
        self.ultimoNodo.anteriorNodo = nodo
        self.ultimoNodo = nodo

        return

    # Função para remoção de um nodo da fila
    # As remoções sempre ocorrem no primeiro nodo da fila
    def removeNodo(self):

        # Se primeiroNodo é None, então a fila é vazia
        # e não há o que remover
        if not self.primeiroNodo:
            print('ERROR\nFila vazia!')
            return

        # Caso contrário, guarda-se a referência para o atual primeiroNodo,
        # e tornamos o anterior a ele o primeiroNodo da estrutura
        nodoRemocao = self.primeiroNodo
        self.primeiroNodo = self.primeiroNodo.anteriorNodo

        # Em seguida, tornamos nula a referência anteriorNodo do nodo recém
        # removido
        nodoRemocao.anteriorNodo = None

        # Se acontecer do primeiroNodo ser None, então a fila ficou vazia e
        # devemos tornar None também o ponteiro para ultimoNodo
        if not self.primeiroNodo:
            self.ultimoNodo = None

        return

    # Função para acessar o nodo de uma fila
    # Para essas estruturas, o acesso é exclusivo ao primeiro nodo
    def acessaNodo(self):

        # Se primeiroNodo for None, então a fila é vazia
        # e não há o que mostrar
        if self.primeiroNodo == None:
            print('ERROR\nFila vazia!')
            return

        # Caso contrário, imprime o conteúdo do
        # primeiro elemento da fila
        print(self.primeiroNodo.info)
        return

    # Função para imprimir o conteúdo de todos os nodos da fila
    def imprimeFila(self):
        nodoAtual = self.primeiroNodo

        while nodoAtual != None:
            print(nodoAtual.info, end = ' ')
            nodoAtual = nodoAtual.anteriorNodo
        print()
        return


def main():
    fila = FilaEncadeada()
    fila.imprimeFila()
    print("?")


main()
