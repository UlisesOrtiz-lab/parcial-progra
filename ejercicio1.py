"""Un consultorio médico atiende a una serie de pacientes, solo está una 
secretaria y en el consultorio hay varios doctores cada paciente llega y 
deja sus datos además del motivo de su consulta y posteriormente la 
secretaria les asigna la fecha de su consulta.
 En el caso que una persona ya tenga una consulta previa en lugar 
de tomar datos se le pasará a sala de esperas. Implementa esta 
problemática a tu código."""

# consultorio.py

class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.cita_asignada = None

class Consultorio:
    def __init__(self):
        self.pacientes = {}  
        
    def registrar_paciente(self, nombre, motivo_consulta):
        if nombre in self.pacientes:
            print(f"El paciente {nombre} ya tiene una consulta previa. Se le pasa a sala de espera.")
            return
        paciente = Paciente(nombre, motivo_consulta)
        self.pacientes[nombre] = paciente
        print(f"Paciente {nombre} registrado exitosamente.")

    def asignar_cita(self, nombre, fecha_cita):
        if nombre not in self.pacientes:
            print(f"Paciente {nombre} no está registrado.")
            return
        paciente = self.pacientes[nombre]
        paciente.cita_asignada = fecha_cita
        print(f"Cita asignada para el paciente {nombre} en la fecha {fecha_cita}.")

    def mostrar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return
        for nombre, paciente in self.pacientes.items():
            estado_cita = paciente.cita_asignada if paciente.cita_asignada else "Sin cita asignada"
            print(f"Paciente: {nombre}, Motivo de consulta: {paciente.motivo_consulta}, Cita: {estado_cita}")

def main():
    consultorio = Consultorio()

    while True:
        print("\nConsultorio Médico")
        print("1. Registrar Paciente")
        print("2. Asignar Cita")
        print("3. Mostrar Pacientes")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            nombre = input(" nombre del paciente: ")
            motivo_consulta = input(" motivo de la consulta: ")
            consultorio.registrar_paciente(nombre, motivo_consulta)
            
        elif opcion == '2':
            nombre = input("nombre del paciente: ")
            fecha_cita = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
            consultorio.asignar_cita(nombre, fecha_cita)
            
        elif opcion == '3':
            consultorio.mostrar_pacientes()
            
        elif opcion == '4':
            print("Que se recupere pronto...")
            break
        else:
            print("Opción inválida. seleccionar una de las opciones presentadas.")

if __name__ == "__main__":
    main()