rango_inicial = int(input("Escribe el inicio del rango: "))
rango_final = int(input("Escribe le fin del rango: "))

if(rango_inicial < rango_final):
    numero = int(input("Dime un numero: "))
    if(numero >= rango_inicial and numero <= rango_final):
        print("El nuemro esta dentro del rango.")
    else:
    print("El numero no esta dentro el rango.")
    
