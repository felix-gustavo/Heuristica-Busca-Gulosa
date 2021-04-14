import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(allNodes, path):
  color_map = []

  G=nx.Graph()

  for node in allNodes:
    for adjacente in node.adjacentes:
      G.add_edges_from([(node.nome, adjacente.nome)])

  [color_map.append("blue") if node in path else color_map.append("grey") for node in G.nodes]

  fixed_positions = {
    allNodes[0].nome: (0.199, 6.133), 
    allNodes[1].nome: (0.141, 5.177),
    allNodes[2].nome: (0.347, 6.510),
    allNodes[3].nome: (0.379, 5.248),
    allNodes[4].nome: (0.877, 7.055), # acre
    allNodes[5].nome: (1.083, 6.334), # ro
    allNodes[6].nome: (0.946, 4.826), # to
    allNodes[7].nome: (0.542, 4.544), # ma
    allNodes[8].nome: (0.660, 4.228), # pi
    allNodes[9].nome: (0.520, 3.953), # ce
    allNodes[10].nome: (0.581, 3.659), # RN
    allNodes[11].nome: (0.728, 3.672), # PB
    allNodes[12].nome: (0.838, 3.786), # PE
  }
  
  fixed_nodes = fixed_positions.keys()
  pos = nx.spring_layout(G,pos=fixed_positions, fixed = fixed_nodes)

  nx.draw(G, pos, node_color = color_map, with_labels = True, node_size=800, font_color="white")
  plt.savefig("simple_path.png")
  plt.show()