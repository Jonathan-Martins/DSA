#Calculadora em python v1 classes de calculo    
    
class Soma():
    def __init__(self, *num):
        self.operadores = num
    
    def resultado(self):
        resul = 0
        for i in self.operadores:
            resul += i
        return resul

    def __str__(self):
        return f"{self.operadores[0]} + {self.operadores[1]} = "
    
class Subtracao():
    def __init__(self, *num):
        self.operadores = num
    
    def resultado(self):
        resul = self.operadores[0] - self.operadores[1]
        return resul
    
    def __str__(self):
        return f"{self.operadores[0]} - {self.operadores[1]} = "
    
class Multiplicacao():
    def __init__(self, *num):
        self.operadores = num        

    def resultado(self):
        resul = 1
        for i in self.operadores:
            resul *= i
        return resul

    def __str__(self):
        return f"{self.operadores[0]} x {self.operadores[1]} = "

class Divisao():
    def __init__(self, *num):
        self.operadores = num
    
    def resultado(self):
        resul = self.operadores[0] / self.operadores[1]
        return resul
    
    def __str__(self):
        return f"{self.operadores[0]} / {self.operadores[1]} = "

