class Order:
    #In odoo its Table_model
    def __init__(self,table):
        self.__table = table
        self.__productOrders = {}
        self.__cost = 0


    def getTable(self):
        return self.__table

    def getCost(self):
        return self.__cost

    def getProductOrders(self):
        return self.__productOrders
    
    def addProductOrders(self,id,productOrder):
        self.__productOrders[id]=productOrder
        self.__cost=self.__cost+ productOrder.getValue()
