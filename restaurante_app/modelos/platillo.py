"""
Módulo que define la clase Platillo, hija de Producto.

Representa una comida o plato preparado que se ofrece en
Delicias Andinas Sherlyn, añadiendo atributos propios que no aplican a un
producto genérico ni a una bebida.
"""

from modelos.producto import Producto


class Platillo(Producto):
    """
    Clase hija que representa un platillo de Delicias Andinas Sherlyn.

    Hereda de Producto los atributos comunes (nombre, precio,
    disponibilidad) y agrega atributos específicos del platillo:
    - tiempo_preparacion_minutos (int): Tiempo estimado de preparación, en minutos.
    - calorias (int): Cantidad aproximada de calorías del platillo.
    """

    def __init__(self, nombre, precio, tiempo_preparacion_minutos, calorias, disponible=True):
        """
        Inicializa un platillo reutilizando el constructor de la clase
        padre mediante super() y añadiendo los atributos propios del
        platillo.

        Args:
            nombre (str): Nombre del platillo.
            precio (float): Precio del platillo.
            tiempo_preparacion_minutos (int): Tiempo estimado de preparación, en minutos.
            calorias (int): Cantidad aproximada de calorías del platillo.
            disponible (bool): Disponibilidad del platillo.
        """
        super().__init__(nombre, precio, disponible)
        self.tiempo_preparacion_minutos = tiempo_preparacion_minutos
        self.calorias = calorias

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información
        específica de un platillo (demostración de polimorfismo).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(
            f"Platillo: {self.nombre} | Tiempo de preparación: {self.tiempo_preparacion_minutos} min | Calorías: {self.calorias} kcal | "
            f"Precio: ${self.obtener_precio():.2f} | Estado: {estado}"
        )
