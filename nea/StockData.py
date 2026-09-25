import csv, datetime


class StockData:
    def __init__(self, the_program, source_file) -> None:
        self.the_program = the_program
        self.DataList = self.CreateDataList(source_file)
        self.TimePeriod = len(self.DataList)-1
        self.DataFrequency = 1

    def AlterTimePeriod(self, NewPeriod):
        NewPeriod = int(NewPeriod)
        if NewPeriod < (len(self.DataList)//252) and NewPeriod >= 1:
            self.TimePeriod = NewPeriod * 252
        if self.the_program.DEBUG:
            print(f"{self.TimePeriod} should = {NewPeriod*252}")

        # Clear and re-add current strategy objects
        self.the_program.simulation.ClearStrategies()
        self.the_program.ui.restart()
        

    def AlterDataFrequency(self, NewFrequency):
        NewFrequency = int(NewFrequency)
        if NewFrequency < 32 and NewFrequency >= 1 and NewFrequency < (self.TimePeriod//15):
            self.DataFrequency = NewFrequency
        if self.the_program.DEBUG:
            print(f"{self.DataFrequency} should = {NewFrequency}")

        # Clear and re-add current strategy objects
        self.the_program.simulation.ClearStrategies()
        self.the_program.ui.restart()

    def LoadDataFile(self, path):
        with open(path, "r") as f:
            content = csv.reader(f, delimiter=',')
            f.close()
            return content


    def CreateDataList(self, path):
         with open(path, "r") as f:
            Content = csv.reader(f, delimiter=',')
            Datalist = []
            Datelist = []
            Openlist = []
            Highlist = []
            Lowlist = []
            Closelist = []
            a=0

            for row in Content:
                if a != 0:
                    if path == "Download Data - DJIA.csv":
                        Datelist.append(datetime.date(int(row[0][6:10]), int(row[0][0:2]), int(row[0][3:5])))
                    else:
                        Datelist.append(datetime.date(int(row[0][6:10]), int(row[0][3:5]), int(row[0][0:2])))
                    Openlist.append(row[1])
                    Highlist.append(row[2])
                    Lowlist.append(row[3])
                    Closelist.append(row[4])
                
                a = 1
            Length = len(Datelist) - 1
            for i in range(len(Datelist)):
                Datalist.append([Datelist[Length-i], Openlist[Length-i] , Highlist[Length-i] , Lowlist[Length-i] , Closelist[Length-i]])
            if path != "Download Data - DJIA.csv":
                Datalist = self.ReverseDataList(Datalist)
            f.close()
            return Datalist

    def ReverseDataList(self, list):
        newlist = []
        for day in list:
            newlist.insert(0,day)
        return newlist

class DataPoint:
    # constructor
    # automatically called when an object is instantiated
    def __init__(self):
        self.__Timestamp = ""
        self.__Open = -1
        self.__High = -1
        self.__Low = -1
        self.__Close = -1

