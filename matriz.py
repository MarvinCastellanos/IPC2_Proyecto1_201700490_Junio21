from nodo import punto
from graphviz import Digraph

class matrizD:
    def __init__(self):
        self.head=punto(0,0,'blanco','0,0')

    
    def generaGraphviz(self):
        aux1=self.head
        aux2=self.head
        dot=Digraph(comment='Tablero')
        dot.attr(style='filled')
        dot.node(str(aux1.getX())+','+str(aux1.getY()),'Head')
        while(True):
         #grafica nodos hacia arriba
            if(aux2.getArriba() is not None):
                pos = str(aux2.getX())+','+str(aux2.getY())
                posSig = str(aux2.getArriba().getX())+','+str(aux2.getArriba().getY())

                dot.node(posSig,str(aux2.getArriba().getValor()),fillcolor=aux2.getArriba().getColor())
                dot.edge(pos,posSig)
                #dot.edge(posSig,pos)
         #grafica nodos hacia abajo
            if(aux2.getAbajo() is not None):
                dot.node(str(aux2.getAbajo().getX())+','+str(aux2.getAbajo().getY()),str(aux2.getAbajo().getValor()))
                pos = str(aux2.getX())+','+str(aux2.getY())
                posSig = str(aux2.getAbajo().getX())+','+str(aux2.getAbajo().getY())
                dot.edge(pos,posSig)
                #dot.edge(posSig,pos)
         #grafica nodos hacia anterior
            if (aux2.getAnterior() is not None):
                pos = str(aux2.getX())+','+str(aux2.getY())
                posSig = str(aux2.getAnterior().getX())+','+str(aux2.getAnterior().getY())

                dot.node(posSig,str(aux2.getAnterior().getValor()))
                
                #dot.edge(pos,posSig)
                #dot.edge(posSig,pos)
         #grafica nodos hacia siguiente
            if(aux2.getSiguiente() is not None):
                pos = str(aux2.getX())+','+str(aux2.getY())
                posSig = str(aux2.getSiguiente().getX())+','+str(aux2.getSiguiente().getY())
                dot.node(posSig,str(aux2.getSiguiente().getValor()))
                
                dot.edge(pos,posSig)
                aux2=aux2.getSiguiente()
                continue
            else:
                if(aux1.getAbajo() is not None):
                    with dot.subgraph() as s:
                        aux2=aux1
                        s.attr(rank='same')
                        while(True):
                            if(aux2.getSiguiente() is not None):
                                s.node(str(aux2.getX())+','+str(aux2.getY()))
                                aux2=aux2.getSiguiente()
                            else:
                                s.node(str(aux2.getX())+','+str(aux2.getY()))
                                break
                    aux1=aux1.getAbajo()
                    aux2=aux1
                    continue
                else:
                    with dot.subgraph() as s:
                        aux2=aux1
                        s.attr(rank='same')
                        while(True):
                            if(aux2.getSiguiente() is not None):
                                s.node(str(aux2.getX())+','+str(aux2.getY()))
                                aux2=aux2.getSiguiente()
                            else:
                                s.node(str(aux2.getX())+','+str(aux2.getY()))
                                break
                    break
            
            
        dot.render('Matriz', view=True)

    def generaXML():
        print('xml')
    
    def agregaNodo(self,nodo, x, y):
        auxX=self.head
        auxY=self.head
     
     #Recorre y crea cabeceras X
        contadorX=0
        while(True):
            if (auxX.getX()<x):
                if (auxX.getSiguiente()==None):
                    nuevo=punto(contadorX+1,0,'white',contadorX+1)
                    auxX.setSiguiente(nuevo)
                    nuevo.setAnterior(auxX)
                    contadorX+=1
                    auxX=auxX.getSiguiente()
                    #print('cabeceraX '+str(contadorX)+' Agregada')
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
                    #print('se agrego nodo en X')
                    break
                elif (auxX.getAbajo().getY()<y):
                    auxX=auxX.getAbajo()
                else:
                    nodo.setAbajo(auxX.getAbajo())
                    nodo.setArriba(auxX)
                    auxX.getAbajo().setArriba(nodo)
                    auxX.setAbajo(nodo)
                    #print('se agrego nodo en x')
                    break
            else:
                auxX=nodo

     #Recorre cabeceras Y
        contadorY=0
        while(True):
            if (auxY.getY()<y):
                if (auxY.getAbajo()==None):
                    nuevo=punto(0,contadorY+1,'white',contadorY+1)
                    auxY.setAbajo(nuevo)
                    nuevo.setArriba(auxY)
                    contadorY+=1
                    auxY=auxY.getAbajo()
                    #print('cabeceraY '+str(contadorY)+' Agregada')
                else:
                    auxY=auxY.getAbajo()
                    contadorY+=1
            if (auxY.getY()==y):
                break

     #Recorre nodos de fila
        while(True):
            if (auxY.getX()<x):
                if (auxY.getSiguiente()==None):
                    auxY.setSiguiente(nodo)
                    nodo.setAnterior(auxX)
                    #print('nodo Y agregado')
                    break
                elif (auxY.getSiguiente().getX()<x):
                    auxY=auxY.getSiguiente()
                else:
                    nodo.setSiguiente(auxY.getSiguiente())
                    nodo.setAnterior(auxY)
                    auxY.getSiguiente().setAnterior(nodo)
                    auxY.setSiguiente(nodo)
                    break
            else:
                auxY=nodo