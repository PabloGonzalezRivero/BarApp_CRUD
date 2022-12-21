class Product:
    def __init__(self,id,name,description,category,ingredients,price):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__category = category
        self.__ingredients = ingredients
        self.__price = price
        
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getCategory(self):
        return self.__category

    def getIngredients(self):
        return self.__ingredients
    
    def getPrice(self):
        return self.__price
    
    def setCategory(self,pcategory):
        self.__category=pcategory

    def setIngredient(self,iid,ingredient):
        self.__ingredients[iid]=ingredient
