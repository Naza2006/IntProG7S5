edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 11:
    print("Eres un niño")
elif edad > 11 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 65:
    print("Eres un adulto")
else:
    print("Eres un anciano") 