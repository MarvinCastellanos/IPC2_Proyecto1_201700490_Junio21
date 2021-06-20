from nodo import punto
from nodoY import NodoCabeceraY
from nodoX import NodoCabeceraX

class matrizD:
    def __init__(self):
        self.headX=NodoCabeceraX(1)
        self.headY=NodoCabeceraY(1)
    
    def generaGraphviz():
        print('grafica Graphviz')

    def generaXML():
        print('xml')
    
    def agregaNodo(self,nodo, x, y):
        auxX=self.headX
        auxY=self.headY
     
     #Recorre y crea cabeceras X
        contadorX=1
        while(True):
            if (auxX.getX()<x):
                if (auxX.getSiguiente()==None):
                    nuevo=NodoCabeceraX(contadorX+1)
                    auxX.setSiguiente(nuevo)
                    nuevo.setAnterior(auxX)
                    contadorX+=1
                    auxX=auxX.getSiguiente()
                else:
                    auxX=auxX.getSiguiente()
                    contadorX+=1
            if (auxX.getX()==x):
                break
     #recorre nodos de columna
        while(True):
            if (auxX.getY()<y):
                if (auxX.getAbajo()==None):
                    auxX.setAbajo(nodo)
                    nodo.setArriba(auxX)
                    break
                elif (auxX.getAbajo().getY()<y):
                    auxX=auxX.getAbajo()
                else:
                    nodo.setAbajo(auxX.getAbajo())
                    nodo.setArriba(auxX)
                    auxX.getAbajo().setArriba(nodo)
                    auxX.setAbajo(nodo)
                    break

     #Recorre cabeceras Y
        contadorY=1
        while(True):
            if (auxY.getY()<y):
                if (auxY.getAbajo()==None):
                    nuevo=NodoCabeceraY(contadorY+1)
                    auxY.setAbajo(nuevo)
                    nuevo.setArriba(auxY)
                    contadorY+=1
                    auxY=auxY.getAbajo()
                else:
                    auxY=auxY.getAbajo()
                    contadorY+=1
            if (auxY.getY()==y):
                break

     #Recorre nodos de fila
        while(True):
            if (auxX.getX()<x):
                if (auxY.getSiguiente()==None):
                    auxY.setSiguiente(nodo)
                    nodo.setAnterior(auxX)
                    break
                elif (auxY.getSiguiente().getX()<x):
                    auxY=auxY.getSiguiente()
                else:
                    nodo.setSiguinte(auxY.getSiguiente())
                    nodo.setAnterior(auxY)
                    auxY.getSiguiente().setAnterior(nodo)
                    auxY.setSiguiente(nodo)
                    break