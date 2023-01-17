n=(input("ingrese el valor de n:"))
if not n.isnumeric():
    raise TypeError("ingrese un Número entero positivo")
n=int(n)
contador=0
#range es una función que va desde el 1 al n
for i in range(1,n+1):
    numero=i
    while numero != 1 and numero != 89:
        suma=0
        #este for que viene abajo separa en digitos, lo hace volviendo en un stream a numero y así usando un for in paso por todos sus digitos
        for digito in str(numero):
#           print("digito", digito)
            suma+=int(digito)**2
#            print("suma" , suma)
        numero=suma
    if numero==89:
        contador+=1
porcentaje=(contador/n)*100
print("el porcentaje de numeros de la cadena que llega al 89 es de:",porcentaje,"%")
