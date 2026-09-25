from Graph import *
from Simulation import *
from StockData import *
from UI import *
import tkinter as tk

class Program:
    def __init__(self):
        self.stock_data = StockData(self,"IUCS.L.csv")
        self.simulation = Simulation(self)
        #self.graph = Graph(self, tk.Tk())
        self.ui = UI(self, tk.Tk())
        self.DEBUG = False


if __name__ == "__main__":
    theProgram = Program()
    theProgram.ui.run()

