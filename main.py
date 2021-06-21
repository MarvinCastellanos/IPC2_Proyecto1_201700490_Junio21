from matriz import matrizD
from nodo import punto


punto1= punto(1,3,'verde','jugador1')
punto2= punto(2,1,'verde','jugador1')
punto3= punto(3,3,'verde','jugador1')
punto4= punto(1,1,'verde','jugador1')

matriz = matrizD()

matriz.agregaNodo(punto1,punto1.getX(),punto1.getY())
matriz.agregaNodo(punto2,punto2.getX(),punto2.getY())
matriz.agregaNodo(punto3,punto3.getX(),punto3.getY())
matriz.agregaNodo(punto4,punto4.getX(),punto4.getY())
