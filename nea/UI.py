import tkinter as tk
from BuyAndHold import BuyAndHold
from DCA import DCA
from TrendTrading import TrendTrading
import os

class UI(tk.Frame):
    def __init__(self, the_program, parent,  *args, **kwargs):
        # call Frame constructor
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.the_program = the_program

        # build interface
        parent.geometry("600x400")
        parent.title("Strategy Settings")
        self.Create_Frames()
        self.Create_Buttons()
        self.Create_Labels()
        self.Create_Entries()
        self.Create_Checkbuttons()


    def Create_Frames(self):
        self.frm_UI = tk.Frame(self.parent, bg="white")
        self.frm_UI.grid()

    def Create_Labels(self):
        self.lbl_Title = tk.Label(self.frm_UI, fg = "#333333", justify="left", text="Strategy Settings")
        self.lbl_Title.grid(row=0, column=0, columnspan=4)

        self.lbl_DefVals = tk.Label(self.frm_UI, fg = "#333333", justify="left", text="Default values are xx")
        self.lbl_DefVals.grid(row=1, column=0, columnspan=4)

        self.lbl_TimePeriod = tk.Label(self.frm_UI, fg = "#333333", justify="left", text="Time Period(years):")
        self.lbl_TimePeriod.grid(row=2, column=1)

        self.lbl_DataFreq = tk.Label(self.frm_UI, fg = "#333333", justify="left", text="DataFrequency(days):")
        self.lbl_DataFreq.grid(row=3, column=1)

    def Create_Entries(self):
        self.ent_TimePeriod = tk.Entry(self.frm_UI, borderwidth="1px",  fg = "#333333", justify="left", text=tk.StringVar)
        self.ent_TimePeriod.grid(row=2, column=2, columnspan=2)

        self.ent_DataFreq = tk.Entry(self.frm_UI, borderwidth="1px",  fg = "#333333", justify="left", text=tk.StringVar)
        self.ent_DataFreq.grid(row=3, column=2, columnspan=2)

    def Create_Checkbuttons(self):
        self.chk_btnDCA = tk.Checkbutton(self.frm_UI, fg = "#333333", justify="left", text="DCA", 
                                      offvalue= 0, onvalue=1, command= lambda: self.the_program.simulation.AddDelStrategy(DCA(self.the_program)))
        self.chk_btnDCA.grid(row=2, column=0)

        self.chk_btnBandH = tk.Checkbutton(self.frm_UI, fg = "#333333", justify="left", text="BuyAndHold", 
                                      offvalue= 0, onvalue=1, command= lambda: self.the_program.simulation.AddDelStrategy(BuyAndHold(self.the_program)))
        self.chk_btnBandH.grid(row=3, column=0)

        self.chk_btnTrendTrade = tk.Checkbutton(self.frm_UI, fg = "#333333", justify="left", text="TrendTrade", 
                                      offvalue= 0, onvalue=1, command= lambda: self.the_program.simulation.AddDelStrategy(TrendTrading(self.the_program)))
        self.chk_btnTrendTrade.grid(row=4, column=0)

    def Create_Buttons(self):
        self.btn_TimePeriod = tk.Button(self.frm_UI, activebackground="red", bg="green",
                                 command=lambda: self.the_program.stock_data.AlterTimePeriod(self.ent_TimePeriod.get()),
                                 text="Amend Time Period")
        self.btn_TimePeriod.grid(row=2, column=4)

        self.btn_DataFreq = tk.Button(self.frm_UI, activebackground="red", bg="green",
                                 command=lambda: self.the_program.stock_data.AlterDataFrequency(self.ent_DataFreq.get()),
                                 text="Amend Data Frequency")
        self.btn_DataFreq.grid(row=3, column=4)

        self.btn_Test = tk.Button(self.frm_UI, activebackground="red", bg="green",
                                 command=lambda: self.the_program.simulation.RunStrategies(),
                                 text="Test")
        self.btn_Test.grid(row=5, column=0, columnspan=4)
        '''
        self.btn_TimePeriod = tk.Button(self.parent, activebackground="red", bg="green",
                                 command=lambda: self.the_program.simulation.AddDCA(), width=20,
                                 text="Add DCA Strategy")
        self.btn_DCA.grid(row=0, column=1, padx=1, pady=1)

        self.btn_BuyAndHold = tk.Button(self.parent, activebackground="red", bg="green",
                                 command=lambda: self.the_program.simulation.AddBuyAndHold(), width=20,
                                 text="Add BuyAndHold Strategy")
        self.btn_BuyAndHold.grid(row=0, column=2, padx=1, pady=1)

        self.btn_Run = tk.Button(self.parent, activebackground="red", bg="green",
                                        command=lambda: self.the_program.simulation.RunStrategies(), width=20,
                                        text="Test Strategies")
        self.btn_Run.grid(row=0, column=3, padx=1, pady=1)
        '''

    def run(self):
        UI.grid(self)
        self.parent.mainloop()

    def restart(self):
        self.parent.destroy()
        self.the_program.ui = UI(self.the_program, tk.Tk())
        self.the_program.ui.run()
