from ast import main
import re, csv, datetime
from tracemalloc import start
from datetime import timedelta

class StrategyFunctionsForList:
    @staticmethod
    def CalculateSMA(DataList, Date, UserN):
         #print(Date)
         # Make calculation for last n days
         n = UserN
         RunningTotal = 0
         count = 1
         price = 0
         delta = timedelta(days=n)
         #print(Date-delta)
         for day in DataList:
             
             if day[0] < (Date-delta):
                 pass
                 
             elif day[0] < Date:
                count +=1
                price = day[1]
                RunningTotal = float(RunningTotal + float(price))
         sma = RunningTotal / count
         sma = round(sma, 2)
         #print(sma)
         return sma

    def CalculateEMA(DataList, StartDate, UserN, EMAyesterday):
        
        # Make calculation for last n days
        n = UserN
        alpha = 2 / (n+1)
        ema = 0
        for day in DataList:
            if day[0] == StartDate:
               ema = alpha*float(day[1]) + ((1-alpha)*EMAyesterday)
               break
            else:
                ema = EMAyesterday
        return ema

    def CalculateStrength(day, EMA, SMA):
        Strength = float(EMA) - float(SMA)
        return Strength

    def TrendRecognition(DataList, StartYear, StartMonth, StartDay, TimePeriod):
        smalist = []
        for i in range(TimePeriod):
            smalist.append(StrategyFunctionsForList.CalculateSMA(DataList, StartYear, StartMonth, StartDay + i, 3))
            print(smalist)
        for i in range(len(smalist)):
            if i != 0:
                # Identify if Stock sma increased or decreased a significant amount
                if smalist[i] > (smalist[i-1]*1.01):
                    print("UP!")
                elif smalist[i] < (smalist[i-1]*0.99):
                    print("DOWN!")
                else:
                    print("STEADY!")
    
    def Invest(Amount, Price, Wallet, Shares):
        Wallet = Wallet - Amount

        Shares = Shares + float(Amount/float(Price))
        return Wallet, Shares