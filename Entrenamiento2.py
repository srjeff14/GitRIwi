while(True):
    try:
        option = int(input("""Elija una opción:
1.Determinar el estado de aprobación de una nota
2.Calcular el promedio de notas
3.Contar califiaciones mayores
4.Verificar y contar calificaiones específicas
5.Salir\n"""))
    except ValueError:
        print("Digite una opción valida")
        print("")
        continue
    if(option == 1):
        while(True):
            try:
                nota = int(input("Digite la nota: (0/100):\n"))
                if (nota > 0 and nota >= 60 and nota <= 100):
                    print("Usted gano la nota")
                    break
                elif(nota >= 0 and nota < 60):
                    print("Usted perdio la nota")
                    break
                else:
                    print("Digite un valor valido") 
            except ValueError:
                print("Digite un valor valido")
                continue
    elif (option == 2):
        notas = []
        while(True):
            try:
                cant = int(input("Digite la cantidad de notas: "))
                acum = 0
                if(cant > 0): 
                    for i in range(1,cant+1):
                        while(True):
                            try:
                                while(True):
                                    nota = int(input(f"Digite la nota número {i}: "))                                
                                    if (nota < 0):
                                        print("Digite un valor valido")
                                    else:
                                        break
                                notas.insert(i,nota)
                                acum += nota 
                            except ValueError:
                                print("Digite un valor correcto")
                                continue
                            break
                    prom = acum / cant
                    print(f"El promedio de las notas fue: {prom}")
                    break
                else:
                    print("Digite un valor valido")
            except ValueError:
                print("Digite un valor valido")
                continue
        
    elif (option == 3):
        notas = []
        cont = 0
        while(True):
            try:
                while(True):
                        cant = int(input("Digite la cantidad de notas: "))
                        if(cant > 0):
                            breCicle = 0
                            if (cant >= 1):
                                for i in range(1,cant+1):
                                    while(True):
                                        try:
                                            nota = int(input(f"Digite la nota número {i}: "))
                                            breCicle += 1
                                            if (nota >= 0 and nota <= 100):
                                                notas.insert(i,nota)
                                                if (nota >= 60 and nota < 101):
                                                    cont += 1
                                                    break
                                                elif(nota < 0):
                                                    print("Digite un valor valido")
                                                break
                                            elif(breCicle == cant):
                                                break
                                            else: 
                                                print("DIgite un valor valido")
                                        except ValueError:
                                            print("Digite un valor correcto")
                                            continue
                            else:
                                print("Digite un valor valido")
                            break
                        else:
                            print("Digite un valor valido")
            except ValueError:
                print("Digite un valor valido")
                continue
            break
        print(f"La cantidad de notas aprobadas fueron: {cont}")
        comas = ", ".join(map(str, notas))
        print(f"Las notas fueron: {comas}")
        
    elif (option == 4):
        notas = []
        while(True):
            try:
                cant = int(input("Digite la cantidad de notas: "))
                acum = 0
                breCicle = 0
                if(cant > 0): 
                    for i in range(1,cant+1):
                        while(True):
                            try:
                                nota = int(input(f"Digite la nota número {i}: "))
                                if (nota <= 100 and nota >= 0):
                                    notas.insert(i,nota)
                                    acum += nota 
                                    breCicle += 1
                                    break
                                elif(nota <= 0):
                                    print("Igrese un valor valido")
                                elif (breCicle == cant):
                                    break
                            except ValueError:
                                print("Digite un valor correcto")
                                continue
                    prom = acum / cant
                    print(f"El promedio de las notas fue: {prom}")
                    comas = ", ".join(map(str, notas))
                    print(f"Las notas fueron: {comas}")
                    break
                else:
                    print("Digite un valor valido")
            except ValueError:
                print("Digite un valor valido")
                continue
            
    elif(option < 1 or option > 5):
        print("Digite una opción valida")
        
    elif (option == 5):
        break
    
    

    
        
        
        
        
        
        
        
        

            
        
        
    
        