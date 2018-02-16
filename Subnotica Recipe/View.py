from DBManager import *
from tkinter import *

class View(object):
    """docstring for View."""
    def __init__(self, master):
        self.__b1 = Listbox(master)
        self.__b2 = Listbox(master)
        self.__b1.pack(side=LEFT, fill=BOTH, expand=1)
        self.__b2.pack(side=LEFT, fill=BOTH, expand=1)
        for i in CraftedItems:
            self.__b1.insert(END, i)
        self.__b1.bind("<<ListboxSelect>>", self.ShowRecipe)

    def ShowRecipe(self,a):
        self.__b2.delete(0, END)
        itemlistindex = self.__b1.curselection()
        itemlist = []

        for i in itemlistindex:
            itemlist.append(self.__b1.get(i))

        r = []

        try:
            for i,j in RawItemsRecipes(itemlist).items():
                r.append(i+" : "+str(j))
        except:
            r.append("Cannot Compute")

        self.__b2.insert(END, "Raw Item Recipe :")
        self.__b2.insert(END, "")

        for i in r:
            self.__b2.insert(END, i)

        self.__b2.insert(END, "")
        self.__b2.insert(END, "Base Item Recipe :")
        self.__b2.insert(END, "")

        for i in itemlist:
            self.__b2.insert(END, i + " :")
            self.__b2.insert(END, "")
            for j,k in zip(RequestToList("SELECT Material,Quantity FROM CraftedItems WHERE Name=\""+i+"\"",0)[0].split(","),RequestToList("SELECT Material,Quantity FROM CraftedItems WHERE Name=\""+i+"\"",1)[0].split(",")):
                self.__b2.insert(END, j + " : " + k )
