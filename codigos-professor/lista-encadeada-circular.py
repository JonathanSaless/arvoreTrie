#
#    Implementação de Lista Linear Encadeada Circular em Python 3
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
# Implementa um Nodo, uma classe simples que guarda qualquer informação, um
# "ponteiro" para o próximo nodo e outro "ponteiro" para o nodo anterior na
# estrutura encadeada
#

# Definição da classe Nodo
class Nodo:
    
    #Método construtor
    def __init__(self, info):
        
        # O argumento 'info' representa uma infomação
        # qualquer a ser aplicada na classe Nodo
        self.info = info
        
        # O atributo 'proximoNodo' servirá como referência para o próximo
        # Nodo a ser atribuído no tipo de alocação encadeada. No início o
        # valor será 'None' pois no momento da criação não há qualquer nodo
        # a ser referenciado
        self.proximoNodo = None

#
# Classe ListaEncadeadaCircular
#
# Esta classe implementa uma lista encadeada e circular em Python 3. Nesta
# classe, elementos são relacionados entre si a partir de um
# "ponteiro" que identifica a ordem dos nodos. A lista guarda a referência
# para o primeiro nodo da lista e contém algumas funções para inserção,
# remoção, busca e percorrimento. Não há índices de posição nesse tipo de
# lista. Segue abaixo a implementação da classe bem como seus principais
# métodos, como o construtor, inserção de nodo, remoção e busca
#

# Definição da classe ListaEncadeadaCircular
class ListaEncadeadaCircular:
    
    # Método construtor
    def __init__(self):
        
        # Ponteiro que aponta para o nodo raiz (ou cabeça) da lista. Na
        # inicialização da lista, por não haver nodos, a raiz será None
        self.raiz = None
    
    # Função simples de inserção de nodos no início da lista
    #
    # nodo - o nodo a ser inserido na lista
    def insereNodo(self, nodo):
        # Se não há um nodo raiz já definido, então esse será o nodo raiz
        # da estrutura. O ponteiro aponta para o próprio nodo pois trata-se
        # de uma lista circular
        if not self.raiz:
            nodo.proximoNodo = nodo
            self.raiz = nodo
            
        # Caso já exista uma raiz, os ponteiros do nodo que será adicionado
        # passam a apontar para a raiz atual. Em seguida, varre-se a lista
        # para encontrar o "último" nodo da lista circular. Este, terá seu
        # ponteiro proximoNodo atualizado para apontar para o novo nodo na
        # estrutura, que será a raiz da mesma
        else:
            nodo.proximoNodo = self.raiz
            
            nodoAtual = self.raiz
            while nodoAtual.proximoNodo != self.raiz:
                nodoAtual = nodoAtual.proximoNodo
            
            nodoAtual.proximoNodo = nodo
            self.raiz = nodo
        
        return
    
    # Remove nodo a partir do conteúdo informado
    #
    # info - conteúdo a ser removido da estrutura
    def removeNodo(self, info):
        # Guarda-se o nodo raiz da estrutura
        nodoAtual = self.raiz
        
        # Cria-se uma referência para um nodo anterior que será utilizado
        # para a remoção
        nodoAnterior = None
        
        # Essa verificação serve para o caso onde a lista encadeada ainda não
        # tem nodos. Assim, não há o que ser removido
        if self.raiz == None:
            print('Lista Vazia\nNão há o que ser removido')
            return
        
        # Esse laço while irá varrer a estrutura verificando se a informação
        # que dado nodo tem é aquela que se está buscando. Caso não, o comando
        # nodoAtual = nodoAtual.proximoNodo passará a referência para o nodo
        # seguinte da estrutura, que terá sua informação verificada a seguir
        while nodoAtual.info != info:
            nodoAnterior = nodoAtual
            nodoAtual = nodoAtual.proximoNodo
            
            # Caso o nodo verificado seja a raiz, então não há a informação
            # a ser removida na lista
            if nodoAtual == self.raiz:
                print('Conteúdo não existe na estrutura')
                return
        
        # Se o nodo a ser removido for a raiz da lista, será necessário forçar
        # o percorrimento da estrutura para encontrar o "último" nodo da lista.
        # Após, então modificamos a raiz para o próximo nodo. Isso serve para
        # evitar que a lista fique sem raiz
        if nodoAtual == self.raiz:
            nodoAtual = self.raiz.proximoNodo
            nodoAnterior = self.raiz
            
            while nodoAtual != self.raiz:
                nodoAnterior = nodoAtual
                nodoAtual = nodoAtual.proximoNodo
            
            self.raiz = self.raiz.proximoNodo
            nodoAnterior.proximoNodo = self.raiz
        
        # Se a função conseguiu sair do laço while então o conteúdo foi
        # encontrado e o nodo será removido. Para tanto, apenas atualiza-se
        # os ponteiros do nodo anterior ao atual para o próximoNodo do
        # nodoAtual, e do anterior ao próximo para o anterior ao atual,
        # removendo-o da estrutura
        else:
            nodoAnterior.proximoNodo = nodoAtual.proximoNodo
        
        # Anula-se o ponteiro próximo nodo do que está sendo removido
        nodoAtual.proximoNodo = None
        
        return

    # Função para imprimir o conteúdo de um nodo da lista a partir
    # da posição informada (índice)
    #
    # posicao - índice a ter o conteúdo apresentado
    def acessaPosicao(self, posicao):
        # Guarda-se o nodo raiz da estrutura
        nodoAtual = self.raiz
        
        # Cria-se uma variável para ir guardando a posição em análise
        posicaoEmAnalise = 0
        
        # Percorre a estrutura até atingir a posição buscada ou até que o
        # nodoAtual seja o último nodo, o que significa que a posição é maior
        # que a quantidade de nodos existentes na estrutura
        while posicaoEmAnalise < posicao:
            nodoAtual = nodoAtual.proximoNodo
            
            if nodoAtual == self.raiz:
                break
            
            posicaoEmAnalise += 1
        
        # Caso posiao seja diferente da posicaoEmAnalise, então não há o que
        # mostrar; do contrário, imprime a informação do conteúdo fornecido
        if posicao == posicaoEmAnalise:
            print(nodoAtual.info)
        else:
            print('ERROR\nPosição Inválida!\nMaior que o final da lista')
        
        return

    # Função para buscar a posicao na lista de dado conteúdo
    #
    # conteudo - o conteudo a ser buscado na lista
    def buscaPosicao(self, conteudo):
        # Guarda-se o nodo raiz da estrutura
        nodoAtual = self.raiz
        
        # Cria-se uma variável para ir guardando a posição na estrutura
        posicao = 0
        
        # Percorre-se a estrutura em busca do conteúdo a ser encontrado.
        # Caso nodoAtual seja o último, então a busca percorreu a estrutura
        # inteira e não achou o conteúdo correspondente
        while nodoAtual.info != conteudo:
            nodoAtual = nodoAtual.proximoNodo
            posicao += 1
            
            if nodoAtual == self.raiz:
                break
        
        # Caso nodoAtual tenha o conteúdo buscado, imprime-se a informação; do
        # contrário, o conteúdo não existe na estrutura
        if nodoAtual.info == conteudo:
            print(posicao)
        else:
            print('Conteúdo não está presente')
        
        return

    # Função para imprimir o conteúdo de todos os nodos da lista
    def imprimeLista(self):
        nodoAtual = self.raiz
        
        while nodoAtual.proximoNodo != self.raiz:
            print(nodoAtual.info, end = ' ')
            nodoAtual = nodoAtual.proximoNodo
            
        print(nodoAtual.info, end = ' ')
        print()
        return
