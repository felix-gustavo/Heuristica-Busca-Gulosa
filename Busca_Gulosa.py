path = list()

def busca(atual, objetivo):
    path.append(atual.nome)
    
    if atual != objetivo:
        busca(sorted(atual.adjacentes)[0], objetivo)
        return path