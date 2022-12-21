import json
import requests
from category import Category
from product import Product
from ingredient import Ingredient


def getCategories():
        url = "http://localhost:8069/bar_app/category"

        querystring = {""}

        headers = {
        }
        responseC = requests.request("GET",url)
        if responseC.status_code == 200:
            dataC = responseC.json()
            categories = {} # Key -> Id, Value --> Category
            for c in range(len(dataC["data"])) :   
                categoryId = dataC["data"][c]["id"]
                categoryName = dataC["data"][c]["name"]
                categoryDescription = dataC["data"][c]["description"]
                categoryProducts ={}
                for cat in range(len(dataC["data"][c]["products"])):
                    product = dataC["data"][c]["products"][cat]
                    categoryProducts[product]= product
                newCategory = Category(categoryId,categoryName,categoryDescription,categoryProducts)
                categories[categoryId] = newCategory
        return categories
        
def getIngredients():
        url = "http://localhost:8069/bar_app/ingredient"

        querystring = {""}

        headers = {
        }
        responseI = requests.request("GET",url)
        if responseI.status_code == 200:
            dataI = responseI.json()
            ingredients = {} # Key -> Id, Value --> Ingredient
            for i in range(len(dataI["data"])) :    
                ingredientId = dataI["data"][i]["id"]
                ingredientName = dataI["data"][i]["name"]
                ingredientObservation = dataI["data"][i]["observation"]
                ingredientProducts = {}
                for cat in range(len(dataI["data"][i]["products"])):
                    product = dataI["data"][i]["products"][cat]
                    ingredientProducts[product]= product
                newIngredient = Ingredient(ingredientId,ingredientName,ingredientObservation,ingredientProducts)
                ingredients[ingredientId] = newIngredient
        return ingredients
    
def getProducts():
        url = "http://localhost:8069/bar_app/products"

        querystring = {""}

        headers = {
        }
        responseP = requests.request("GET",url)
        if responseP.status_code == 200:
            dataP = responseP.json()
            products = {} # Key -> Id, Value --> Product
            for p in range(len(dataP["data"])) :    
                productId = dataP["data"][p]["id"]
                productName = dataP["data"][p]["name"]
                productDescription = dataP["data"][p]["description"]
                catID = dataP["data"][p]["category"][0]
                catName = dataP["data"][p]["category"][1]
                productCategory = Category(catID,catName,"null","null")
                productIngredients={}
                for nIng in range(len(dataP["data"][p]["ingredients"])):
                     Pingred= dataP["data"][p]["ingredients"][nIng]
                     productIngredients[Pingred]=Pingred
                productPrice = dataP["data"][p]["price"]
                newProduct = Product(productId,productName,productDescription,productCategory,productIngredients,productPrice)
                products[productId] = newProduct
        return products

def addIngredient(name,observation):
    ingredient = {}
    ingredient["name"]=name
    ingredient["observation"]=observation

    response = requests.request("POST", "http://localhost:8069/bar_app/addIngredient", json=ingredient).text

    response = json.loads(response)

    categoryid=response["result"]["id"]
    newingredient= Category(categoryid,name,observation,products={})
    return newingredient

def addCategory(name,description):
    category = {}
    category["name"]=name
    category["description"]=description

    response = requests.request("POST", "http://localhost:8069/bar_app/addCategory", json=category).text

    response = json.loads(response)

    categoryid=response["result"]["id"]
    newCategory = Category(categoryid,name,description,products={})
    return newCategory

def addProduct(name,description,category,productIngredients,price):
     
    
     product = {} 
     product["name"] = name 
     product["description"] = description
     product["category"] = category
     product["price"] = price
 

     product["ingredients"]=list(productIngredients.values())

     response = requests.request("POST", "http://localhost:8069/bar_app/addProduct", json=product).text

     response = json.loads(response)

     productid=response["result"]["id"]
     newProduct = Product(productid,name,description,category,productIngredients,price)
     return newProduct

def getProduct(id):
    url ="http://localhost:8069/bar_app/getProduct/"
    responseP = requests.request("GET",url+str(id))
    
  
    if responseP.status_code == 200:
            dataP = responseP.json()  
            productId = dataP["data"][0]["id"]
            productName = dataP["data"][0]["name"]
            productDescription = dataP["data"][0]["description"]
            catID = dataP["data"][0]["category"][0]
            catName = dataP["data"][0]["category"][1]
            productCategory = Category(catID,catName,"null","null")
            productIngredients={}
            for nIng in range(len(dataP["data"][0]["ingredients"])):
                    Pingred= dataP["data"][0]["ingredients"][nIng]
                    productIngredients[Pingred]=Pingred
            productPrice = dataP["data"][0]["price"]
            newProduct = Product(productId,productName,productDescription,productCategory,productIngredients,productPrice)
            return newProduct

def getCategory(id):
    url ="http://localhost:8069/bar_app/getCategory/"
    response = requests.request("GET",url+str(id))
    
  
    if response.status_code == 200:
        dataC = response.json()
        categoryId = dataC["data"][0]["id"]
        categoryName = dataC["data"][0]["name"]
        categoryDescription = dataC["data"][0]["description"]
        
        newCategory = Category(categoryId,categoryName,categoryDescription,"null")
        return newCategory

def getIngredient(id):
    url ="http://localhost:8069/bar_app/getIngredient/"
    response = requests.request("GET",url+str(id))
    
  
    if response.status_code == 200:
        dataI = response.json()
        ingredientId = dataI["data"][0]["id"]
        ingredientName = dataI["data"][0]["name"]
        ingredientObservation = dataI["data"][0]["observation"]
        ingredientProducts = {}
        for cat in range(len(dataI["data"][0]["products"])):
            product = dataI["data"][0]["products"][cat]
            ingredientProducts[product]= product
        newIngredient = Ingredient(ingredientId,ingredientName,ingredientObservation,ingredientProducts)

        return newIngredient

def updateIngredient(ingredientId,tipo,valor):
     ingredient = {} 
     ingredient["id"]=ingredientId
     
     ingredient[tipo] = valor
     
     response = requests.request("PUT", "http://localhost:8069/bar_app/updateIngredient", json=ingredient).text
     response = json.loads(response)
     if response["result"]["status"] == 201:
        return True

def delIngredient(id):
    ingredient = {} 
    ingredient["id"]=id
    response = requests.request("DELETE", "http://localhost:8069/bar_app/deleteIngredient", json=ingredient).text

    response = json.loads(response)

def delProduct(id):
    product = {} 
    product["id"]=id
    response = requests.request("DELETE", "http://localhost:8069/bar_app/deleteProduct", json=product).text

    response = json.loads(response)

def updateProduct(productId,tipo,valor):
     product = {} 
     product["id"]=productId
     if(type(valor) is dict):
        product[tipo] = list(valor.values())
     else:
        product[tipo] = valor
     
     response = requests.request("PUT", "http://localhost:8069/bar_app/updateProduct", json=product).text
     response = json.loads(response)
     if response["result"]["status"] == 201:
        return True

def updateCategory(categoryId,tipo,valor):
     category = {} 
     category["id"]=categoryId
     
     category[tipo] = valor
     
     response = requests.request("PUT", "http://localhost:8069/bar_app/updateCategory", json=category).text
     response = json.loads(response)
     if response["result"]["status"] == 201:
        return True

def delCategory(id):
    category = {} 
    category["id"]=id
    response = requests.request("DELETE", "http://localhost:8069/bar_app/deleteCategory", json=category).text

    response = json.loads(response)
     
     
     

        

