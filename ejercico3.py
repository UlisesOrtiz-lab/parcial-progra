def mostrar_opciones_habitaciones():
    habitaciones = {
        1: {'nombre': 'Habitación Estándar', 'precio_noche': 50},
        2: {'nombre': 'Habitación Deluxe', 'precio_noche': 75},
        3: {'nombre': 'Suite Presidencial', 'precio_noche': 150}
    }
    
    print("Opciones de habitaciones disponibles:")
    for clave, valor in habitaciones.items():
        print(f"{clave}. {valor['nombre']} - ${valor['precio_noche']} por noche")
    
    return habitaciones

def solicitar_datos_cliente():
    nombre = input("Introduce tu nombre: ")
    telefono = input("Introduce tu número de teléfono: ")
    correo = input("Introduce tu correo electrónico: ")
    noches = int(input("¿Cuántas noches te quedarás? "))
    return nombre, telefono, correo, noches

def solicitar_servicios_extra():
    print("\nServicios extra disponibles:")
    print("1. Uso de la piscina - $20 por noche")
    print("2. Acceso a la cancha de golf - $50 por noche")
    
    servicios = {
        1: 20,
        2: 50
    }
    
    servicio_seleccionado = input("Selecciona el número del servicio extra deseado (separado por comas si eliges más de uno): ")
    servicios_elegidos = list(map(int, servicio_seleccionado.split(',')))
    
    costo_extra = sum(servicios[servicio] for servicio in servicios_elegidos if servicio in servicios)
    return costo_extra

def main():
    habitaciones = mostrar_opciones_habitaciones()
    
    eleccion = int(input("\nElige el número de la habitación deseada: "))
    if eleccion not in habitaciones:
        print("Opción inválida. Terminando el programa.")
        return
    
    habitacion = habitaciones[eleccion]
    nombre, telefono, correo, noches = solicitar_datos_cliente()
    
    costo_habitacion = habitacion['precio_noche'] * noches
    costo_extra = solicitar_servicios_extra()
    total = costo_habitacion + costo_extra
    
    print("\nFactura detallada:")
    print(f"Nombre: {nombre}")
    print(f"Teléfono: {telefono}")
    print(f"Correo electrónico: {correo}")
    print(f"Tipo de habitación: {habitacion['nombre']}")
    print(f"Número de noches: {noches}")
    print(f"Precio por noche: ${habitacion['precio_noche']}")
    print(f"Costo de la habitación: ${costo_habitacion}")
    print(f"Costo de servicios extra: ${costo_extra}")
    print(f"Total a pagar: ${total}")

if __name__ == "__main__":
    main()

