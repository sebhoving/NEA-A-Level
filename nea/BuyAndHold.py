from tkinter import ROUND
from IStrategy import IStrategy
import math

class BuyAndHold(IStrategy):

    def __init__(self, the_program) -> None:
        super().__init__(the_program)
        self.NumYears = (self.the_program.stock_data.TimePeriod//252)
        self.YearlyInvestment = self.the_program.simulation.Investment / self.NumYears
        self.Shares = 0.0
        self.INTEREST  = 1.03
        self.Executed = False
        self.FinalMoney = 0.0
        self.PercentInc = 0.0

    def _PerformStrategy(self):
        print("BuyAndHold")
        if not self.Executed:
            for i in range(self.NumYears):
                self.Shares = self.Shares + (self.YearlyInvestment / float(self.the_program.stock_data.DataList[1+i*252][1])) # Testing on open (1)
                if self.the_program.DEBUG:
                    print(f"shares = {self.Shares}")
            self.FinalMoney = round((self.Shares*float(self.the_program.stock_data.DataList[-1][1])),2)
            self.PercentInc = round(((self.FinalMoney/self.the_program.simulation.Investment)-1)*100,2)

            for i in range(self.NumYears):
                self.INTEREST  = self.INTEREST *1.03
        print(f"Final number of shares={self.Shares}, this is equal to {self.FinalMoney}pounds at current market price,"
              f"this is a {self.PercentInc}% increase, "
              f"Interest(At 3%) in same period is {round((self.INTEREST -1)*100,2)}%")
        self.Executed = True
        #return super()._PerformStrategy(curr_strat)

