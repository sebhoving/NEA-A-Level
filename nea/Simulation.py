# from ast import main
from datetime import timedelta
from sys import maxsize
import math
from DCA import DCA
from BuyAndHold import BuyAndHold
from TrendTrading import TrendTrading
from IStrategy import *

# View of the stock data, overlay one or many strategies and show a result for a strategy.
class Simulation:
    def __init__(self, the_program) -> None:
        self.the_program = the_program
        self.ActiveStrategies = []
        self.strategy = IStrategy(the_program)
        self.dca = False
        self.bandh = False
        self.trendtrade = False
        self.Investment = 100000

    def ClearStrategies(self):
        
        self.ActiveStrategies = []
        self.dca = False
        self.bandh = False
        self.trendtrade = False

    def AddDelStrategy(self, Strat):

        if isinstance(Strat, DCA) and not self.dca:
            self.ActiveStrategies.append(Strat)
            self.dca = True
            if self.the_program.DEBUG:
                print(f"should have added DCA, list = {self.ActiveStrategies}")
                print(f"{self.dca} => should be TRUE")
            
        elif isinstance(Strat, DCA) and self.dca:
            for strat in self.ActiveStrategies:
                if isinstance(Strat, DCA):
                    self.ActiveStrategies.remove(strat)
                    self.dca = False
            if self.the_program.DEBUG:    
                print(f"should have Removed DCA, list = {self.ActiveStrategies}")
                print(f"{self.dca} => should be False")

        if self.the_program.DEBUG:
            print(f"{isinstance(Strat, BuyAndHold) and not self.bandh} => {type(Strat)}")

        if isinstance(Strat, BuyAndHold) and not self.bandh:
            self.ActiveStrategies.append(Strat)
            self.bandh = True
            if self.the_program.DEBUG:    
                print(f"should have added BuyHold, list = {self.ActiveStrategies}")
                print(f"{self.bandh} => should be TRUE")

        elif isinstance(Strat, BuyAndHold) and self.bandh:
            for strat in self.ActiveStrategies:
                if isinstance(strat, BuyAndHold):
                    self.ActiveStrategies.remove(strat)
                    self.bandh = False
            if self.the_program.DEBUG:    
                print(f"should have Removed BuyHold, list = {self.ActiveStrategies}")
                print(f"{self.bandh} => should be False")

        if isinstance(Strat, TrendTrading) and not self.trendtrade:
            self.ActiveStrategies.append(Strat)
            self.trendtrade = True
            if self.the_program.DEBUG:
                print(f"should have added trendtrading, list = {self.ActiveStrategies}")
                print(f"{self.trendtrade} => should be TRUE")
            
        elif isinstance(Strat, TrendTrading) and self.trendtrade:
            for strat in self.ActiveStrategies:
                if isinstance(Strat, TrendTrading):
                    self.ActiveStrategies.remove(strat)
                    self.trendtrade = False
            if self.the_program.DEBUG:    
                print(f"should have Removed TrendTrading, list = {self.ActiveStrategies}")
                print(f"{self.trendtrade} => should be False")



    def RunStrategies(self):
        if self.the_program.DEBUG:  
            print(self.ActiveStrategies)
        # call run on all active strategies
        for curr_strat in self.ActiveStrategies:
            # curr_strat is an instance of Strategy
            curr_strat._PerformStrategy()

