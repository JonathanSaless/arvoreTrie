#
#    ListaSequencial - Implementação de Lista Linear Sequencial em Python 3
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
# Essa classe será utilizada na lista com alocação sequencial
#

# Definição da classe Nodo
class Nodo:

    #Método construtor
    def __init__(self, info):

        # O argumento 'info' representa uma infomação
        # qualquer a ser aplicada na classe Nodo
        self.info = info

#
# Classe ListaSequencial
#
# Esta classe implementa uma lista linear alocada de forma sequencial em Python
# 3. Nesta classe, elementos são inseridos e removidos em qualquer lugar da
# lista porém não deve haver espaços vazios entre os elementos. Abaixo segue a
# implementação da classe bem como seus principais métodos, como o construtor,
# inserção de nodo no fim, em outra posição, remoção e busca
#

# Definição da classe ListaSequencial
class ListaSequencial:

    # Método construtor
    #
    # tamanhoMaximo - o tamanho máximo de índices a ser previamente alocado
    def __init__(self, tamanhoMaximo):

        # Cria uma lista vazia de nome "lista" no construtor
        self.lista = []

        # Ponteiro que aponta para o próximo índice da lista
        self.proximoIndice = 0

        # Tamanho máximo que a lista suportará, representando a alocação de
        # memória prévia. Subtraimos 1 do tamanho máximo para casar com o
        # índice da lista (que lembramos, varia de 0 ao tamanho máximo - 1)
        self.tamanhoMaximo = tamanhoMaximo - 1

    # Função simples de inserção de nodos ao final da lista
    #
    # nodo - o nodo a ser inserido na lista
    def insereNodoNoFim(self, nodo):

        # Verifica se o próximo índice da lista não aponta para um espaço
        # maior que o previamente alocado no construtor. Caso sim, imprime
        # mensagem de erro
        if self.proximoIndice > self.tamanhoMaximo:
            print('ERROR\nLista com tamanho máximo permitido')
            return

        # self.lista.append(None) aloca memória para ser utilizada a seguir
        self.lista.append(None)
        self.lista[self.proximoIndice] = nodo
        self.proximoIndice += 1

        return

    # Método utilizado para inserção de um nodo em algum espaço da lista
    #
    # nodo - o nodo a ser inserido na lista
    # posicao - a posicao na lista onde o nodo será inserido
    def insereNodo(self, nodo, posicao):

        # Verifica se a posição utilizada para inserção está fora do
        # tamanho máximo da lista
        if posicao > self.tamanhoMaximo:
            print('ERROR\nPosição Inválida!\nMaior que o tamanho máximo da lista')
            return

        # Verifica se a posição utilizada para inserção está em um espaço
        # entre o primeiro índice e o próximo índice da lista. Caso sim,
        # todos os elementos da lista à direita deverão ser deslocados para
        # a direita a fim de abrir espaço para o nodo a ser inserido
        if posicao >= 0 and posicao < self.proximoIndice:
            self.lista.append(None)
            self.proximoIndice += 1

            # Laço for para deslocar os elementos para um índice à direita,
            # abrindo espaço para a inserção do nodo na posição indicada
            #
            # Atentem pois esse laço é decrescente
            for i in range(self.proximoIndice - 1, posicao, -1):
                self.lista[i], self.lista[i - 1] = self.lista[i - 1], self.lista[i]

            self.lista[posicao] = nodo
            return

        # Se a posição a ser utilizada é o próprio próximo índice, apenas
        # aloca memória e faz a inserção do nodo
        if posicao == self.proximoIndice:
            self.lista.append(None)
            self.proximoIndice += 1

            self.lista[posicao] = nodo
            return

        # Se a posição for maior que o próximo índice, a lista teria
        # espaços vazios entre elementos. Não queremos isso, portanto
        # fazemos a verificação e caso isso ocorra apresentaremos uma
        # mensagem de erro
        if posicao > self.proximoIndice:
            print('ERROR\nPosição Inválida!\nMaior que o final da lista')
            return

    # Função para remover um nodo a partir da posição na lista
    #
    # posicao - posição na lista em que o nodo será removido
    def removeNodo(self, posicao):

        # Verifica se a posição a ser removida é válida. Caso sim, o elemento
        # será movimentado até o final da lista e, apenas lá, removido
        if posicao >= 0 and posicao < self.proximoIndice:

            # O laço for com o deslocamento do nodo a ser removido
            # até o final da lista
            for i in range(posicao, self.proximoIndice - 1):
                self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]

            # self.lista.pop() é o comando para remover o último elemento da lista
            self.lista.pop()
            self.proximoIndice -= 1
            return

        # Se a posição a ser removida já é o final da lista,
        # então basta removê-la sem deslocamentos
        if posicao == self.proximoIndice - 1:
            self.lista.pop()
            self.proximoIndice -= 1
            return

        # Verifica se a posicao a ser removida está fora do limite dos índices
        # já presentes. Caso sim, é uma posição inválida e imprimi-se uma
        # mensagem de erro
        if posicao > self.proximoIndice:
            print('ERROR\nPosição Inválida!\nMaior que o final da lista')
            return

    # Função para imprimir o conteúdo de um nodo da lista a partir
    # da posição informada (índice)
    #
    # posicao - índice a ter o conteúdo apresentado
    def acessaPosicao(self, posicao):

        # Verifica se a posição informada é válida. Caso sim, imprime o
        # conteúdo; caso contrário, apresenta mensagem de erro
        if posicao <= self.proximoIndice:
            print(self.lista[posicao].info)
        else:
            print('ERROR\nPosição Inválida!\nMaior que o final da lista')
        return

    # Função para buscar a posicao na lista de dado conteúdo
    #
    # conteudo - o conteudo a ser buscado na lista
    def buscaPosicao(self, conteudo):

        # Laço for para varrer a lista em busca do conteúdo
        # Caso exista, será impresso
        for i in range(self.proximoIndice):
            if self.lista[i].info == conteudo:
                print(i)
                return

        # Se o conteúdo não existe, imprime uma mensagem informativa
        print('Conteúdo não está presente')
        return

    # Função para imprimir o conteúdo de todos os nodos da lista
    def imprimeLista(self):
        for i in self.lista:
            print(i.info, end = ' ')
        print()
        return
