#
#    Implementação de Lista Linear Encadeada em Python 3
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
# Implementa um Nodo, uma classe simples que guarda qualquer informação e um
# "ponteiro" para o próximo Nodo na estrutura encadeada
#
# Essa classe será utilizada na lista com alocação encadeada
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
        # valor será 'None' pois não há no momento da criação não há qualquer
        # nodo a ser referenciado
        self.proximoNodo = None

#
# Classe ListaEncadeada
#
# Esta classe implementa uma lista linear alocada de forma encadeada em Python
# 3. Nesta classe, elementos são relacionados entre si a partir de um
# "ponteiro" que identifica a ordem dos nodos. A ListaEncadeada guarda a
# referência para o primeiro nodo da lista e contém algumas funções para
# inserção, remoção, busca e percorrimento.Não há índices de posição nesse tipo
# de lista. Segue abaixo a implementação da classe bem como seus principais
# métodos, como o construtor, inserção de nodo no início e no fim, remoção e
# busca
#

# Definição da classe ListaEncadeada
class ListaEncadeada:
    
    # Método construtor
    def __init__(self):
        
        # Ponteiro que aponta para o nodo raiz (ou cabeça) da lista. Na
        # inicialização da lista, por não haver nodos, a raiz será None
        self.raiz = None
    
    # Função simples de inserção de nodos no início (raiz) da lista
    #
    # nodo - o nodo a ser inserido na lista
    def insereNodoNoInicio(self, nodo):
        
        # Se não há um nodo raiz já definido, então esse será o nodo raiz
        # da estrutura
        if not self.raiz:
            self.raiz = nodo
            
        # Caso já exista um nodo raiz, então a referência à raiz na estrutura
        # será atualizada, e o ponteiro de próximo nodo no novo nodo raiz será
        # atualizado para o nodo raiz anterior
        else:
            nodo.proximoNodo = self.raiz
            self.raiz = nodo
        
        return
    
    # Função simples de inserção de nodos no final da lista
    #
    # nodo - o nodo a ser inserido na lista
    def insereNodoNoFinal(self, nodo):
        
        # Se a lista está vazia, então aponta a raiz da estrutura para o nodo
        if not self.raiz:
            self.raiz = nodo
            return
        
        # Recupera-se o nodo raiz da estrutura
        nodoAtual = self.raiz
        
        # Para inserir um nodo ao final da estrutura, é necessário percorrê-la
        # até que o último nodo seja encontrado. Esse último nodo será aquele
        # em que o valor de proximoNodo será None (pois como é o último, não há
        # próximo nodo)
        while nodoAtual.proximoNodo != None:
            nodoAtual = nodoAtual.proximoNodo
        
        # Após encontrar o último nodo, apenas insere-se o nodo a ser
        # adicionado ao ponteiro proximoNodo do último nodo
        nodoAtual.proximoNodo = nodo
        
        return
    
    # Remove nodo a partir do conteúdo informado
    #
    # info - conteúdo a ser removido da estrutura
    def removeNodo(self, info):
        # Guarda-se o nodo raiz da estrutura
        nodoAtual = self.raiz
        # Cria-se uma variável para referenciar um nodo anterior
        nodoAnterior = None
        
        # Essa verificação é para o caso onde a lista encadeada ainda não tem
        # nodos. Assim, não há o que ser removido
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
            
            # Caso o nodoAtual seja None, significa que chegou-se ao final da
            # lista encadeada e o conteúdo buscado não existe na estrutura.
            # Portanto, não há o que ser removido
            if nodoAtual == None:
                print('Conteúdo não existe na estrutura')
                return
        
        # Se a função conseguiu sair do laço while então o conteúdo foi
        # encontrado e o nodo será removido. Para tanto, apenas atualiza-se
        # os ponteiros do nodoAnterior para o próximoNodo do nodoAtual,
        # removendo-o da estrutura
        #
        # No caso do if, se nodoAnterior == None, significa que o nodo a ser
        # removido é a própria raiz da lista. Assim, apenas atualiza-se a
        # referência à raiz da lista para o próximo nodo disponível
        if nodoAnterior == None:
            self.raiz = nodoAtual.proximoNodo
            nodoAtual.proximoNodo = None
            
        # Para o else atualiza-se o proximoNodo do nodoAnterior para o
        # proximoNodo do nodoAtual. Isso atualizará as referências e eliminará
        # o nodo a ser removido
        else:
            nodoAnterior.proximoNodo = nodoAtual.proximoNodo
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
        # nodoAtual seja None, o que significa que a posição é maior que a
        # quantidade de nodos existentes na estrutura
        while posicaoEmAnalise < posicao and nodoAtual != None:
            nodoAtual = nodoAtual.proximoNodo
            posicaoEmAnalise += 1
        
        # Caso o nodoAtual seja None, então não há o que mostrar; do contrário,
        # imprime a informação do conteúdo fornecido
        if nodoAtual == None:
            print('ERROR\nPosição Inválida!\nMaior que o final da lista')
        else:
            print(nodoAtual.info)
        
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
        # Caso nodoAtual seja None, então a busca percorreu a estrutura
        # inteira e não achou o conteúdo correspondente
        while nodoAtual != None and nodoAtual.info != conteudo:
            nodoAtual = nodoAtual.proximoNodo
            posicao += 1
        
        # Caso nodoAtual seja None, então o conteúdo não está na estrutura; do
        # contrário, imprime a posição que contém o conteúdo buscado
        if nodoAtual == None:
            print('Conteúdo não está presente')
        else:
            print(posicao)
        
        return

    # Função para imprimir o conteúdo de todos os nodos da lista
    def imprimeLista(self):
        nodoAtual = self.raiz
        
        while nodoAtual != None:
            print(nodoAtual.info, end = ' ')
            nodoAtual = nodoAtual.proximoNodo
            
        print()
        return
