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
        breCicle = 0
        while(True):
            try:
                valor = int(input("Digite el valor especifico: "))
                if(valor > 0):
                    while(True):
                        try:
                            cant = int(input("Digite la cantidad de notas: "))
                            if(cant > 0):
                                if (cant >= 1):
                                        while(breCicle < cant):
                                            try:
                                                nota = int(input(f"Digite la nota número {breCicle+1}: "))
                                                if (nota > 0 and nota <= 100):
                                                    notas.insert(breCicle,nota)
                                                    breCicle += 1
                                                    if (nota > valor):
                                                        cont += 1
                                                        break
                                                    elif(nota < 0):
                                                        print("Digite un valor valido")
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
                        if (breCicle == cant):
                            break
                    print(f"La cantidad de notas aprobadas fueron: {cont}")
                    comas = ", ".join(map(str, notas))
                    print(f"Las notas fueron: {comas}")
                    break
                else:
                    print("Digite un valor valido")
            except ValueError:
                print("Digite un valor valido")
                continue
        
        
    elif (option == 4):
        while(True):
            try:
                cant = int(input("Digite la cantidad de notas: "))
                if cant > 0:
                    notas = input(f"Digite las {cant} notas separadas por coma: ").split(",")
                    if len(notas) != cant:
                        print(f"Debe ingresar exactamente {cant} notas.")
                        continue

                    notaInt = []
                    rep = {}
                    for i in notas:
                        try:
                            numero = int(i.strip())
                            if 0 <= numero <= 100:
                                notaInt.append(numero)
                                if numero in rep:
                                    rep[numero] += 1
                                else:
                                    rep[numero] = 1
                            else:
                                print(f"Error: '{numero}' no está en el rango válido (0-100) y será omitido.")
                        except ValueError:
                            print(f"Error: '{i.strip()}' no es un valor numérico válido y será omitido.")

                    if len(notaInt) == 0:
                        print("No se ingresaron notas válidas.")
                        continue

                    prom = sum(notaInt) / len(notaInt)
                    print(f"El promedio fue: {prom}")
                    print(f"Las notas válidas fueron: {notaInt}")
                    repetidas = {k: v for k, v in rep.items() if v > 1}
                    if repetidas:
                        print(f"Las notas que se repiten son: {repetidas}")
                    else:
                        print("No hay notas repetidas.")
                    break
                else:
                    print("Digite un valor válido.")
            except ValueError:
                print("Digite un valor válido.")
                continue
            
            
            
            
            
            
            
    elif(option < 1 or option > 5):
        print("Digite una opción valida")
        
    elif (option == 5):
        break
    
    

    
        
        
        
        
        
        
        
        

            
        
        
    
        