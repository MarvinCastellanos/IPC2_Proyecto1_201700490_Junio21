class NodoCabeceraX:
    def __init__(self,x):
        self.anterior=None
        self.siguiente=None
        self.abajo=None
        self.x=x
        self.y=0

    def setAnterior(self,nodoC):
        self.anterior=nodoC
    
    def setSiguiente(self,nodoC):
        self.siguiente=nodoC
    
    def setAbajo(self,nodoC):
        self.abajo=nodoC
    
    def getAnterior(self):
        return self.anterior
    
    def getSiguiente(self):
        return self.siguiente
    
    def getAbajo(self):
        return self.abajo
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y