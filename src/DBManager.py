from math import *
import sqlite3
conn = sqlite3.connect('SubDB.db')
c = conn.cursor()


def RequestToList(request):
    c.execute(request)
    return c.fetchall()

RawItems = RequestToList("SELECT Name FROM RawItem")
CraftedItems = RequestToList("SELECT Name FROM CraftedItems")

def RawItemsRecipe(CraftedItem, r = None,num = 1):
    if r == None:
        r = {}
    # request = c.execute("SELECT Material,Quantity FROM CraftedItems WHERE Name=?",(CraftedItem,))
    request = RequestToList("SELECT Material,Quantity FROM CraftedItems WHERE Name=\""+CraftedItem+"\"")[0]
    for Item,qte in zip(request[0].split(","),request[1].split(",")):
        if (Item,) not in RawItems:
            # refaire l'operation
            RawItemsRecipe(Item,r,ceil(int(qte)*num/RequestToList("SELECT Number FROM CraftedItems WHERE Name=\""+Item+"\"")[0][0]))
        else:
            # ajouter les RawItems
            if Item in r.keys():
                r[Item] += int(qte) * num
            else:
                r[Item] = int(qte) * num
    return r

def RawItemsRecipes(CraftedItems, r = None,num = 1):
    if r == None:
        r = {}
    # request = c.execute("SELECT Material,Quantity FROM CraftedItems WHERE Name=?",(CraftedItem,))
    for i in CraftedItems:
        RawItemsRecipe(i,r,num)
    return r
