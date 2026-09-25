from IStrategy import IStrategy
from StrategyUtil import *

class TrendTrading(IStrategy):
    def __init__(self, the_program) -> None:
        super().__init__(the_program)
        self.smaN = 90 # the period the sma is calculated over
        self.emaN = 30 # the period the ema is calculated over
        self.smalist = []
        self.emalist = [int(float(self.the_program.stock_data.DataList[0][1]))]
        self.strengthlist = []
        self.strengthYesterday = 0
        self.crossovers = []
        self.Timeleft = self.the_program.stock_data.TimePeriod
        self.direction = ""
        self.tradingtime = True
        self.executed = False

        #from DCA
        self.NumYears = (self.the_program.stock_data.TimePeriod / 252)
        self.InvestmentFreq = 52  # (weekly)
        self.SplitInvestment = self.the_program.simulation.Investment / (self.NumYears*self.InvestmentFreq)
        self.Shares = 0.0
        self.INTEREST = 1.03
        self.FinalMoney = 0.0
        self.PercentInc = 0.0
        

    def _PerformStrategy(self):
        print("TrendTrading")
        if not self.executed:
            #Create the sma list
        
            for i in range(self.the_program.stock_data.TimePeriod):
                self.smalist.append(StrategyFunctionsForList.CalculateSMA(self.the_program.stock_data.DataList, self.the_program.stock_data.DataList[i][0], self.smaN))
        
            #Create the ema list

            for i in range(self.the_program.stock_data.TimePeriod):
                ema = StrategyFunctionsForList.CalculateEMA(self.the_program.stock_data.DataList, self.the_program.stock_data.DataList[i][0] + timedelta(days=1), self.emaN, self.emalist[-1])
                self.emalist.append(ema)

            #Create strength list to find crossover points

            for i in range(self.the_program.stock_data.TimePeriod):
                self.strengthlist.append(StrategyFunctionsForList.CalculateStrength(i, self.emalist[i], self.smalist[i]))

            #make a list of crossover points
            for i in range(len(self.strengthlist)):
                if (self.strengthlist[i]*self.strengthYesterday) <= 0:
                    self.crossovers.append(self.the_program.stock_data.DataList[i][0])

                self.strengthYesterday = self.strengthlist[i]
            if self.the_program.DEBUG:
                print(self.crossovers)


            if self.strengthlist[1] > 0:
                self.direction = "UP"
            else:
                self.direction = "DOWN"

            #Plan: invest DCA whilst strength above 0 and calculate each investment amount by splitting remaining time period
            
            day = 0
            crossover = 1
            for day in range(self.the_program.stock_data.TimePeriod):
                if self.the_program.stock_data.DataList[day][0] == self.crossovers[crossover]:
                    crossover += 1
                    # need to chnage trading time to false @TODO!!
                if self.tradingtime:
                    if (day % (252//self.InvestmentFreq)) == 0: # dont invest every day
                        self.Shares = self.Shares + (self.SplitInvestment / float(
                            self.the_program.stock_data.DataList[1 + day][1]))  # Testing on open price (1)
                        print(self.Shares)

                day +=1


            #Copied from DCA to be augmented for TrendTrading
            '''
            for i in range(int(self.NumYears*self.InvestmentFreq-1)):
                self.Shares = self.Shares + (self.SplitInvestment / float(
                    self.the_program.stock_data.DataList[1 + i * (252//self.InvestmentFreq)][1]))  # Testing on open (1)
                
            self.FinalMoney = round((self.Shares * float(self.the_program.stock_data.DataList[-1][1])), 2)
            self.PercentInc = round(((self.FinalMoney / self.the_program.simulation.Investment) - 1) * 100, 2)

            for i in range(int(self.NumYears)):
                self.INTEREST = self.INTEREST * 1.03
        print(
            f"Final number of shares={self.Shares}, this is equal to {self.FinalMoney} pounds at current market price,"
            f"this is a {self.PercentInc}% increase,"
            f"Interest(At 3%) in same period is {round((self.INTEREST - 1) * 100, 2)}%")
        self.Executed = True
        '''
        #return super()._PerformStrategy(curr_strat)

# Larger complexity