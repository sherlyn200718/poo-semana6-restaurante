"""
Punto de arranque del sistema restaurante_app de Delicias Andinas Sherlyn.

Crea instancias de Platillo y Bebida propias de un restaurante de comida típica andina, las
registra en el servicio Restaurante y muestra la información resultante
en consola, demostrando herencia, encapsulación y polimorfismo.
"""

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    """Función principal que ejecuta el flujo del programa."""

    # Creamos el servicio principal del restaurante
    restaurante = Restaurante("Delicias Andinas Sherlyn")

    # Creación de objetos Platillo (clase hija de Producto)
    platillo_uno = platillo_uno = Platillo(
        nombre="Locro de papa",
        precio=5.0,
        tiempo_preparacion_minutos=25,
        calorias=350
    )

    platillo_dos = platillo_dos = Platillo(
        nombre="Llapingachos con chorizo",
        precio=6.5,
        tiempo_preparacion_minutos=20,
        calorias=600
    )

    # Creación de objetos Bebida (clase hija de Producto)
    bebida_uno = bebida_uno = Bebida(
        nombre="Canelazo",
        precio=3.5,
        volumen_ml=250,
        es_alcoholica=True
    )

    bebida_dos = bebida_dos = Bebida(
        nombre="Jugo de mora",
        precio=2.0,
        volumen_ml=300,
        es_alcoholica=False
    )

    # Registramos los productos en el restaurante
    restaurante.agregar_producto(platillo_uno)
    restaurante.agregar_producto(platillo_dos)
    restaurante.agregar_producto(bebida_uno)
    restaurante.agregar_producto(bebida_dos)

    # Mostramos el menú completo (demostración de polimorfismo)
    restaurante.mostrar_menu()

    # Demostración de encapsulación: obtener_precio() y cambiar_precio()
    # controlan el acceso al atributo privado __precio
    print("\n--- Prueba de encapsulación sobre el precio ---")
    print(f"Precio actual de '{platillo_uno.nombre}': ${platillo_uno.obtener_precio():.2f}")

    platillo_uno.cambiar_precio(6.0)
    print(f"Nuevo precio de '{platillo_uno.nombre}': ${platillo_uno.obtener_precio():.2f}")

    # Intento de asignar un precio inválido (debe ser rechazado)
    platillo_uno.cambiar_precio(-5)


if __name__ == "__main__":
    main()
