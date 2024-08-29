#Una empresa de renta de transporte tiene varios tipos de vehículos a su
#disposición cada uno con sus características y coste de renta. La
#empresa periódicamente registra los nuevos vehículos que ingresan al
#lote para su posterior puesta en renta.
# Implementa la funcionalidad de rentar los vehículos disponibles
#tomando en cuenta los datos del cliente


class Vehiculo:
    def __init__(self, tipo, marca, modelo, año, coste):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.coste = coste
        self.disponible = True

    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo} ({self.año}) - ${self.coste}/dia - {'Disponible' if self.disponible else 'No disponible'}"


class Cliente:
    def __init__(self, nombre, identificacion, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.identificacion}, Tel: {self.telefono})"


class EmpresaRentaTransporte:
    def __init__(self):
        self.vehiculos = []
        self.alquileres = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos_disponibles(self):
        for idx, vehiculo in enumerate(self.vehiculos):
            if vehiculo.disponible:
                print(f"{idx + 1}. {vehiculo}")

    def rentar_vehiculo(self, cliente, indice_vehiculo):
        if 0 <= indice_vehiculo < len(self.vehiculos):
            vehiculo = self.vehiculos[indice_vehiculo]
            if vehiculo.disponible:
                vehiculo.disponible = False
                self.alquileres.append((cliente, vehiculo))
                print(f"{cliente.nombre} ha rentado el vehiculo: {vehiculo}")
            else:
                print("El vehiculo no esta disponible para renta.")
        else:
            print("Indice de vehiculo invalido.")


empresa = EmpresaRentaTransporte()

empresa.agregar_vehiculo(Vehiculo("Carro", "Toyota", "Corolla", 2020, 50))
empresa.agregar_vehiculo(Vehiculo("Moto", "Yamaha", "R3", 2021, 30))
empresa.agregar_vehiculo(Vehiculo("Camioneta", "Ford", "F-150", 2019, 80))

# Proceso de renta
def iniciar_renta():
    nombre = input("Ingrese el nombre del cliente: ")
    identificacion = input("Ingrese el numero de identificacion del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")

    cliente = Cliente(nombre, identificacion, telefono)

    print("\nVehiculos disponibles para renta:")
    empresa.mostrar_vehiculos_disponibles()

    try:
        indice_vehiculo = int(input("\nSeleccione el numero del vehiculo a rentar: ")) - 1
        empresa.rentar_vehiculo(cliente, indice_vehiculo)
    except ValueError:
        print("Entrada invalida. Por favor ingrese un numero.")

iniciar_renta()

# Este ejercicio de implementación para la empresa de renta de transporte
# aborda un problema práctico: gestionar vehículos disponibles para alquiler 
# y registrar los datos de los clientes que los rentan. 
# Cada clase tiene una responsabilidad clara: Vehiculo se ocupa de
# las características del vehículo, Cliente gestiona los datos del cliente y
# EmpresaRentaTransporte se encarga de coordinar las operaciones de la empresa.
# Esto hace que el código sea más fácil de entender y mantener..