# coding=utf-8
#
#    Implementação de Fila com Alocação Sequencial em Python 3
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
# Essa classe será utilizada na fila com alocação sequencial
#

# Definição da classe Nodo
class Nodo:

    #Método construtor
    def __init__(self, info):

        # O argumento 'info' representa uma infomação
        # qualquer a ser aplicada na classe Nodo
        self.info = info

#
# Classe FilaSequencial
#
# Esta classe implementa uma fila com alocação sequencial em Python 3. Nesse
# tipo de estrutura, defini-se na inicialização o tamanho máximo de memória a
# ser reservada para a estrutura. As operações de inserção e remoção são
# realizadas respectivamente em extremos opostos da fila (a inserção sendo
# sempre ao final e a remoção e consulta no início da fila). Segue a
# implementação da classe e os já citados métodos
#

# Definição da classe FilaSequencial
class FilaSequencial:

    # Método construtor
    #
    # tamanhoMaximo - o tamanho máximo de índices a ser previamente alocado
    def __init__(self, tamanhoMaximo):

        # Cria uma fila vazia de nome "fila" no construtor
        self.fila = []

        # Ponteiro que aponta para o final da fila
        self.final = 0

        # Tamanho máximo que a fila suportará, representando a alocação de
        # memória prévia. Subtraimos 1 do tamanho máximo para casar com o
        # índice da fila (que lembramos, varia de 0 ao tamanho máximo - 1)
        self.tamanhoMaximo = tamanhoMaximo - 1

    # Função de inserção de nodos na fila
    # Lembre-se que a inserção ocorre apenas no final da fila
    #
    # nodo - o nodo a ser inserido na fila
    def insereNodo(self, nodo):

        # Verifica se o final da fila não aponta para um espaço maior que
        # o previamente alocado no construtor. Caso sim, imprime mensagem
        # de erro
        if self.final > self.tamanhoMaximo:
            print('ERROR\nFila com tamanho máximo permitido')
            return

        # self.fila.append(None) aloca memória para ser utilizada a seguir
        self.fila.append(None)
        self.fila[self.final] = nodo
        self.final += 1

        return

    # Função de remoção de nodo da fila
    # A remoção ocorre sempre no início da fila. Na implementação, deslocamos
    # o elemento a ser removido (que é o primeiro elemento da fila) para o
    # final e removemo-os com o comando utilizado na implementação de lista
    # sequencial
    def removeNodo(self):

        # Verifica se a fila tem tamanho 0 - caso sim, não há o que remover
        # da fila e retornaremos uma mensagem de erro
        if self.final == 0:
            print('ERROR\nFila vazia!')
            return

        for i in range(0, self.final - 1):
            self.fila[i], self.fila[i + 1] = self.fila[i + 1], self.fila[i]

        # self.lista.pop() é o comando para remover o último elemento da lista
        self.fila.pop()
        self.final -= 1
        return

    # Função para imprimir o conteúdo do nodo do início da fila
    # O conteúdo acessado em uma fila sempre é o que está no início
    def acessaNodo(self):

        # Verifica se a fila tem tamanho 0 - caso sim, não há o que
        # consultar e será retornada uma mensagem de erro
        if self.final == 0:
            print('ERROR\nFila vazia!')
            return

        print(self.fila[0].info)
        return

    # Função para imprimir o conteúdo de todos os nodos da fila
    # Essa função é meramente informativa e não necessariamente está
    # presente em implementações de fila
    def imprimeFila(self):
        for i in self.fila:
            print(i.info, end = ' ')
        print()
        return

def main():
    fila = FilaSequencial(4)
    fila.insereNodo(Nodo (1))
    fila.insereNodo(Nodo (2))
    fila.insereNodo(Nodo (4))
    fila.insereNodo(Nodo (5))
    fila.insereNodo(Nodo (6))
    fila.imprimeFila()


main()
