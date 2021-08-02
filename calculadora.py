import math
class calculadora:
    def __init__(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
   
    def suma(self):
        return self.num1+self.num2
   
    def resta(self):
        return self.num1-self.num2
   
    def multiplicacion(self):
        multi=self.num1*self.num2
        print ("{}*{}={}".format(self.num1,self.num2,multi))

    def division (self):
        return self.num1/self.num2
   

class calEstandar (calculadora):
    def __init__(self, numero1, numero2):
     super().__init__(numero1,numero2)

    def multiplicacion(self):
        return self.num1*self.num2
        
    def exponente(self):
        return self.num1**self.num2

    def valorAbsoluto(self, numero):
        if numero < 0:
            numero=numero*-1
            return numero
        else:
            numero=numero
            return numero

class calCientifica(calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)      

    def circunferencia(self, radio):
        pi=3.1416
        per=2*pi*radio
        return per

    def areaCirculo(self, radio):
        pi=3.1416
        area=pi*(radio**2)
        return area

    def areaCuadrado(self, lado):
        areaC=lado*lado
        return areaC 
        


#cal=calculadora(4,2)
#print(cal.division())
# print(cal.resta())           
#calEst=calEstandar(0,0)
#print(calEst.multiplicacion())
#print(calEst.exponente())
#print(calEst.valorAbsoluto(-6))
calCien=calCientifica(0,0)
#print(calCien.circunferencia(2))
#print(calCien.areaCirculo(3))
print(calCien.areaCuadrado(5))




