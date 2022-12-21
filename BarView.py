from BarControler import BarController
from datetime import datetime
controler = BarController()

def listCategories():
    categories = controler.listCategories()
    for id,category in categories.items():
        print("\n")
        print("Name: ",category.getName())
        print("\t Category ID: ",category.getId())
        print("\t Description: ",category.getDescription())
        print("\n")

def listProducts(categoryId):
    if controler.checkCategory(categoryId):
        products = controler.listProducts(categoryId)
        for pid,product in products.items():
            print("\n")
            print("Name: ",product.getName())
            print("\t Product ID: ",pid)
            print("\t Description: ",product.getDescription())
            print("\t Ingredients:")
            ingredients = product.getIngredients()
            for Iid,i in  ingredients.items():
                print("\t\t Ingredient: ",i.getName())
            print("\t Price: ",product.getPrice())
            print("\n")
    else:
        print("The id doesn't belong to any category")

def addOrder():
    table = input("Enter the number of the table: ")

    choice = 1
    controler.addOrder(table)  
    while(choice!=0):
        choice = int(input("Enter the id of the product (Enter 0 to end): "))
        if controler.checkProduct(choice):
            if(choice!=0):
                quant = input("Enter the quantity of the product: ")
                if(int(quant)>0):
                    controler.addProductOrder(table,choice,quant)
                    
                else:
                    print("The quantity of the product has to be grater than 0")
        elif(choice==0):
            break
        else:
            print("Product not found. Try again.")
     
        
def ListOrders():
    orders = controler.listOrders()
    for id,order in orders.items():
        print("\n")
        print("Table: ",order.getTable())
        productOrders = order.getProductOrders()
        for Pid,productOrder in  productOrders.items():
            print("\t\t Product: ",productOrder.getProduct().getName()," - Quantity: ",productOrder.getQuantity())
        print("\t Cost: ",order.getCost(),"€")
        print("\n")
    
def markDone():
    table = input("Enter the table of the order: ")
    if controler.checkOrder(table):
        controler.orderDone(table)
        print("Order done")
    else:
        print("ERROR: Order not found")

def profits():
    profit = controler.seeProfits()
    print("Profit of today until now: ",profit,"€")

def finalProfit():
    profit = controler.seeProfits()
    print("Final profit: ",profit,"€")

#Next lines are about the CRUD 

def listIngredients():
    ingredients = controler.listIngredients()
    for Iid,ingredient in  ingredients.items():
        print("Id: ",ingredient.getId(), " - Ingredient: ",ingredient.getName())

def listProducts():
    products = controler.listProducts()
    for pid,product in  products.items():
        print("Id: ",product.getId(), " - Name: ",product.getName())

#CRUD PRODUCT

def addProduct():
    name = input("Enter the name of the product: ")
    if controler.productName(name):
        description = input("Enter the description of the product: ")
        listCategories()
        category = input("Enter the id of the category for the product: ")
        productIngredients={}
        #productIngredients=""
        listIngredients()
        choiceI=1
        while(choiceI!=0):
            choiceI = int(input("Enter the id of the ingredient (Enter 0 to end): "))
            if controler.checkIngredient(choiceI):
                if(choiceI!=0):
                    productIngredients[choiceI]=int(choiceI)
            elif(choiceI==0):
                break
            else:
                print("Ingredient not found. Try again.")
        price = input("Enter the price of the product: ")
        controler.addProduct(name,description,category,productIngredients,price)
    else:
        print("There's already a product with that name.")

def getProduct():
    listProducts()
    productId=input("Enter the id of the product: ")
    if(controler.checkProduct(productId)):
        newProduct=controler.getProduct(productId)
        print("\n")
        print("Name: ",newProduct.getName())
        print("\t Product ID: ",newProduct.getId())
        print("\t Description: ",newProduct.getDescription())
        print("\t Category: ",newProduct.getCategory().getName())
        print("\t Ingredients:")
        ingredients = newProduct.getIngredients()
        for Iid,i in  ingredients.items():
                print("\t\t Ingredient: ",i.getName())
        print("\t Price: ",newProduct.getPrice())
        print("\n")
    else:
        print("There is no product with that id")

def delProduct():
    listProducts()
    productId=input("Enter the id of the product: ")
    if(controler.checkProduct(productId)):
        if(controler.delProduct(productId)):
            print("The product has been removed")
        else:
            print("Error. The product hasn't been removed")
    else:
        print("There is no product with that id")

def updateProduct():
    listProducts()
    productId=input("Enter the id of the product: ")
    if(controler.checkProduct(productId)):
        print("Choose what to update from the product")
        print("1.- Name")
        print("2.- Description")
        print("3.- Category")
        print("4.- Ingredients")
        print("5.- Price")
        print("6.- Return")
        UpdateoptionProduct = int(input("Choose option: "))
        print("\n")
        if(UpdateoptionProduct == 1):
            tipo="name"
            value=input("Enter the new name for the product: ")
            if controler.updateProduct(productId,tipo,value):
                print("Product updated")
            else:
                print("Error. The product hasn't been updated")
        elif(UpdateoptionProduct == 2):
            tipo="description"
            value=input("Enter the new description for the product: ")
            if controler.updateProduct(productId,tipo,value):
                print("Product updated")
            else:
                print("Error. The product hasn't been updated")
        elif(UpdateoptionProduct == 3):
            tipo="category"
            value=input("Enter the new category for the product: ")
            if controler.updateProduct(productId,tipo,value):
                print("Product updated")
            else:
                print("Error. The product hasn't been updated")
        elif(UpdateoptionProduct == 4):
            tipo="ingredients"
            print("Select all the ingredients of the product")
            productIngredients={}
            listIngredients()
            choiceI=1
            while(choiceI!=0):
                choiceI = int(input("Enter the id of the ingredient (Enter 0 to end): "))
                if controler.checkIngredient(choiceI):
                    if(choiceI!=0):
                        productIngredients[choiceI]=int(choiceI)
                elif(choiceI==0):
                    break
                else:
                    print("Ingredient not found. Try again.")
            if controler.updateProduct(productId,tipo,productIngredients):
                print("Product updated")
            else:
                print("Error. The product hasn't been updated")
        elif(UpdateoptionProduct == 5):
            tipo="price"
            value=input("Enter the new price for the product: ")
            if controler.updateProduct(productId,tipo,value):
                print("Product updated")
            else:
                print("Error. The product hasn't been updated")
        elif(UpdateoptionProduct == 6):
            print("\n")
        else:
            print("Option error")
    else:
        print("There is no product with that id")

#CRUD Category
def addCategory():
    name = input("Enter the name of the category: ")
    if controler.categoryName(name):
        description = input("Enter the description of the category: ")
        controler.addCategory(name,description)
    else:
        print("There's already a category with that name.")

def getCategory():
    listCategories()
    categoryId=input("Enter the id of the category: ")
    if controler.checkCategory(categoryId):
        newCategory=controler.getCategory(categoryId)
        print("\n")
        print("Name: ",newCategory.getName())
        print("\t Category ID: ",newCategory.getId())
        print("\t Description: ",newCategory.getDescription())
        print("\n")
    else:
        print("The id doesn't belong to any category")
    
def updateCategory():
    listCategories()
    categoryId=input("Enter the id of the category: ")
    if controler.checkCategory(categoryId):
        print("Choose what to update from the category")
        print("1.- Name")
        print("2.- Description")
        print("3.- Return")
        UpdateoptionCategory = int(input("Choose option: "))
        print("\n")
        if(UpdateoptionCategory == 1):
            tipo="name"
            value=input("Enter the new name for the category: ")
            if controler.updateCategory(categoryId,tipo,value):
                print("Category updated")
            else:
                print("Error. The category hasn't been updated")
        elif(UpdateoptionCategory == 2):
            tipo="description"
            value=input("Enter the new description for the category: ")
            if controler.updateCategory(categoryId,tipo,value):
                print("Category updated")
            else:
                print("Error. The category hasn't been updated")
        elif(UpdateoptionCategory == 3):
            print("\n")
        else:
            print("Option error")
    else:
        print("The id doesn't belong to any category")

def delCategory():
    listCategories()
    categoryId=input("Enter the id of the category: ")
    if(controler.checkCategory(categoryId)):
        if(controler.delCategory(categoryId)):
            print("The category has been removed")
        else:
            print("Error. The category hasn't been removed")
    else:
        print("There is no category with that id")

#CRUD Ingredient
def addIngredient():
    name = input("Enter the name of the Ingredient: ")
    if controler.ingredientName(name):
        observation = input("Enter the observation of the Ingredient: ")
        controler.addIngredient(name,observation)
    else:
        print("There's already a Ingredient with that name.")

def getIngredient():
    listIngredients()
    IngredientId=input("Enter the id of the Ingredient: ")
    if controler.checkIngredient(IngredientId):
        newIngredient=controler.getIngredient(IngredientId)
        print("\n")
        print("Name: ",newIngredient.getName())
        print("\t Ingredient ID: ",newIngredient.getId())
        print("\t Observation: ",newIngredient.getObservation())
        print("\n")
    else:
        print("The id doesn't belong to any Ingredient")
    
def updateIngredient():
    listIngredients()
    IngredientId=input("Enter the id of the Ingredient: ")
    if controler.checkIngredient(IngredientId):
        print("Choose what to update from the Ingredient")
        print("1.- Name")
        print("2.- Observation")
        print("3.- Return")
        UpdateoptionIngredient = int(input("Choose option: "))
        print("\n")
        if(UpdateoptionIngredient == 1):
            tipo="name"
            value=input("Enter the new name for the Ingredient: ")
            if controler.updateIngredient(IngredientId,tipo,value):
                print("Ingredient updated")
            else:
                print("Error. The Ingredient hasn't been updated")
        elif(UpdateoptionIngredient == 2):
            tipo="observation"
            value=input("Enter the new observation for the Ingredient: ")
            if controler.updateIngredient(IngredientId,tipo,value):
                print("Ingredient updated")
            else:
                print("Error. The Ingredient hasn't been updated")
        elif(UpdateoptionIngredient == 3):
            print("\n")
        else:
            print("Option error")
    else:
        print("The id doesn't belong to any Ingredient")

def delIngredient():
    listIngredients()
    IngredientId=input("Enter the id of the Ingredient: ")
    if(controler.checkIngredient(IngredientId)):
        if(controler.delIngredient(IngredientId)):
            print("The Ingredient has been removed")
        else:
            print("Error. The Ingredient hasn't been removed")
    else:
        print("There is no Ingredient with that id")

while True:  
    print("\n")
    print("1.- Enter the CRUD mode")
    print("2.- Ener the Order mode")
    print("3.- Exit")
    optionM = int(input("Choose option: "))
    print("\n")
    if(optionM == 3):
        

        print("\n GOODBYE")
        break
    elif (optionM == 1):
        while True:  
            print("\n")
            print("1.- CRUD product")
            print("2.- CRUD category")
            print("3.- CRUD ingredient")
            print("4.- Return")
            CRUDoption = int(input("Choose option: "))
            print("\n")
            if(CRUDoption == 4):
                break
            elif (CRUDoption == 1):
                #CRUD of the product
                print("1.- Create new Product")
                print("2.- Read selected Product")
                print("3.- Update selected Product")
                print("4.- Delete selected Product")
                print("5.- Return")
                optionProduct = int(input("Choose option: "))
                print("\n")
                if(optionProduct == 5):
                    break
                elif(optionProduct == 1):
                    addProduct()
                elif(optionProduct == 2):
                    getProduct()
                elif(optionProduct == 3):
                    updateProduct()
                elif(optionProduct == 4):
                    delProduct()
                else:
                    print("Option error")
            elif (CRUDoption == 2):
               #CRUD of the category
                print("1.- Create new Category")
                print("2.- Read selected Category")
                print("3.- Update selected Category")
                print("4.- Delete selected Category")
                print("5.- Return")
                optionCategory = int(input("Choose option: "))
                print("\n")
                if(optionCategory == 5):
                    break
                elif(optionCategory == 1):
                    addCategory()
                elif(optionCategory == 2):
                    getCategory()
                elif(optionCategory == 3):
                    updateCategory()
                elif(optionCategory == 4):
                    delCategory()
                else:
                    print("Option error")
                
            elif (CRUDoption == 3):
                #CRUD of the category
                print("1.- Create new Ingredient")
                print("2.- Read selected Ingredient")
                print("3.- Update selected Ingredient")
                print("4.- Delete selected Ingredient")
                print("5.- Return")
                optionIngredient = int(input("Choose option: "))
                print("\n")
                if(optionIngredient == 5):
                    break
                elif(optionIngredient == 1):
                    addIngredient()
                elif(optionIngredient == 2):
                    getIngredient()
                elif(optionIngredient == 3):
                    updateIngredient()
                elif(optionIngredient == 4):
                    delIngredient()
                else:
                    print("Option error")

            else:
                print("Option error")
            
    elif (optionM == 2):
        while True:  
            print("\n")
            print("1.- List categories")
            print("2.- List products from a category")
            print("3.- Made an order")
            print("4.- List active orders")
            print("5.- Mark an order as done")
            print("6.- See the current profit of today")
            print("7.- Exit")
            option = int(input("Choose option: "))
            print("\n")
            if(option == 7):
                finalProfit()

                print("\n BYE")
                break
            elif (option == 1):
                listCategories()
                
            elif (option == 2):
                categoryId = input("Enter the id of the wanted category: ")
                listProducts(categoryId)
                
            elif (option == 3):
                addOrder()
                
                
            elif (option == 4):
                ListOrders()
                
            elif (option == 5):
                markDone()

            elif (option == 6):
                profits()

            else:
                print("Option error")
    else:
        print("Option error")

    
