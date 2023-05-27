import time
from clases import Veterinaria
from metodos import iniciar_sesion, registrar_veterinario, registrar_vendedor, registrar_duenos, validar_dueno, regitrar_mascota, registrar_historia_clinica, registrar_orden, registrar_factura, ver_ordenes, ver_historia_clinica, generar_diccionario, registrar_administrador, ver_facturas
from os import system #Obteniendo metodo system para usar en sistema OS
from random import randint
from datetime import datetime

## Cargando información por defecto - > la clase veterinaria tiene todos estos metodos: ubicacion: clases.pý
veterinaria = Veterinaria()
veterinaria.registrar_administrador()
veterinaria.registrar_veterinario()
veterinaria.registrar_vendedor()
veterinaria.registrar_dueno()
veterinaria.registrar_mascota()
veterinaria.registrar_historia_clinica()
veterinaria.registrar_orden()

while True:
    print("\n----- MENU PRINCIPAL -----")
    print("1.Iniciar sesión")
    print("0.Salir")

    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        usuario = input("Ingrese su usuario: ")
        contrasena = int(input("Ingrese su contraseña: "))
        rol = iniciar_sesion(veterinaria, usuario, contrasena) #Valida las credenciales y entrega el rol -> metodos
        
        if rol == "Administrador" : 
            system("cls") #limpiando consola
            while True:
                print("1.Registrar veterinario")
                print("2.Registrar vendedor")
                print("3.Registrar administrador")
                print("0.Salir")
                opcion = int(input("Seleccione una opcion: "))
                system("cls") #limpiando consola
                if opcion == 0:
                    system("cls") #limpiando consola
                    break
                
                #cuanto hay un int antes del input, es que estoy transformando de st4ring a entero
                cedula = int(input("Ingrese la cédula: ")) 
                nombre = input("Ingrese nombre: ")
                edad = int(input("Ingrese edad: "))
                usuario = input("Ingrese un usuario: ")
                contrasena = int(input("Ingrese contraseña: "))
                
                #cuando hablamos de registrar, quiere decir que ingresamos informacions a las lista de c/u
                if opcion == 1:
                    registrar_veterinario(cedula,nombre,edad,usuario,contrasena, veterinaria)
                if opcion == 2:
                    registrar_vendedor(cedula,nombre,edad,usuario,contrasena, veterinaria)
                if opcion == 3:
                    registrar_administrador(cedula,nombre,edad,usuario,contrasena, veterinaria)
  
                time.sleep(0.5)
                    
        elif rol == "MedicoVeterinario":
            while True:
                system("cls") #limpiando consola
                print("1.Registrar Dueño")
                print("2.Registrar Mascota")
                print("3.Registrar Historia Clinica")
                print("4.Consultar Historia Clinica")
                print("5.Ver ordenes")
                print("0.Salir")
                opcion = int(input("Seleccione una opcion: "))
                system("cls") #limpiando consola
                if opcion == 1:
                    
                    cedula = int(input("Ingrese la cedula: "))
                    nombre = input("Ingrese nombre: ")
                    edad = int(input("Ingrese edad: "))
                    registrar_duenos(cedula, nombre, edad, veterinaria)
                    
                elif opcion == 2:
                    cedula = int(input("Ingrese la cedula del dueño: "))
                    #Preguntamos si hay una cedula, para crear una mascota
                    if validar_dueno(cedula, veterinaria) is False:
                        print("No existe la cédula: "+str(cedula))
                        time.sleep(0.5) #Pausa el proceso .5 segundos (para que se puea ver los mensajes)
                        break
                    
                    nombre = input("Ingrese nombre de la mascota: ")
                    edad = int(input("Ingrese la edad de la mascota: "))
                    especie = input("Ingrese la especie de la mascota: ")
                    raza = input("Ingrese la raza de la mascota: ")
                    peso = int(input("Ingrese la peso de la mascota: "))
                    color = input("Ingrese la color de la mascota: ")
                    tamano = input("Ingrese la tamaño la mascota: ")
                    #Se crea un diccionario de carasteristicas = {"key" : value} => diccionario
                    caracteristicas = {
                        "color" : color,
                        "tamaño" : tamano
                    }
                    
                    regitrar_mascota(nombre, cedula, edad, especie, raza, caracteristicas, peso, veterinaria)
                    time.sleep(0.5) #Pausa el proceso .5 segundos (para que se puea ver los mensajes) / retrasa el programa
                elif opcion == 3:
                    print("Lista de mascotas:")
                    for mascota in veterinaria.lista_mascotas: #siempre queveamos un for es para recorrer algo!
                        print(f"Id: {mascota.id} - Nombre: {mascota.nombre} - C Dueño: {mascota.cedula_dueno}")
                    id_mascota = int(input("Id Mascota:")) 
                    historial_vacunacion = [] #Creamos listas , las listas se inician []
                    historial_alergia = [] #Creamos listas , las listas se inician []
                    medico = input("Nombre de doctor: ")
                    motivo = input("Motivo de consulta: ")
                    sintomatologia = input("Sintomatologia: ")
                    diagnostico = input("Diagnostico: ")
                    procedimiento = input("Procedimiento: ")
                    r_medicamento = int(input("Medicamento: 1:Si / 0:No: "))
                    if r_medicamento == 1 :
                        medicamento = input("Ingrese el medicamento: ")
                        dosis = input("Ingrese la dosis del medicamento: ")
                        id_orden = randint(1000,9999)
                    if procedimiento.lower == 'vacunación' or procedimiento.lower == 'vacunacion':
                        historial_vacunacion.append({
                            "vacuna" : medicamento
                        })
                    a_medicamento = int(input("Alergia: 1:Si / 0:No: "))
                    if a_medicamento == 1:
                        alergia = input("Ingrese la alergia: ")
                        historial_alergia.append({
                            'medicamento': alergia
                        })
                    detalle_procedimiento = input("Detalle Procedimiento: ")
                    
                    #Profe, como el archivo estaba tan extenso, preferi crear un metodo, que me creara el diccionario - < metodos.py
                    informacion = generar_diccionario(id_mascota, medico, motivo, sintomatologia, diagnostico, procedimiento, r_medicamento,
                                                      medicamento, dosis, id_orden, historial_vacunacion, historial_alergia, detalle_procedimiento, a_medicamento)
                    registrar_historia_clinica(informacion, veterinaria)
                    if r_medicamento == 1 :
                        cedula_d = int(input("Cédula dueño: "))
                        cedula_m = int(input("Cédula medico: "))
                        #según el ejercicio si hay medicamento, hay 1 orden
                        registrar_orden(id_orden, id_mascota, cedula_d, cedula_m, medicamento, dosis, informacion.get('fecha'), veterinaria) #para obtener la fecha del diccionario 
                    time.sleep(0.5)
                elif opcion == 4:
                    clinica: dict = {}
                    id_clinica = int(input("Ingresa el Id de la mascota: "))
                    for h_clinica in veterinaria.historias_clinicas: #For igual recorrer algo
                        if h_clinica.get("id") == id_clinica: #evaluando que si hay una historia clinica con el id de la mascota
                            clinica = h_clinica #guardo variable
                            break #salir del for
                    if not clinica: #si no encontro entonces digo que no hay nada y ya!
                        print("No hay Historia Clinica")
                    else :
                        ver_historia_clinica(clinica) #Mostrar la historia clinica; profe el archivo estaba muy largo e hice un metodo
                        print("1:Editar Historial")
                        print("2:Anular orden")
                        print("0:Salir")
                        opcion = int(input("Selecciona una opción: "))
                        if opcion == 1:
                            id_mascota = id_clinica
                            historial_vacunacion = [] #Creamos listas , las listas se inician []
                            historial_alergia = [] #Creamos listas , las listas se inician []
                            medico = input("Nombre de doctor: ")
                            motivo = input("Motivo de consulta: ")
                            sintomatologia = input("Sintomatologia: ")
                            diagnostico = input("Diagnostico: ")
                            procedimiento = input("Procedimiento: ")
                            r_medicamento = int(input("Medicamento: 1:Si / 0:No: "))
                            if r_medicamento == 1 :
                                medicamento = input("Ingrese el medicamento: ")
                                dosis = input("Ingrese la dosis del medicamento: ")
                                id_orden = randint(1000,9999)
                            if procedimiento.lower == 'vacunación' or procedimiento.lower == 'vacunacion':
                                historial_vacunacion.append({
                                    "vacuna" : medicamento
                                })
                            a_medicamento = int(input("Alergia: 1:Si / 0:No: "))
                            if a_medicamento == 1:
                                alergia = input("Ingrese la alergia: ")
                                historial_alergia.append({
                                    'medicamento': alergia
                                })
                            detalle_procedimiento = input("Detalle Procedimiento: ")
                            
                            #Profe, como el archivo estaba tan extenso, preferi crear un metodo, que me creara el diccionario - < metodos.py
                            informacion = generar_diccionario(id_mascota, medico, motivo, sintomatologia, diagnostico, procedimiento, r_medicamento,
                                                            medicamento, dosis, id_orden, historial_vacunacion, historial_alergia, detalle_procedimiento, a_medicamento)
                            veterinaria.historias_clinicas.remove(clinica)
                            clinica.update(informacion)
                            veterinaria.historias_clinicas.append(clinica) #volvemos agregar
                            
                        elif opcion == 2:
                            veterinaria.historias_clinicas.remove(clinica) #removemos el antiguo item
                            clinica.update({
                                "anular_orden" : "Si"
                            }) #actualizamos
                            veterinaria.historias_clinicas.append(clinica) #volvemos agregar
                            time.sleep(0.5) 
                elif opcion == 5:
                    ver_ordenes(veterinaria)#Mostrar ordenes; profe el archivo estaba muy largo e hice un metodo
                    time.sleep(1.5)
                else:
                    system("cls") #limpiando consola
                    break
        
    # colocar si rol es igual a Vendedor
    # imprimit menu para venedor [ver ordenes, generar factura]
    # if y elif para ver ordenes y ver facturas

        elif rol == "Vendedor":  
            while True:
                system("cls") #limpiando consola
                print("1.Ver ordenes")
                print("2.Vender producto")
                print("3.listar facturas")
                print("0.Salir")
                opcion = int(input("Seleccione una opcion: "))
                if opcion == 1:
                    ver_ordenes(veterinaria)#Mostrar ordenes; profe el archivo estaba muy largo e hice un metodo
                    time.sleep(1.5)
                if opcion == 2:
                    id_mascota = int(input("Id Mascota: "))
                    id_dueno = int(input("Id Dueño: "))
                    opcion = int(input("Es una venta de una orden: 1:Sí / 0: No: "))
                    if opcion == 1:
                        id_orden = int(input("Id Orden: "))
                    producto = input("Ingrese el producto: ") 
                    id_orden = ("N/A", id_orden)[opcion == 1]#(false, true)[condicion]
                    valor = int(input("Valor de producto: "))
                    cantidad = int(input("Cantidad: "))
                    fecha = datetime.now().isoformat
                    factura = registrar_factura(id_mascota, id_dueno, id_orden, producto, valor, cantidad, fecha, veterinaria)
                    time.sleep(0.5)
                if opcion == 3:
                    ver_facturas(veterinaria)#Mostrar facturas; profe el archivo estaba muy largo e hice un metodo
                    time.sleep(1.5)    
    
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")