#Projeto de Algoritmos I - PROJETO FINAL

#interface gráfica
from tkinter import *

class app():
    def __init__(self, master):
        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1["padx"] = 20
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 10
        self.container2.pack(side = LEFT)

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 20
        self.container3.pack(side = RIGHT)

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 20
        self.container4.pack(side = BOTTOM)

        self.adc = Button(self.container3, text = "ADICIONAR")
        self.adc["font"] = ("Times", "10", "bold")
        self.adc["command"] = self.adicionar
        self.adc.pack()

        self.pesquisatxt = Label(self.container1, text = "PALAVRA:")
        self.pesquisatxt["font"] = ("Arial","10", "bold") 
        self.pesquisatxt.pack(side = LEFT)
        
        self.palavra = Entry(self.container1)
        self.palavra.pack(side = RIGHT)

        self.pesquisabutton = Button(self.container2, text = "PESQUISAR",fg = "white", bg = "Black", width = 10 )
        self.pesquisabutton["font"] = ("Times", "10", "bold")
        self.pesquisabutton["command"] = self.pesquisar
        self.pesquisabutton.pack()

        self.pesquisado = Label(self.container4)
        self.pesquisado["text"] = ""
        self.pesquisado.pack()
    def pesquisar(self):
        palavra = self.palavra.get()
        a = arvore.achar(palavra)
        if a:
            self.pesquisado["text"] = "Encontrou a palavra!"
                
        else:
            self.pesquisado["text"] = "Não encontrou a palavra!"
    def adicionar(self):
        palavra = self.palavra.get()
        arvore.insere(palavra)
        self.pesquisado["text"] = ""
        

#trie

class TrieNode():
    def __init__(self, info=None):
        self.info = info
        self.filho = []
        self.fim = False
        self.contador = 1
    

    def insere(self, palavra):
        node = self
        for letra in palavra:
            achou = False
            for filho in node.filho:
                if filho.info == letra:
                    filho.contador += 1
                    node = filho
                    achou = True
                    break
            if not achou:
                novo_nodo = TrieNode(letra)
                node.filho.append(novo_nodo)
                node = novo_nodo
        node.fim = True


    def achar(self, prefixo):
        node = self
        if not self.filho:
            return False
        for letra in prefixo:
            nachou = True
            for filho in node.filho:
                if filho.info == letra:
                    nachou = False
                    node = filho
                    break
            if nachou:
                return False
        return True


    

arvore = TrieNode()        
root = Tk()
app(root)
root.mainloop()

