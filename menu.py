
from calculadora import calEstandar, calCientifica
import os 

class Menu:
    def __init__(self,titulo="",opciones=[]):
         self.titulo=titulo
         self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("elija opcion [1...{}]:".format(len(self.opciones)))
        return opc       

opc=''
while opc != '5':   
    os.system("cls")     
    menu=Menu("***MENU PRINCIPAL***", ['1) Calculadora', '2) Operacion Numeros', '3) Tratamiento de Listas', '4) Operaciones de Cadenas ', '5) Salir'])
    opc=menu.menu()
    if opc =='1':
        opc1=''
        while opc1 != '10':
            os.system("cls")
            menu1=Menu("**MENU CALCULADORA**", ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) Valor Absoluto', '7) Circunferencia', '8) Area Circulo', '9) Area Cuadrado', '10) Salir'])
            opc1=menu1.menu()
            if opc1=='1':
                os.system("cls")
                print("Suma de dos numeros")
                n1=int(input("Ingrese n1: "))
                n2=int(input("Ingrese n2: "))
                calEst=calEstandar(n1,n2)
                suma=calEst.suma()
                print("{}+{}={}".format(n1,n2,suma))
                input ("presione una tecla para continuar...")
           
            elif opc1 == '2':  
                os.system("cls")
                print("Resta de dos numeros")
                n1=int(input("Ingrese n1: "))
                n2=int(input("Ingrese n2: "))
                calEst=calEstandar(n1,n2)
                resta=calEst.resta()
                print("{}-{}={}".format(n1,n2,resta))
                input ("presione una tecla para continuar...")
       
            elif opc1 == '3':  
                os.system("cls")
                print("Multiplicacion de dos numeros")
                n1=int(input("Ingrese n1: "))
                n2=int(input("Ingrese n2: "))
                calEst=calEstandar(n1,n2)
                multi=calEst.multiplicacion()
                print("{}*{}={}".format(n1,n2,multi))
                input ("presione una tecla para continuar...")

            elif opc1 == '4':  
                os.system("cls")
                print("Division de dos numeros")
                n1=int(input("Ingrese n1: "))
                n2=int(input("Ingrese n2: "))
                calEst=calEstandar(n1,n2)
                division=calEst.division()
                print("{}/{}={}".format(n1,n2,division))
                input ("presione una tecla para continuar...")
                  
            elif opc1 == '5':  
                os.system("cls")
                print("Exponente")
                n1=int(input("Ingrese n1: "))
                n2=int(input("Ingrese n2: "))
                calEst=calEstandar(n1,n2)
                expo=calEst.exponente()
                print("{}**{}={}".format(n1,n2,expo))
                input ("presione una tecla para continuar...")

            elif opc1 == '6':  
                os.system("cls")
                print("Valor Absoluto")
                calEst=calEstandar(0,0)
                num=int(input("Ingrese numero: "))
                valAb=calEst.valorAbsoluto(num)
                print("Valor absoluto de {}  es {}".format(num,valAb))
                input ("presione una tecla para continuar...")
                
            elif opc1 == '7':  
                os.system("cls")
                print("Circunferencia")
                calCient=calCientifica(0,0)
                radio=float(input("Ingrese radio de la circunferencia: "))
                cir=calCient.circunferencia(radio)
                print ("La circunferencia es: {}".format(cir))
                input ("presione una tecla para continuar...")

            elif opc1 == '8':  
                os.system("cls")
                print("Area del circulo")
                calCient=calCientifica(0,0)
                radio=float(input("Ingrese radio de la circunferencia: "))
                area=calCient.areaCirculo(radio)
                print ("El area del circulo es: {}".format(area))
                input ("presione una tecla para continuar...")

            elif opc1 == '9':  
                os.system("cls")
                print("Area del cuadrado")
                calCient=calCientifica(0,0)
                lado=float(input("Ingrese lado del cuadrado: "))
                areaC=calCient.areaCuadrado(lado)
                print ("El area del cuadrado es: {}".format(areaC))
                input ("presione una tecla para continuar...")

            elif opc1 == '10':  
                os.system("cls")   
            else:  
                print("Opcion no valida")

    elif opc=='2':
        opc2=''
        while opc2 != '11':
            os.system("cls") 
            menu2=Menu("**MENU OPERACION NUMEROS**", ['1) Presentar los numeros de 1 a n', '2) Sumar los numeros de 1 a n', 
            '3) Multiplo de cualquier numero', '4) Presentar los divisores de un numero', '5) Numero Primo', '6) Factorial de cualquier numero',
            '7) Fibonacci de una serie de n numeros', '8) Perfecto', '9) Primos Gemelos', '10) Numeros Amigos', '11) Salir'])
            opc2=menu2.menu()
            if opc2=='1':
                os.system("cls") 

    elif opc== '3':
        menu3=Menu("menu listas", ['1) perfecto', '2) primo', '3) salir'])

        opc3=menu3.menu()
    elif opc=='4':
        menu4=Menu("menu cadenas", ['1) perfecto', '2) primo', '3) salir'])
        opc4=menu4.menu()
    elif opc=='5':
        os.system("cls")
        print("****GRACIAS POR SU VISITA****")
    else:
        print("Opcion no valida")
        






