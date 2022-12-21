class Ingredient:
    def __init__(self,id,name,observation,products):
        self.__id = id
        self.__name = name
        self.__observation = observation
        self.__products = products
        
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getObservation(self):
        return self.__observation

    def getProducts(self):
        return self.__products
    
    def setProduct(self,pid,product):
        self.__products[pid]=product