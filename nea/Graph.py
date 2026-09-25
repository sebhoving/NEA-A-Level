# from ast import main
from datetime import timedelta
from sys import maxsize
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter.ttk import *
import math
from GraphUtil import *


class Graph(tk.Frame):
    def __init__(self, the_program, parent,  *args, **kwargs):
        # call Frame constructor
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.the_program = the_program

        # build interface
        self.Create_Frames()
        self.Create_Graph()
        

    def Create_Frames(self):
        self.frm_Graph = tk.Frame(self.parent, bg = "blue", width= 500, height= 180)
        self.frm_Graph.grid(row = 0, column = 1, padx = 0, pady = 0)

   
    def Create_Graph(self):
        self.canvas = tk.Canvas(self.frm_Graph, background="gray57", width= 700, height = 500)
        self.canvas.grid(row=0,column=1, padx = (0,50))

        self.canvas.create_line(30, 20, 30, 400, fill="black", width=2) # y-axis
        self.canvas.create_line(29, 400, 500, 400, fill="black", width=2)  # x-axis

        # import the data using parsingeggstock2.py
        # EggStock = Datafile("Download Data - DJIA.csv")
        # EggStock.DataList = Parse.CreateDataList("Download Data - DJIA.csv")
        # print(EggStock.DataList)
        
        #Find the scaling function for x
        xscaler = GraphCalculations.DateCalcs(self.the_program.stock_data.DataList)

        #Create Pricelist
        pricelist = []
        for i in range(len(self.the_program.stock_data.DataList)):
            pricelist.append(float(self.the_program.stock_data.DataList[i][1]))
        
        
        #Normalise Pricelist
        Normpricelist = pricelist        
        GraphCalculations.NormalisePriceList(Normpricelist)

        #Create Pricelist again cos i had a weird issue
        pricelist = []
        for i in range(len(self.the_program.stock_data.DataList)):
            pricelist.append(float(self.the_program.stock_data.DataList[i][1]))

        # Draw Pricelist
        for i in range(len(Normpricelist)-1):
            self.canvas.create_line((i*xscaler),400-(Normpricelist[i]*300),((i+1)*xscaler),400-(Normpricelist[i+1]*300), fill="green", width=1)

        # use the imported functions to find the sma
        smalist = []
        for i in range(len(pricelist)):
            smalist.append(GraphCalculations.CalculateSMA(self.the_program.stock_data.DataList, self.the_program.stock_data.DataList[i][0], 90))
        
        smalist = GraphCalculations.NormalisePriceListWithMaxList(smalist, pricelist)
        
        
        # Draw sma
        for i in range(len(smalist)-1):
            self.canvas.create_line((i*xscaler),400-(smalist[i]*300),((i+1)*xscaler),400-(smalist[i+1]*300), fill="blue", width=1) # line joining 2 sma points

        #use the imported functions to find the ema
        x = int(float(self.the_program.stock_data.DataList[0][1]))
        emalist = [x]
        for i in range(len(pricelist)):
            ema = GraphCalculations.CalculateEMA(self.the_program.stock_data.DataList, self.the_program.stock_data.DataList[i][0] + timedelta(days=1), 30, emalist[-1])
            emalist.append(ema)
        
        
        emalist = GraphCalculations.NormalisePriceListWithMaxList(emalist,pricelist)
        

        #Draw ema
        for i in range(len(emalist)-1):
            self.canvas.create_line((i*xscaler),400-(emalist[i]*300),((i+1)*xscaler),400-(emalist[i+1]*300), fill="red", width=1) # line joining 2 sma points
        
        #use the imported functions to find the strength
        strengthlist = []
        for i in range(len(pricelist)):
            strengthlist.append(GraphCalculations.CalculateStrength(i, emalist[i], smalist[i]))
        MAX = [0.5]
        strengthlist = GraphCalculations.NormalisePriceListWithMaxList(strengthlist, MAX)

        #Draw strength
        for i in range(len(strengthlist)-1):
            self.canvas.create_line((i*xscaler),300-(strengthlist[i]*300),((i+1)*xscaler),300-(strengthlist[i+1]*300), fill="purple", width=1) # line joining 2 sma points
            self.canvas.create_line(30,300,630,300, fill="purple", width=1)
        '''
        if self.the_program.DEBUG:
            print(f"length of smalist is {len(smalist)}, length of emalist is {len(emalist)}, length of pricelist is {len(pricelist)}, length of strengthlist is {len(strengthlist)}")
            '''


    def run(self):
        Graph.grid(self)
        self.parent.mainloop()
