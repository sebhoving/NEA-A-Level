import datetime



class IStrategy():
    def __init__(self, the_program) -> None:
        self.the_program = the_program
        self.Shares = -1.0
        self.INTEREST = -1.0
        self.Executed = False
        self.FinalMoney = -1.0
        self.PercentInc = -1.0

    def _PerformStrategy(self):
        print("IStrategy should never appear") 
        #Perform the calculations necessary and return data

    def __repr__(self) -> str:
        return(
           f"""Final number of shares={self.Shares}, this is equal to {self.FinalMoney} pounds at current market price,\n
           this is a {self.PercentInc}% increase,\n
           Interest(At 3%) in same period is {round((self.INTEREST - 1) * 100, 2)}%""")

        



# if __name__ == "__main__":
#     EggStock = Datafile("Download Data - DJIA.csv")
#     EggStock.DataList = Parse.CreateDataList("Download Data - DJIA.csv")
#     InvestmentStrategy = Strategy(1000.00, 7, 7, 2023)
#     Strategy.DCA(InvestmentStrategy, EggStock)