class punto:
    def __init__(self,x,y,color,valor):
        self.x=x
        self.y=y
        self.color=color
        self.valor=valor
        self.siguiente=None
        self.anterior=None
        self.arriba=None
        self.abajo=None

    def setSiguiente(self,nodo):
        self.siguiente=nodo
    
    def setAnterior(self,nodo):
        self.anterior=nodo
    
    def setArriba(self,nodo):
        self.arriba=nodo
    
    def setAbajo(self,nodo):
        self.abajo=nodo
    
    def getSiguiente(self):
        return self.siguiente
    
    def getAnterior(self):
        return self.anterior
    
    def getArriba(self):
        return self.arriba
    
    def getAbajo(self):
        return self.abajo
    
    def getColor(self):
        return self.color
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y