intentos=0
a=0
NumeroDelCentroA=0
b=0
NumeroDelCentroB=0
c=0
numeroDelCentroC=0


while intentos <3:
    n=(input("ingrese el valos de N:"))
    if not n.isnumeric() :
        raise TypeError("Ingrese un número entero positivo")
    n=int(n)    
   #La función LEN indica la cantidad de caracteres
    if len(str(n))>=4:
        a=n*n
        NumeroDelCentroA=str(a)[2:6]
        print("numero A al cuadrado:", a)
        print("número aleatorio de A:", a*10**(-2*int(len(str(n)))))
        print("numero del centro A:", NumeroDelCentroA)
        b=int(NumeroDelCentroA)*int(NumeroDelCentroA)
        NumeroDelCentroB=str(b)[2:6]
        print("numero B al cuadrado:", b)
        print("número aleatorio de B:", b*10**(-2*int(len(str(n)))))
        print("numero del centro de B", NumeroDelCentroB)
        c=int(NumeroDelCentroB)*int(NumeroDelCentroB)
        numeroDelCentroC=str(c)[2:6]
        print("numero C al cuadrado:", c)
        print("número aleatorio de C:", c*10**(-2*int(len(str(n)))))
        print("numero del centro de C", numeroDelCentroC)
    else:
        print("el numero debe tener al menos 4 digitos")
        intentos += 1
if intentos==3:
    print("se han agotado los intentos")