#Calculadora em python v1 menu
from Lab02_calculadora import *

class Menu():
    def __init__(self):
        self.msg = ""
        self.val1 = 0
        self.val2 = 0
        self.op = 0

    def invalida(self):
        self.msg = "Operação inválida!"
        return self.msg
    
    def setValores(self):
        self.val1 = int(input("Informe o 1º valor: "))
        self.val2 = int(input("Informe o 2º valor: "))
    
    def confirmacao(self):
        self.op = str(input("Deseja continuar? [s/n] ")).strip().lower()[0]
        if self.op in "sn":
            if self.op == "n":
                return True

    def main(self):
        while True:
            self.msg = """Escolha uma das operações:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair"""
            print(self.msg)
            self.op = int(input("1/2/3/4: "))
            if self.op == 1:
                print("--Soma--")
                self.setValores()
                s = Soma(self.val1, self.val2)
                print(f"{s}{s.resultado()}")
                if self.confirmacao():
                    break
            elif self.op == 2:
                print("--Subtração--")
                self.setValores()
                sub = Subtracao(self.val1, self.val2)
                print(f"{sub}{sub.resultado()}")
                if self.confirmacao():
                    break
            elif self.op == 3:
                print("--Multiplicação--")
                self.setValores()
                mul = Multiplicacao(self.val1, self.val2)
                print(f"{mul}{mul.resultado()}")
                if self.confirmacao():
                    break
            elif self.op == 4:
                print("--Divisão--")
                self.setValores()
                d = Divisao(self.val1, self.val2)
                print(f"{d}{d.resultado()}")
                if self.confirmacao():
                    break
            else:
                self.invalida()
                break
                

menu = Menu()
menu.main()