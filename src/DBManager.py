from math import *
import sqlite3
conn = sqlite3.connect('SubDB.db')
c = conn.cursor()


def RequestToList(request,pos):
    l = []
    for i in c.execute(request):
        l.append(i[pos])
    return l

RawItems = RequestToList("SELECT Name FROM RawItem",0)
CraftedItems = RequestToList("SELECT Name FROM CraftedItems",0)

def RawItemsRecipe(CraftedItem, r = None,num = 1):
    if r == None:
        r = {}
    # request = c.execute("SELECT Material,Quantity FROM CraftedItems WHERE Name=?",(CraftedItem,))
    for Item,qte in zip(RequestToList("SELECT Material,Quantity FROM CraftedItems WHERE Name=\""+CraftedItem+"\"",0)[0].split(","),RequestToList("SELECT Material,Quantity FROM CraftedItems WHERE Name=\""+CraftedItem+"\"",1)[0].split(",")):
        if Item not in RawItems:
            # refaire l'operation
            RawItemsRecipe(Item,r,ceil(int(qte)/RequestToList("SELECT Number FROM CraftedItems WHERE Name=\""+Item+"\"",0)[0]))
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
