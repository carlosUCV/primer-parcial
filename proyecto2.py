H=(input("ingresa la profundidad del pozo en metros:"))
Ld=(input("ingresa la distancia que el caracol asciende durante el dia en metros:"))
Ln=(input("ingrese la cantidad que el caracol desciende mientras duerme en metros:"))
Distancia_Recorrida=0
Dias=0
if not H.isnumeric() or not Ld.isnumeric() or not Ln.isnumeric() :
   raise TypeError("Ingrese un número entero y positivo")
H=int(H)
Ld=int(Ld)
Ln=int(Ln)
if Ld>Ln:
    while Distancia_Recorrida < H:
        Distancia_Recorrida+=Ld-Ln
        Dias+=1
    if Distancia_Recorrida>=H:
        if Dias==1:
            print("el caracol dura un día en salir")
        else:
            print("Al ", Dias,"día el caracol puede dormir tranquilo sin despertar en el pozo")
            print("El caracol sale exactamente en", H/(Ld-Ln), "días")
else:
    print("el caracol no sale del pozo")