from datetime import datetime #fechas
from random import randint #Random
from clases import MedicoVeterinario, Vendedor, DuenoMascota, Mascota, Ordenes, Facturas, Administrador #Clases
#from principal import *

#funcion para iniciar sesion
def iniciar_sesion(veterinaria,usuario,contrasena):
    rol = None
    # Verificar si la cédula y contraseña corresponden a un administrador
    if validar_administrador(veterinaria,usuario, contrasena):
        rol = "Administrador"
    # Verificar si la cédula y contraseña corresponden a un médico veterinario
    elif validar_veterinario(veterinaria,usuario, contrasena):
        rol = "MedicoVeterinario"
        # Verificar si la cédula y contraseña corresponden a un vendedor
    elif validar_vendedor(veterinaria,usuario, contrasena):
        rol = "Vendedor"
    return rol

    #funcion para validar administrador
def validar_administrador(veterinaria,usuario,contrasena):
    for administrador in veterinaria.lista_administradores:#recorriendo todos los admins
        if administrador.usuario == usuario and administrador.contrasena == contrasena: #comparo las credenciales
            return True
    return False
    
#funcion para validar medico veterinario
def validar_veterinario(veterinaria,usuario,contrasena):
    for medico_veterinario in veterinaria.lista_veterinarios:#recorriendo todos los veterinarios
        if medico_veterinario.usuario == usuario and medico_veterinario.contrasena == contrasena:#comparo las credenciales
            return True
    return False

#funcion para validar vendedor
def validar_vendedor(veterinaria,usuario, contrasena):
    for vendedor in veterinaria.lista_vendedores:#recorro todos los vendedores
        if vendedor.usuario == usuario and vendedor.contrasena == contrasena:#comparo las credenciales
            return True
    return False

def registrar_administrador(cedula,nombre,edad,usuario,contrasena,veterinaria): #creando administradores
    admon = Administrador(cedula,nombre,edad,usuario,contrasena)#Creando un objeto de cada clase
    veterinaria.lista_administradores.append(admon) #Añadir a la lista correspondiente de cada item

#funcion para registrar vendedor
def registrar_vendedor(cedula,nombre,edad,usuario,contrasena,veterinaria):
    vendedor=Vendedor(cedula,nombre,edad,usuario,contrasena) #Creando un objeto de cada clase
    veterinaria.lista_vendedores.append(vendedor) #Añadir a la lista correspondiente de cada item
    print("Vendedor registrado exitosamente.")

#funcion para registrar veterinario
def registrar_veterinario(cedula,nombre,edad,usuario,contrasena,veterinaria):
    veterinario=MedicoVeterinario(cedula,nombre,edad,usuario,contrasena)#Creando un objeto de cada clase
    veterinaria.lista_veterinarios.append(veterinario) #Añadir a la lista correspondiente de cada item
    print("Medico veterinario registrado exitosamente.")
    
#funcion para registrar dueño de mascota
def registrar_duenos(cedula,nombre,edad,veterinaria):
    dueno=DuenoMascota(cedula,nombre,edad)#Creando un objeto de cada clase
    veterinaria.lista_duenos.append(dueno) #Añadir a la lista correspondiente de cada item
    print("Dueño registrado exitosamente.")

def validar_dueno(cedula, veterinaria):
    for dueno in veterinaria.lista_duenos:
        if dueno.cedula == cedula:
            return True
    return False     

def regitrar_mascota(nombre, cedula, edad, especie, raza, caracteristicas, peso, veterinaria):
    mascota = Mascota(nombre, cedula, edad, especie, raza, caracteristicas, peso)#Creando un objeto de cada clase
    veterinaria.lista_mascotas.append(mascota) #Añadir a la lista correspondiente de cada item
    print("Mascota registrado exitosamente.")
 
def registrar_historia_clinica(informacion, veterinaria):
    veterinaria.historias_clinicas.append(informacion) #Añadir a la lista correspondiente de cada item
    print("historia clinica registrada exitosamente")

def registrar_orden(id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis, fecha_generacion, veterinaria):
    orden = Ordenes(id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis, fecha_generacion)#Creando un objeto de cada clase
    veterinaria.lista_ordenes.append(orden) #Añadir a la lista correspondiente de cada item
    print("orden registrada exitosamente")

def registrar_factura(id_mascota, id_dueno, id_orden, producto, valor, cantidad, fecha, veterinaria):
    factura = Facturas(randint(1000,9999), id_mascota, id_dueno, id_orden, producto, valor, cantidad, fecha)#Creando un objeto de cada clase
    veterinaria.lista_facturas.append(factura) #Añadir a la lista correspondiente de cada item
    print("factura registrada exitosamente")

def ver_ordenes(veterinaria): #imprimir informacion que envian desde principal
     for orden in veterinaria.lista_ordenes: #For es para recorrer
        print("Orden: "+str(orden.id_orden))
        print("Mascota: "+str(orden.id_mascota))
        print("Cédula dueño: "+str(orden.cedula_dueno))
        print("Cédula veterinario: "+str(orden.cedula_veterinario))
        print("Medicamento: "+orden.medicamento)
        print("Dosis: "+str(orden.dosis))
        print("Fecha generación: "+orden.fecha_generacion)
        print("=========================================")
        
def ver_facturas(veterinaria): #imprimir informacion que envian desde principal
    for factura in veterinaria.lista_facturas:
        print("Id Mascota: "+str(factura.id_mascota))
        print("Id Dueño: "+str(factura.id_dueno))
        print("Id Orden: "+str(factura.id_orden))
        print("Producto: "+factura.producto)
        print("Valor: "+str(factura.valor))
        print("Cantidad: "+str(factura.cantidad))
        print("Fecha generación: "+factura.fecha)
        print("=========================================")
        
def ver_historia_clinica(clinica): #imprimir informacion que envian desde principal
    print(f"Historia Nro: "+str(clinica.get("id")))
    print(f"Motivo consulta: "+clinica.get("motivo_consulta"))
    print(f"Sintomatologia: "+clinica.get("sintomatologia"))
    print(f"Diagnostico: "+clinica.get("diagnostico"))
    print(f"Procedimiento: "+clinica.get("procedimiento"))
    print(f"Medico: "+clinica.get("medico"))
    print(f"Anular Orden: "+clinica.get("anular_orden"))
    print(f"Fecha: "+str(clinica.get("fecha")))
    print("")
    print("")
    
def generar_diccionario(id_mascota, medico, motivo, sintomatologia, diagnostico, procedimiento, r_medicamento,
                        medicamento, dosis, id_orden, historial_vacunacion, historial_alergia, detalle_procedimiento, 
                        a_medicamento): #Crear el dicionario para las historias clinicas, que solicitan en principal
    return {
        "id" : id_mascota,
        "medico" : medico,
        "motivo_consulta" : motivo,
        "sintomatologia" : sintomatologia,
        "diagnostico" : diagnostico,
        "procedimiento" : procedimiento,
        "medicamento" : ("Ninguno", medicamento)[r_medicamento == 1],
        "dosis" : ("Ninguna", dosis)[r_medicamento == 1], #Condiciones parecidas a ternarios, profe en otros lenguajes hay en python, no [si es (falso, verdaero)]
        "id_orden" : ("N/A", id_orden)[r_medicamento == 1],
        "historial_vacunacion": ("N/A", historial_vacunacion)[procedimiento.lower == 'vacunacion'],
        "historial_alergia": ("N/A", historial_alergia)[a_medicamento == 1],
        "detalle_procedimiento" : detalle_procedimiento,
        "fecha" : datetime.now().isoformat, #para generar fecha y transformalas mas bonitas
        "anular_orden" : "No"
    }
