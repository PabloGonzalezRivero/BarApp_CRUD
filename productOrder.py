class ProductOrder:
    #In odoo its the order_model
    def __init__(self,id,product,quantity,value):
        self.__id = id
        self.__product = product
        self.__quantity = quantity
        self.__value = value

        
    def getId(self):
        return self.__id

    def getQuantity(self):
        return self.__quantity


    def getProduct(self):
        return self.__product
    
    def getValue(self):
        return self.__value