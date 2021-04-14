from VetorOrdenado import VetorOrdenado

class Busca_gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        self.path = []
        
    def buscar(self, atual):
        self.path.append(atual.nome)

        print("\nAtual: {}" .format(atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            self.achou = True
        else: 
            self.fronteira = VetorOrdenado(len(atual.adjacentes))
            for i in atual.adjacentes:
                if i.visitado == False:
                    i.visitado = True
                    self.fronteira.inserir(i)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Busca_gulosa.buscar(self, self.fronteira.getPrimeiro())

    def getPath(self):
        return self.path