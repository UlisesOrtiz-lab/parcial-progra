#Una biblioteca ofrece préstamos de libros a través de una tarjeta
#impresa que contiene los datos de la persona que realiza el préstamo. El
#sistema de préstamos registra la fecha en que se retira el libro y la fecha
#límite para su devolución. Realiza un programa que solvente esto de
#una manera más eficaz.


from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, dias_prestamo=14):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_prestamo + timedelta(days=dias_prestamo)
        self.fecha_devolucion = None

    def devolver_libro(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion
        if self.fecha_devolucion > self.fecha_limite:
            dias_de_retraso = (self.fecha_devolucion - self.fecha_limite).days
            sancion = dias_de_retraso * 1  
            print(f"El libro '{self.libro.titulo}' fue devuelto tarde por {dias_de_retraso} dias.")
            print(f"Sancion aplicada: {sancion} unidades monetarias.")
        else:
            print(f"El libro '{self.libro.titulo}' fue devuelto a tiempo. No hay sancion.")

usuario = Usuario("Ulises")
libro = Libro("programacion avanzada")

fecha_prestamo = datetime.now()
prestamo = Prestamo(usuario, libro, fecha_prestamo)

fecha_devolucion = fecha_prestamo + timedelta(days=16) 
prestamo.devolver_libro(fecha_devolucion)
