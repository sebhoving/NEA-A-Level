from IStrategy import IStrategy

class DCA(IStrategy):
    def __init__(self, the_program) -> None:
        super().__init__(the_program)
        self.NumYears = (self.the_program.stock_data.TimePeriod / 252)
        self.InvestmentFreq = 52  # (weekly)
        self.SplitInvestment = self.the_program.simulation.Investment / (self.NumYears*self.InvestmentFreq)
        self.Shares = 0.0
        self.INTEREST = 1.03
        self.Executed = False
        self.FinalMoney = 0.0
        self.PercentInc = 0.0

    def _PerformStrategy(self):
        print("DCA")
        if not self.Executed:
            for i in range(int(self.NumYears*self.InvestmentFreq-1)):
                self.Shares = self.Shares + (self.SplitInvestment / float(
                    self.the_program.stock_data.DataList[1 + i * (252//self.InvestmentFreq)][1]))  # Testing on open (1)
                
            self.FinalMoney = round((self.Shares * float(self.the_program.stock_data.DataList[-1][1])), 2)
            self.PercentInc = round(((self.FinalMoney / self.the_program.simulation.Investment) - 1) * 100, 2)

            for i in range(int(self.NumYears)):
                self.INTEREST = self.INTEREST * 1.03
        #print(
        #    f"Final number of shares={self.Shares}, this is equal to {self.FinalMoney} pounds at current market price,"
        #    f"this is a {self.PercentInc}% increase,"
        #    f"Interest(At 3%) in same period is {round((self.INTEREST - 1) * 100, 2)}%")
        print(self)
        self.Executed = True
        #return super()._PerformStrategy(curr_strat)

# Daily/weekly/monthly investment
# @TODO: In reality investment amount would be an exponential curve rather than a linear one
