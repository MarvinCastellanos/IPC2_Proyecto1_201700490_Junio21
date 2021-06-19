class NodoCabeceraY:
    def __init__(self,y):
        self.arriba=None
        self.abajo=None
        self.siguiente=None
        self.y=y

    def setArriba(self,nodoC):
        self.arriba=nodoC
    
    def setAbajo(self,nodoC):
        self.abajo=nodoC
    
    def setSiguiente(self,nodoC):
        self.siguiente=nodoC
    
    def getArriba(self):
        return self.arriba
    
    def getAbajo(self):
        return self.abajo
    
    def getSiguiente(self):
        return self.siguiente
    
    def getY(self):
        return self.y