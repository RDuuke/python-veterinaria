from clases import Veterinaria, Mascota, DuenoMascota
from metodos import iniciar_sesion, registrar_veterinario, registrar_vendedor, registrar_duenos, validar_dueno, regitrar_mascota, registrar_historia_clinica, registrar_orden
from os import system #Obteniendo metodo system para usar en sistema OS
from random import randint
from datetime import datetime


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
    # print("2.Registrar veterinario")
    # print("3.Registrar vendedor")
    print("0.Salir")

    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        usuario = input("Ingrese su usuario: ")
        contrasena = int(input("Ingrese su contraeña: "))
        rol = iniciar_sesion(veterinaria, usuario, contrasena)
        
        if rol == "Administrador" : 
            system("cls") #limpiando consola
            while True:
                print("1.Registrar veterinario")
                print("2.Registrar vendedor")
                print("3.Salir")
                opcion = int(input("Seleccione una opcion: "))
                system("cls") #limpiando consola
                if opcion == 1:
                    cedula = int(input("Ingrese la cedula: "))
                    nombre = input("Ingrese nombre: ")
                    edad = int(input("Ingrese edad: "))
                    usuario = input("Ingrese un usuario: ")
                    contrasena = input("Ingrese contraseña: ")
                    registrar_veterinario(cedula,nombre,edad,usuario,contrasena, veterinaria)
                    
                elif opcion == 2:
                    cedula = int(input("Ingrese la cedula: "))
                    nombre = input("Ingrese nombre: ")
                    edad = int(input("Ingrese edad: "))
                    usuario = input("Ingrese un usuario: ")
                    contrasena = input("Ingrese contraseña: ")
                    registrar_vendedor(cedula,nombre,edad,usuario,contrasena, veterinaria)
                else:
                    system("cls") #limpiando consola
                    break
                
        elif rol == "MedicoVeterinario":
            while True:
                system("cls") #limpiando consola
                print("1.Registrar Dueño")
                print("2.Registrar Mascota")
                print("3.Registrar Historia Clinica")
                print("4.Consultar Historia Clinica")
                print("0.Salir")
                opcion = int(input("Seleccione una opcion: "))
                system("cls") #limpiando consola
                if opcion == 1:
                    
                    cedula = int(input("Ingrese la cedula: "))
                    nombre = input("Ingrese nombre: ")
                    edad = int(input("Ingrese edad: "))
                    dueno = registrar_duenos(cedula, nombre, edad, veterinaria)
                    
                elif opcion == 2:
                    cedula = int(input("Ingrese la cedula del dueño: "))
                    if validar_dueno(cedula, veterinaria) is False:
                        print("No existe la cédula: "+str(cedula))
                        break
                    
                    nombre = input("Ingrese nombre de la mascota: ")
                    edad = int(input("Ingrese la edad de la mascota: "))
                    especie = input("Ingrese la especie de la mascota: ")
                    raza = input("Ingrese la raza de la mascota: ")
                    peso = int(input("Ingrese la peso de la mascota: "))
                    color = input("Ingrese la color de la mascota: ")
                    tamano = input("Ingrese la tamaño la mascota: ")
                    
                    caracteristicas = {
                        "color" : color,
                        "tamaño" : tamano
                    }
                    
                    mascota = regitrar_mascota(nombre, cedula, edad, especie, raza, caracteristicas, peso, veterinaria)
                elif opcion == 3:
                    print("Lista de mascotas:")
                    for mascota in veterinaria.lista_mascotas:
                        print(f"Id: {mascota.id} - Nombre: {mascota.nombre} - C Dueño: {mascota.cedula_dueno}")
                    id_mascota = int(input("Id Mascota:")) 
                    historial_vacunacion = []
                    historial_alergia = []
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
                    fecha = datetime.now().isoformat
                    informacion = {
                        "id" : id_mascota,
                        "medico" : medico,
                        "motivo_consulta" : motivo,
                        "sintomatologia" : sintomatologia,
                        "diagnostico" : diagnostico,
                        "procedimiento" : procedimiento,
                        "medicamento" : ("Ninguno", medicamento)[r_medicamento == 1],
                        "dosis" : ("Ninguna", dosis)[r_medicamento == 1],
                        "id_orden" : ("N/A", id_orden)[r_medicamento == 1],
                        "historial_vacunacion": ("N/A", historial_vacunacion)[procedimiento.lower == 'vacunacion'],
                        "historial_alergia": ("N/A", historial_alergia)[a_medicamento == 1],
                        "detalle_procedimiento" : detalle_procedimiento,
                        "fecha" : fecha,
                        "anular_orden" : "No"
                        
                    }
                    registrar_historia_clinica(informacion, veterinaria)
                    if r_medicamento == 1 :
                        cedula_d = int(input("Cédula dueño: "))
                        cedula_m = int(input("Cédula medico: "))
                        registrar_orden(id_orden, id_mascota, cedula_d, cedula_m, medicamento, dosis, fecha, veterinaria)
                elif opcion == 4:
                    clinica: dict= {}
                    id_clinca = int(input("Ingresa el Id de la mascota: "))
                    for h_clinica in veterinaria.historias_clinicas:
                        if h_clinica.get("id") == id_clinca:
                            clinica = h_clinica
                            break
                    
                    if len(clinica) == 0:
                        print("No hay Historia Clinica")
                    print(f"Historia Nro: "+str(clinica.get("id")))
                    print(f"Motivo consulta: "+clinica.get("motivo_consulta"))
                    print(f"Sintomatologia: "+clinica.get("sintomatologia"))
                    print(f"Diagnostico: "+clinica.get("diagnostico"))
                    print(f"Procedimiento: "+clinica.get("procedimiento"))
                    print(f"Medico: "+clinica.get("medico"))
                    print(f"Anular Orden: "+clinica.get("anular_orden"))
                    print(f"Fecha: "+clinica.get("fecha"))
                    print("")
                    print("")
                    print("1:Editar Historial")
                    print("2:Anular orden")
                    opcion = int(input("Selecciona una opción: "))
                    if opcion == 1:
                        print("Editar")
                    elif opcion == 2:
                        index = veterinaria.historias_clinicas.remove(clinica)
                        clinica.update({
                            "anular_orden" : "Si"
                        })
                        veterinaria.historias_clinicas.append(clinica)
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
                print("0.Salir")
                opcion = int(input("Seleccione una opcion: "))
                if opcion == 1:
                    for orden in veterinaria.lista_ordenes:
                        print("Orden: "+str(orden.id_orden))
                        print("Mascota: "+str(orden.id_mascota))
                        print("Cédula dueño: "+str(orden.cedula_dueno))
                        print("Cédula veterinario: "+str(orden.cedula_veterinario))
                        print("Medicamento: "+orden.medicamento)
                        print("Dosis: "+str(orden.dosis))
                        print("Fecha generación: "+orden.fecha_generacion)
                        print("=========================================")
                    
                    id= int(input("Ingrese id de la orden"))
                if opcion == 2:
                    break
    
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")