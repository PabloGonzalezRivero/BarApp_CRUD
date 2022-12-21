class Category:
    def __init__(self,id,name,description,products):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__products = products

        
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getProducts(self):
        return self.__products
    
    def addProducts(self,product,pid):
        self.__products[pid]=product