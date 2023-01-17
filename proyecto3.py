n=input("Ingrese el número de filas N:")
m=(input("Ingrese el número de columnas M:"))
fila=[]
columna=[]
matriz=[]
K=0
invertidor=1
nivelador=1
if not n.isnumeric() or not m.isnumeric():
    raise TypeError("ingrese números enteros positivos por fa")

n=int(n)
m=int(m)
matriz=[]

#crear la matriz
for i in range(n):
    fila=[]
    for j in range(m):
        fila.append(0)
    matriz.append(fila)

#proximos dos ciclos for son para recorrer cada elemento de la matriz
for h in range(n):
    for d in range(m):

#este if es para aumentar la fila para luego restarle ya que no supe como voltearla
# es decir no supe usar el ".reversed"
        if K ==m*invertidor:
            K=(m+K)+1
            invertidor+=2

#este if es para compensar el k ya que le reste "m" tantos
        if K ==(m*nivelador)+1:
            K=K+m-1
            nivelador+=2

#cuando h es impar resto
        if h%2!=0:
            K-=1

#cuando h es par sumo
        if h%2==0:
            K+=1

        matriz[h][d]=K

print(matriz)