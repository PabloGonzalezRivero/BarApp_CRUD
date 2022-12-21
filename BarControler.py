import time
from Barapi import *
from order import Order
from productOrder import ProductOrder

class BarController():

    def __init__(self):
        self._categories = {} #Key -> Id / Value -> Category 
        self._products = {} #Key -> Id / Value -> Product
        self._ingredients = {} #Key -> Id / Value -> Ingredient
        self._Orders = {}
        self._earned=0

        for Cid,category in getCategories().items():
            self._categories[Cid]=category

        for Pid,product in getProducts().items():
            self._products[Pid]=product

        for Iid,ingredient in getIngredients().items():
            self._ingredients[Iid]=ingredient

        for Cid,category in self._categories.items():
            for Pid,product in self._products.items():
                if product.getCategory().getId()==Cid:
                    newcategory= category
                    newproduct=product
                    product.setCategory(newcategory)
                    category.addProducts(newproduct,Pid)
                    


        for Pid,product in self._products.items():
            for pIngredient in product.getIngredients():
                for Iid,ingredient in self._ingredients.items():
                    IngredienteProducto = ingredient
                    ProductoIngrediente = product
                    if pIngredient == int(Iid):
                        product.setIngredient(Iid,IngredienteProducto)
                        ingredient.setProduct(Pid,ProductoIngrediente)
                    
                
        """for productId in self._products:
            self._products[productId]"""
    
    def listCategories(self):
        
        
        return self._categories

    def checkCategory(self,categoryId):
        """""
        if categoryId not in self._categories:
            return False
        else:
            return True
        """""
        for Cid,category in self._categories.items():
            if Cid==int(categoryId):
               
                return True
        return False    
        
            

    def listProducts(self,Cid):
        productById ={}
        for pid,product in self._products.items():
            if product.getCategory().getId()==int(Cid):
                productById[pid]=product
        return productById

    def checkProduct(self,id):
        for pid,product in self._products.items():
            if pid==int(id):
                return True
        return False

    def checkOrder(self,table):
        for Oid,order in self._Orders.items():
            if Oid==table:
                return True
        return False
            

    def selectProduct(self,id):
        for pid,product in self._products.items():
            if pid==int(id):
                return product


    def addProductOrder(self,table,choice,quantity):
        idorder = str(table) +"."+str(choice)

        product=self.selectProduct(choice)

        value = product.getPrice()*int(quantity)

        newProductOrder = ProductOrder(idorder,product,quantity,value)
        for Oid,order in self._Orders.items():
            if Oid==table:
                order.addProductOrders(idorder,newProductOrder)
        


    def orderDone(self,table):
        for Oid,order in self._Orders.items():
            if Oid==table:
                doneOrder =order
        self._earned=self._earned + float(doneOrder.getCost())
        self._Orders.pop(table)
        
    def seeProfits(self):
        return self._earned


    def addOrder(self,table):
        newOrder =Order(table)
        self._Orders[table]=newOrder
        

    def listOrders(self):
        return self._Orders

    def productName(self,name):
        for pid,product in self._products.items():
            if product.getName()==name:
                return False
        return True

    def categoryName(self,name):
        for cid,category in self._categories.items():
            if category.getName()==name:
                return False
        return True
    
    def ingredientName(self,name):
        for Iid,ingredient in self._ingredients.items():
            if ingredient.getName()==name:
                return False
        return True

    def listIngredients(self):
        
        return self._ingredients

    def listProducts(self):
        

        return self._products

    def checkIngredient(self,id):
        for Iid,ingredient in self._ingredients.items():
            if Iid==int(id):
                return True
        return False

    def addCategory(self,name,description):
        
        category=addCategory(name,description)
        newCategory=self.getCategory(category.getId())
        self._categories[newCategory.getId()]=newCategory

    def addIngredient(self,name,observation):
        
        newIngredient=addIngredient(name,observation)
        self._ingredients[newIngredient.getId()]=newIngredient

    def addProduct(self,name,description,category,productIngredients,price):
        
        newProduct=addProduct(name,description,category,productIngredients,price)
        self._products[newProduct.getId()]=newProduct

    def getCategory(self,id):
        category= getCategory(id)
        for pid,product in self._products.items():
            if product.getCategory() == int(id):
                category.addProducts[pid]=product
        return category

    def getProduct(self,id):
        product= getProduct(id)
        for pIngredient in product.getIngredients():
                for Iid,ingredient in self._ingredients.items():
                    IngredienteProducto = ingredient
                    if pIngredient == int(Iid):
                        product.setIngredient(Iid,IngredienteProducto)
        return product

    def getIngredient(self,id):
        ingredient= getIngredient(id)
        for iProduct in ingredient.getProducts():
                for pid,product in self._products.items():
                    IngredienteProducto = product
                    if iProduct == int(pid):
                        ingredient.setProduct(pid,IngredienteProducto)
        return ingredient

    def delProduct(self,id):
        delProduct(id)
        for pid,product in self._products.items():
            if pid==int(id):
                self._products.pop(pid)
                return True
        return False

    def updateProduct(self,productId,tipo,valor):
        if(updateProduct(productId,tipo,valor)):
            newProduct=self.getProduct(productId)
            newList={}
            newList[int(productId)]=newProduct
            self._products.update(newList)
            return True
        else:
            return False
    
    def updateCategory(self,categoryId,tipo,valor):
        if(updateCategory(categoryId,tipo,valor)):
            newCategory=self.getCategory(categoryId)
            newList={}
            newList[int(categoryId)]=newCategory
            self._categories.update(newList)
            return True
        else:
            return False

    def updateIngredient(self,ingredientId,tipo,valor):
        if(updateIngredient(ingredientId,tipo,valor)):
            newIngredient=self.getIngredient(ingredientId)
            newList={}
            newList[int(ingredientId)]=newIngredient
            self._ingredients.update(newList)
            return True
        else:
            return False
        
    def delCategory(self,id):
        delCategory(id)
        for cid,category in self._categories.items():
            if cid==int(id):
                self._categories.pop(cid)
                return True
        return False

    def delIngredient(self,id):
        delIngredient(id)
        for Iid,ingredient in self._ingredients.items():
            if Iid==int(id):
                self._ingredients.pop(Iid)
                return True
        return False

