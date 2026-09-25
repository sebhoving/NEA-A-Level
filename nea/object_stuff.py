class Program:
    def __init__(self) -> None:
        self.stock_data = StockData(self, "file.csv")
        self.simulation = Simulation(self)


class StockData:
    def __init__(self, the_program, source_file) -> None:
        self.the_program = the_program


class Simulation:
    def __init__(self, the_program) -> None:
        self.the_program = the_program
        self.the_program.stock_data
        self.__ActiveStrategies: list[IStrategy]

    def some_method(self):
        for Strat in self.__ActiveStrategies:
            Strat.Run();


# parent class
class IStrategy:
    def __init__(self) -> None:
        pass

    def Run(self):
        raise Exception("NotImplementedException")


class DCA(IStrategy):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def Run(self):
        print("Implement this behaviour")

class Graph:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    theProgram = Program()