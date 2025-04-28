Ciclo = True
while (Ciclo):
    Ciclo2 = True
    try:
        edad = int(input("Ingrese la edad: "))
    except ValueError:
        print("Debe ser un número entero")
        continue
    if (edad < 0):
        print("Digite la edad valida")  
        Ciclo2 = False  
    elif (edad < 12):
        print("Eres un niño")
    elif(edad < 18):
        print("Eres un adolecente")
    elif(edad < 60):
        print("Eres un adulto")
    elif(edad >= 60):
        print("Eres un adulto mayor")
    while (Ciclo2):
        print("¿Desea ingresar otra edad? ")
        try:   
            option = int(input("(Digite el número de la opcion)\n1.si\n2.no\n"))
            if (option == 1): 
                Ciclo2 = False
            elif (option == 2):
                Ciclo = False
                Ciclo2 = False
            elif (option != 1 or option != 2): 
                print("Ingrese un valor valido (Digite el número de la opcion)\n1.si\n2.no\n")
        except ValueError:
            print("Ingrese un valor valido s/n: ")
            continue
        