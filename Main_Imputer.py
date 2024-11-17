from abc import ABC, abstractmethod
import statistics as s              #https://www.geeksforgeeks.org/python-statistics-mode-function/ Source for using this library.
'''This cell is exclusively used to define all the interfaces, the plan is to define an interface for:
   1. Imputer, where the Fit and Tranform classes are gonna be kept
   2. Calculation interface, where this class will serve as a template for Mean/Mode/Median
   3. Axis Strategy, so not having to worry about writing the code for column recognition.'''

class ImputerStrategy(ABC):         #Interface for the Imputer class
    @abstractmethod
    def fit(self):
        pass
    @abstractmethod
    def transform(self):
        pass

class CalculateStrategy(ABC):       #Interface for the Mean/Mode/Median class
    @abstractmethod
    def calculate(self):
        pass

class AxisStrategy(ABC):            #Interface for the Axis strategies
    @abstractmethod
    def select(self, data):
        pass
class Axis0(AxisStrategy):              #Axis0: Only corresponds to implementatiosn for Columns. NOT ROWS!!!!
    def __init__(self,data):
        self._data = data
    
    def select(self, column_index):
        return [row[column_index] for row in self._data if row[column_index] != "nan"]   #Only extracts the columns, if the value is not nan.

class Axis1(AxisStrategy):              #Axis1: Only corresponds to implentations for Rows. NOT NEEEDED !
    
    def select(self, data):
        pass                    #Not to be implemented
class Mean(CalculateStrategy):

    def calculate(self,data):
        return s.mean(data)        #Calculates the mean and returns the data

class Mode(CalculateStrategy):      

    def calculate(self,data):
        return s.mode(data)        #Calulcates the mode and returns the data

class Median(CalculateStrategy):

    def calculate(self,data):
        return s.median(data)      #Calcualtes the median and returns the data
class Imputer:
    def __init__(self,strategy:str="mean",axis:int=0):
        self._strategy = strategy
        self._axis = axis
        self._ImputeValues = None   #For storing the extracted data + applying one of the mean/mode/median calculations
        self._axis_strategy = None
    
    def fit(self, x, data):
        self._axis_strategy = Axis0(data) if self._axis == 0 else Axis1() #This will determine weather it's for column or rows Axis 0 = Column/Axis1 = Row
        column_data = self._axis_strategy.select(x)     

        #Strategy selection
        if self._strategy == "mean":
            calculator = Mean()
        elif self._strategy == "mode":
            calculator = Mode()
        elif self._strategy == "median":
            calculator = Median()
        else:
            raise ValueError ("Only accepts mean/mode/median")
        
        self._ImputeValues = calculator.calculate(column_data)

    
    def transform(self, column_index, data):
        for row in data:
            if row[column_index] == "nan":
                row[column_index] = self._ImputeValues

        return data