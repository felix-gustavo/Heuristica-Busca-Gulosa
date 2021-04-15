from Node import Node
from Busca_Gulosa import Busca_gulosa

RS = Node('RS', 30.17, 53.50, None)

OBJETIVO = RS

AC = Node('AC', 8.77, 70.55, OBJETIVO)

AL = Node('AL', 9.62, 36.82, OBJETIVO)
AM = Node('AM', 3.47, 65.10, OBJETIVO)
AP = Node('AP', 1.41, 51.77, OBJETIVO)
BA = Node('BA', 13.29, 41.71, OBJETIVO)
CE = Node('CE', 5.20, 39.53, OBJETIVO)
DF = Node('DF', 15.83, 47.86, OBJETIVO)
ES = Node('ES', 19.19, 40.34, OBJETIVO)
GO = Node('GO', 15.98, 49.86, OBJETIVO)
MA = Node('MA', 5.42, 45.44, OBJETIVO)
MT = Node('MT', 12.64, 55.42, OBJETIVO)
MS = Node('MS', 20.51, 54.54, OBJETIVO)
MG = Node('MG', 18.10, 44.38, OBJETIVO)
PA = Node('PA', 3.79, 52.48, OBJETIVO)
PB = Node('PB', 7.28, 36.72, OBJETIVO)
PR = Node('PR', 24.89, 51.55, OBJETIVO)
PE = Node('PE', 8.38, 37.86, OBJETIVO)
PI = Node('PI', 6.60, 42.28, OBJETIVO)
RJ = Node('RJ', 22.25, 42.66, OBJETIVO)
RN = Node('RN', 5.81, 36.59, OBJETIVO)
RO = Node('RO', 10.83, 63.34, OBJETIVO)
RR = Node('RR', 1.99, 61.33, OBJETIVO)
SC = Node('SC', 27.45, 50.95, OBJETIVO)
SE = Node('SE', 10.57, 37.45, OBJETIVO)
SP = Node('SP', 22.19, 48.79, OBJETIVO)
TO = Node('TO', 9.46, 48.26, OBJETIVO)

# Norte
RR.adjacentes = [AM, PA]
AP.adjacentes = [PA]
AM.adjacentes = [RR, PA, MT, RO, AC]
PA.adjacentes = [AP, MA, TO, MT, AM, RR]
AC.adjacentes = [AM, RO]
RO.adjacentes = [AC, AM, MT]
TO.adjacentes = [MA, PI, BA, GO, MT, PA]
# Nordeste
MA.adjacentes = [PA, TO, PI]
PI.adjacentes = [MA, CE, PE, BA, TO]
CE.adjacentes = [PE, PB, RN, PI]
RN.adjacentes = [CE, PB]
PB.adjacentes = [RN, CE, PE]
PE.adjacentes = [PB, CE, PI, BA, AL]
AL.adjacentes = [PE, BA, SE]
SE.adjacentes = [AL, BA]
BA.adjacentes = [SE, AL, PE, PI, TO, GO, MG, ES]
# Centro-oeste
MT.adjacentes = [RO, AM, PA, TO, GO, MS]
GO.adjacentes = [BA, MG, MS, MT, TO]
MS.adjacentes = [MT, GO, MG, SP, PR]
# Sudeste
MG.adjacentes = [BA, ES, RJ, SP, MS, GO]
ES.adjacentes = [BA, MG, RJ]
RJ.adjacentes = [ES, MG, SP]
SP.adjacentes = [RJ, MG, MS, PR]
# Sul
PR.adjacentes = [SP, MS, SC]
SC.adjacentes = [PR, RS]
RS.adjacentes = [SC]

allNodes = [RR, AP, AM, PA, AC, RO, TO, MA, PI, CE, RN, PB, PE, AL, SE, BA, MT, GO, MS, MG, ES, RJ, SP, PR, SC, RS]

gulosa = Busca_gulosa(OBJETIVO)
gulosa.buscar(TO)
path = gulosa.getPath()

from drawGaph import drawGraph
  
drawGraph(allNodes, path)