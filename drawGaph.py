import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(allNodes, path):
  color_map = []

  G=nx.Graph()

  for node in allNodes:
    for adjacente in node.adjacentes:
      G.add_edges_from([(node.nome, adjacente.nome)])

  if(path is not None):
    [color_map.append("blue") if node in path else color_map.append("grey") for node in G.nodes]
  else:
    [color_map.append("grey") for node in G.nodes]

  fixed_positions = {
    allNodes[0].nome: (-2.5, 5),  # RR
    allNodes[1].nome: (1.8, 5),  # AP
    allNodes[2].nome: (-1.6, 2.5),  # AM
    allNodes[3].nome: (1.9, 3),  # PA
    allNodes[4].nome: (-3.4, 1.1),  # AC
    allNodes[5].nome: (-1.2, 0.5),  # RO
    allNodes[6].nome: (2.8, 1),  # TO
    allNodes[7].nome: (3.8, 3),  # MA
    allNodes[8].nome: (4.8, 2.2),  # PI
    allNodes[9].nome: (6, 2.8),  # CE
    allNodes[10].nome: (7, 2.6), # RN
    allNodes[11].nome: (7.2, 1.7), # PB
    allNodes[12].nome: (6.4, 1.3), # PE
    allNodes[13].nome: (6.6, 0.3), # AL
    allNodes[14].nome: (6.1, -0.3), # SE
    allNodes[15].nome: (4.7, -0.4), # BA
    allNodes[16].nome: (1, -0.3), # MT
    allNodes[17].nome: (2.6, -1), # GO
    allNodes[18].nome: (1.3, -3), # MS
    allNodes[19].nome: (4, -2), # MG
    allNodes[20].nome: (5, -2), # ES
    allNodes[21].nome: (4.5, -2.8), # RJ
    allNodes[22].nome: (3, -3.9), # SP
    allNodes[23].nome: (2.4, -5.2), # PR
    allNodes[24].nome: (2, -7), # SC
    allNodes[25].nome: (1, -9), # RS
  }
  
  fixed_nodes = fixed_positions.keys()
  pos = nx.spring_layout(G,pos=fixed_positions, fixed = fixed_nodes)

  plt.figure(figsize=(7.6, 8))

  nx.draw(G, pos, node_color = color_map, with_labels = True, node_size=800, font_color="white")
  
  plt.show()