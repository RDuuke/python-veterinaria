from datetime import datetime
from random import randint

class Veterinaria:
    def __init__(self):
        self.lista_administradores = []
        self.lista_veterinarios =[]
        self.lista_vendedores = []
        self.lista_duenos = []
        self.lista_mascotas = []
        self.historias_clinicas = []
        self.lista_ordenes = []
        self.lista_facturas = []

        self.registrar_administrador()

    def registrar_administrador(self):
        admon = Administrador(123456, "Administrador", 30, "admin", 123)
        self.lista_administradores.append(admon)

    def registrar_veterinario(self):
        medico = MedicoVeterinario(123456, "Veterinario", 30, "medico", 123)
        self.lista_veterinarios.append(medico)
    
    def registrar_vendedor(self):
        medico = Vendedor(123456, "Vendedor", 30, "vendedor", 123)
        self.lista_vendedores.append(medico)

    def registrar_dueno(self):
        dueno = DuenoMascota(987, "Lily", 27)
        self.lista_duenos.append(dueno)
    
    def registrar_mascota(self):
        mascota = Mascota("Pedro", 987, 7, "Perro", "Pastor Aleman", "Visco", 28)
        self.lista_mascotas.append(mascota)

    def registrar_historia_clinica(self):
        informacion = {
            "id" : 6356,
            "medico" : "Juan",
            "motivo_consulta" : "dolor",
            "sintomatologia" : "fiebre",
            "diagnostico" : "diagnostico",
            "procedimiento" : "procedimiento",
            "medicamento" : "acetaminofen",
            "dosis" : 4,
            "id_orden" : 99999,
            "historial_vacunacion": "vacunas",
            "historial_alergia": "alergia",
            "detalle_procedimiento" : "vacunas",
            "fecha" : datetime.now().isoformat(),
            "anular_orden" : "No"
        }
        self.historias_clinicas.append(informacion)

    def registrar_orden(self):
        orden = Ordenes(99999, 987, 987, 1234, "acetaminofen", 4, datetime.now().isoformat())
        self.lista_ordenes.append(orden)
        

class Persona:
    def __init__(self, cedula, nombre, edad, rol):
        self.cedula =cedula
        self.nombre = nombre
        self.edad = edad
        self.rol = rol

class Administrador(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, 'Administrador')
        self.usuario = usuario
        self.contrasena = contrasena
        


class MedicoVeterinario(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, 'MedicoVeterinario')
        self.usuario = usuario
        self.contrasena = contrasena
        

class Vendedor(Persona):
    def __init__(self, cedula, nombre, edad, usuario, contrasena):
        super().__init__(cedula, nombre, edad, 'Vendedor')
        self.usuario = usuario
        self.contrasena = contrasena
        

class DuenoMascota(Persona):
    def __init__(self, cedula, nombre, edad,):
        super().__init__(cedula, nombre, edad, 'DuenoMascota')

class Mascota:
    def __init__(self, nom_mascota, cedula_dueno, edad_mascota, especie, raza, caracteristicas, peso):
        self.id = randint(1000,9999)
        self.nombre = nom_mascota
        self.cedula_dueno = cedula_dueno
        self.edad = edad_mascota
        self.especie = especie
        self.raza = raza
        self.caracteristicas = caracteristicas
        self.peso = peso
        self.creado = datetime.now().isoformat()

class Ordenes:
    def __init__(self, id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis, fecha_generacion ):
        self.id_orden = id_orden
        self.id_mascota = id_mascota
        self.cedula_dueno = cedula_dueno
        self.cedula_veterinario = cedula_veterinario
        self.medicamento = medicamento
        self.dosis = dosis
        self.fecha_generacion = fecha_generacion

class Facturas:
    def __init__(self, id_factura, id_mascota, cedula_dueño, id_orden, producto, valor, cantidad, fecha ):
        self.id_factura = id_factura
        self.id_mascota = id_mascota
        self.cedula_dueño = cedula_dueño
        self.id_orden = id_orden
        self.producto = producto
        self.valor = valor
        self.cantidad = cantidad
        self.fecha = fecha