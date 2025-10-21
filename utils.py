"""
This class is a calculator that performs arithmatic oparation on two numbers.

complete methods below and add missing methods according to the tests.

"""
class Calculator():
    """rounding_digits is a default value by which 
    the calculator rounds off numbers 10/3 = 3.3333333333...
    if rounding_digits = 2 the answer for this expression is 3.33  
    """
    rounding_digits = 0
    
    def __init__(self,round_digits):
        self.rounding_digits = round_digits
        
    def addtion(self,a,b):
        return 0
    def subtraction(self,a,b):
        return 0
    def multiplication(self,a,b):
        return 0
    def division(self,a,b):
        return 0
    
    @property
    def round_digits(self):
        return self.rounding_digits
    
    def set_ound_digits(self,digits):
        self.rounding_digits = digits
        
    
class History():
    filepath_ = ""
    def __init__(self, filepath):
        self.filepath_ = filepath
        
    def save(self,expression:str):
        pass
    def restore(self)->list[str]:
        pass
    def clear(self):
        pass