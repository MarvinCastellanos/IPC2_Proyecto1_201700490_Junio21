from matriz import matrizD
from nodo import punto
from graphviz import Digraph


punto1= punto(1,3,'green','1,3')
punto2= punto(2,1,'green','2,1')
punto3= punto(5,3,'green','3,3')
punto4= punto(10,1,'green','1,1')
punto5= punto(3,1,'green','3,1')
punto6= punto(1,20,'green','1,2')

matriz = matrizD()

matriz.agregaNodo(punto1,punto1.getX(),punto1.getY())
matriz.agregaNodo(punto2,punto2.getX(),punto2.getY())
matriz.agregaNodo(punto3,punto3.getX(),punto3.getY())
matriz.agregaNodo(punto4,punto4.getX(),punto4.getY())
matriz.agregaNodo(punto5,punto5.getX(),punto5.getY())
matriz.agregaNodo(punto6,punto6.getX(),punto6.getY())

matriz.generaGraphviz()