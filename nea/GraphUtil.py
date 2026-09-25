from ast import main
from datetime import timedelta
from sys import maxsize
import math

class GraphCalculations():
    @staticmethod
    def NormalisePriceList(List):
        #normalise list
        #find max
        Max = -1
        for Price in List:

            if Price > Max:
                Max = Price
        #min is 0 so its constant and the lines are comparable
        Min = 0

        #transform list to values between 0 and 1
        count = 0
        for Price in List:
            priceNew = (Price-Min)/(Max-Min)
            List[count] = priceNew
            count+=1
        return List

    def NormalisePriceListWithMaxList(List, MaxList):
        #normalise list
        #find max
        Max = -1
        for Price in MaxList:

            if Price > Max:
                Max = Price
            
        
        #min is 0 so its constant and the lines are comparable
        Min = 0

        #transform list to values between 0 and 1
        count = 0
        for Price in List:
            priceNew = (Price-Min)/(Max-Min)
            List[count] = priceNew
            count+=1
        return List

    def DateCalcs(Datalist):
        #find time delta
        delta = Datalist[-2][0] - Datalist[0][0]
        scalingfunction = 850 / delta.days
        return scalingfunction
    
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