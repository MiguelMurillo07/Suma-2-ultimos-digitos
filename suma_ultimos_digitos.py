# Caso No. 6: Dado un número entero determinar si la suma de sus 2 últimos dígitos es un número de 1 solo dígito.


print("----------------------------------")
print("------Suma Últimos 2 Dígitos------")
print("----------------------------------")

# input

z = int(input("Digite un valor entero: "))

#processing

k1=z%10
k2=((z%100)-k1)//10
s = k1+k2

#output

if s>=10:
    print("La suma de los 2 últimos dígitos es más de un dígito.")
    print("La suma total es: " + str(s))
else:
    print("La suma de sus 2 últimos dígitos es un sólo dígito.")
    print("La suma total es: " + str(s))