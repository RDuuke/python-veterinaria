from clases import MedicoVeterinario, Vendedor, DuenoMascota, Mascota, Ordenes
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
    for administrador in veterinaria.lista_administradores:
        if administrador.usuario == usuario and administrador.contrasena == contrasena:
            return True
    return False
    
#funcion para validar medico veterinario
def validar_veterinario(veterinaria,usuario,contrasena):
    for medico_veterinario in veterinaria.lista_veterinarios:
        if medico_veterinario.usuario == usuario and medico_veterinario.contrasena == contrasena:
            return True
    return False

#funcion para validar vendedor
def validar_vendedor(veterinaria,usuario, contrasena):
    for vendedor in veterinaria.lista_vendedores:
        if vendedor.usuario == usuario and vendedor.contrasena == contrasena:
            return True
    return False

#funcion para registrar vendedor
def registrar_vendedor(cedula,nombre,edad,usuario,contrasena,veterinaria):
    vendedor=Vendedor(cedula,nombre,edad,usuario,contrasena)
    veterinaria.lista_vendedores.append(vendedor)
    print("Vendedor registrado exitosamente.")

#funcion para registrar veterinario
def registrar_veterinario(cedula,nombre,edad,usuario,contrasena,veterinaria):
    veterinario=MedicoVeterinario(cedula,nombre,edad,usuario,contrasena)
    veterinaria.lista_veterinarios.append(veterinario)
    print("Medico veterinario registrado exitosamente.")
    
#funcion para registrar dueño de mascota
def registrar_duenos(cedula,nombre,edad,veterinaria):
    dueno=DuenoMascota(cedula,nombre,edad)
    veterinaria.lista_duenos.append(dueno)
    print("Dueño registrado exitosamente.")
    return dueno

def validar_dueno(cedula, veterinaria):
    for dueno in veterinaria.lista_duenos:
        if dueno.cedula == cedula:
            return True
    return False     

def regitrar_mascota(nombre, cedula, edad, especie, raza, caracteristicas, peso, veterinaria):
    mascota = Mascota(nombre, cedula, edad, especie, raza, caracteristicas, peso)
    veterinaria.lista_mascotas.append(mascota)
    print("Mascota registrado exitosamente.")
    return mascota
 
def registrar_historia_clinica(informacion, veterinaria):
    veterinaria.historias_clinicas.append(informacion)
    print("historia clinica registrada exitosamente")

def registrar_orden(id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis, fecha_generacion, veterinaria):
    orden = Ordenes(id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis, fecha_generacion)
    veterinaria.lista_ordenes.append(orden)
    print("orden registrada exitosamente")
    