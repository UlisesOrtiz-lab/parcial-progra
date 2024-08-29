"""Un consultorio médico atiende a una serie de pacientes, solo está una 
secretaria y en el consultorio hay varios doctores cada paciente llega y 
deja sus datos además del motivo de su consulta y posteriormente la 
secretaria les asigna la fecha de su consulta.
 En el caso que una persona ya tenga una consulta previa en lugar 
de tomar datos se le pasará a sala de esperas. Implementa esta 
problemática a tu código."""

''''''
from datetime import datetime

# Base de datos simulada
pacientes = {}  # Diccionario para almacenar pacientes con citas
sala_espera = []  # Lista para pacientes en sala de espera

# Función para registrar un nuevo paciente
def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").strip()
    motivo = input("Ingrese el motivo de la consulta: ").strip()
    
    if nombre in pacientes:
        print(f"El paciente {nombre} ya tiene una cita previa. Será enviado a sala de espera.")
        if nombre not in sala_espera:
            sala_espera.append(nombre)
    else:
        fecha_consulta = input("Ingrese la fecha de consulta (en formato YYYY-MM-DD): ").strip()
        try:
            fecha = datetime.strptime(fecha_consulta, '%Y-%m-%d')
            pacientes[nombre] = {'motivo': motivo, 'fecha_consulta': fecha}
            print(f"Paciente {nombre} registrado con éxito. Cita asignada para el {fecha_consulta}.")
        except ValueError:
            print("Formato de fecha inválido. Por favor use el formato YYYY-MM-DD.")

# Función para mostrar los pacientes en sala de espera
def mostrar_sala_espera():
    if sala_espera:
        print("\nPacientes en sala de espera:")
        for paciente in sala_espera:
            print(f"- {paciente}")
    else:
        print("No hay pacientes en sala de espera.")

# Función principal del sistema
def sistema_consultorio():
    while True:
        print("\nSistema de Gestión de Consultorio Médico")
        print("1. Registrar nuevo paciente")
        print("2. Mostrar sala de espera")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ").strip()
        
        if opcion == '1':
            registrar_paciente()
        elif opcion == '2':
            mostrar_sala_espera()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor elija 1, 2 o 3.")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_consultorio()
