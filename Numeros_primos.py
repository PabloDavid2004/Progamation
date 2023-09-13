numerosprimos=[]
numero = int(input("Introduzca un número: "))

cont=0

for i in range(2, numero+1):
    for j in range(2, int(i/2)+1):
        if i%j==0:
            cont+=1
    if cont==0:
        numerosprimos.append(i)
    cont=0

print("Los números primos son: ", numerosprimos)
