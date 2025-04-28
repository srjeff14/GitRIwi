

Continuar = input("¿Desea ingresar al menú principal? s/n: ")
if (Continuar == "S" or "s"):
    while(Continuar == "s" or "S"):
        
        opcion = input ("""Ingrese la opción que desee\n
                        *** Menú de bienvenida ***\n
                        1. Ingresar usuario\n
                        2. Cambio de moneda\n
                        (Recuerde ingresar el número de la opción) """)
        if (opcion == "1"):
            
            nombre = input("Digite su nombre: ")
            segundoNombre = input("Ingrese su segundo nombre o apellido: ")
            apellido = input("Ingrese el apenllido: ")
            nombreMayus = nombre[0].upper()
            nombre1 = nombreMayus + nombre[1:]
            segundoNombrem = segundoNombre[0].upper()
            segundoNombre1 = segundoNombrem + segundoNombre[1:]
            apellidoMayus = apellido[0].upper()
            apellido1 = apellidoMayus + apellido[1:]
            nombreCompleto = nombre1 + " " + segundoNombre1 + " " + apellido1 
            print (nombreCompleto)
            
        elif (opcion == "2"):
            
            valorEnpesoc = input("Ingrese el valor en pesos: ")
            valorEnpesos = float(valorEnpesoc)
            precioDolarc = input("Ingrese el valor del dolar: ")
            precioDolar = float(precioDolarc)
            valorTotal = valorEnpesos / precioDolar
            print(f"El valor en dolares es de: {valorTotal}")
        
        Continuar = input ("¿Desea continuar en el menú? s/n ")
                
                


