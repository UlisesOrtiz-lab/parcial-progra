'''Un hotel de playa cuenta con un recepcionista que se encarga de 
presentar a los clientes las opciones de habitaciones disponibles junto 
con sus precios. Tras la elección de la habitación, el recepcionista 
solicita los datos personales del cliente y el número de noches que 
permanecerá en el hotel. Finalmente, entrega al cliente una factura 
detallada con el total de los gastos.
 Adicionalmente, los clientes pueden solicitar servicios extra, 
como el uso de la piscina o la cancha de golf, que tienen un costo 
adicional. Implementa esta funcionalidad en tu programa
'''



'''se nos pide un sistema que permita gestionar reservas en un hotel, incluyendo l
a selección de habitaciones, solicitud de datos personales, 
cálculo del total de gastos, y la opción de añadir servicios extra.'''
'''se nos pide: registrar paciente, precio de habitaciones, numero de noches que 
que se va hospedar ademas de una factiura de los gasto de hotel ademas si desea 
incluir algun servicio adicional'''



def mostrar_opciones_habitaciones():
    habitaciones = {
        '1': {'nombre': 'Habitación Individual', 'precio_noche': 50},
        '2': {'nombre': 'Habitación Doble', 'precio_noche': 75},
        '3': {'nombre': 'Suite Familiar', 'precio_noche': 120}
    }
    
    print("\nOpciones de Habitaciones:")
    for clave, valor in habitaciones.items():
        print(f"{clave}. {valor['nombre']} - ${valor['precio_noche']} por noche")
    
    return habitaciones

def mostrar_servicios_extra():
    servicios = {
        '1': {'nombre': 'Uso de la Piscina', 'precio': 20},
        '2': {'nombre': 'Uso de la Cancha de Golf', 'precio': 30}
    }
    
    print("\nServicios Extras:")
    for clave, valor in servicios.items():
        print(f"{clave}. {valor['nombre']} - ${valor['precio']}")
    
    return servicios

def calcular_total(precio_habitacion, noches, servicios_extra):
    total = precio_habitacion * noches
    for servicio in servicios_extra:
        total += servicio['precio']
    return total

def generar_factura(nombre_cliente, habitacion, noches, servicios_extra):
    print("\nFactura Detallada")
    print(f"Cliente: {nombre_cliente}")
    print(f"Habitación: {habitacion['nombre']}")
    print(f"Número de noches: {noches}")
    print(f"\nServicios Extras:")
    
    for servicio in servicios_extra:
        print(f"- {servicio['nombre']} - ${servicio['precio']}")
    
    total = calcular_total(habitacion['precio_noche'], noches, servicios_extra)
    print(f"\nTotal a pagar: ${total}")

def sistema_reservas():
    habitaciones = mostrar_opciones_habitaciones()
    servicios = mostrar_servicios_extra()
    
    while True:
        try:
            eleccion_habitacion = input("\nSeleccione el número de la habitación deseada: ").strip()
            if eleccion_habitacion not in habitaciones:
                print("Opción inválida. Intente de nuevo.")
                continue
            habitacion = habitaciones[eleccion_habitacion]
            
            nombre_cliente = input("Ingrese su nombre completo: ").strip()
            noches = int(input("Ingrese el número de noches que permanecerá: ").strip())
            
            servicios_extra = []
            while True:
                eleccion_servicio = input("\nSeleccione el número del servicio extra deseado (o presione Enter para continuar): ").strip()
                if eleccion_servicio == "":
                    break
                if eleccion_servicio not in servicios:
                    print("Opción inválida. Intente de nuevo.")
                    continue
                servicios_extra.append(servicios[eleccion_servicio])
            
            generar_factura(nombre_cliente, habitacion, noches, servicios_extra)
            
            salir = input("\n¿Desea realizar otra reserva? (s/n): ").strip().lower()
            if salir != 's':
                print("Gracias por su visita. ¡Regrese pronto!")
                break
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")


if _name_ == "_main_":
    sistema_reservas()