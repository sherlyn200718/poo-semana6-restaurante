"""
Módulo que define la clase Bebida, hija de Producto.

Representa una bebida disponible en Delicias Andinas Sherlyn, añadiendo
atributos propios que no aplican a un producto genérico ni a un platillo.
"""

from modelos.producto import Producto


class Bebida(Producto):
    """
    Clase hija que representa una bebida de Delicias Andinas Sherlyn.

    Hereda de Producto los atributos comunes (nombre, precio,
    disponibilidad) y agrega atributos específicos de la bebida:
    - volumen_ml (int): Volumen de la bebida, en mililitros.
    - es_alcoholica (bool): Indica si la bebida contiene alcohol.
    """

    def __init__(self, nombre, precio, volumen_ml, es_alcoholica, disponible=True):
        """
        Inicializa una bebida reutilizando el constructor de la clase
        padre mediante super() y añadiendo los atributos propios de la
        bebida.

        Args:
            nombre (str): Nombre de la bebida.
            precio (float): Precio de la bebida.
            volumen_ml (int): Volumen de la bebida, en mililitros.
            es_alcoholica (bool): Indica si la bebida contiene alcohol.
            disponible (bool): Disponibilidad de la bebida.
        """
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml
        self.es_alcoholica = es_alcoholica

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información
        específica de una bebida (demostración de polimorfismo).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        print(
            f"Bebida: {self.nombre} | Volumen: {self.volumen_ml} ml | Tipo: {'Alcohólica' if self.es_alcoholica else 'No alcohólica'} | "
            f"Precio: ${self.obtener_precio():.2f} | Estado: {estado}"
        )
