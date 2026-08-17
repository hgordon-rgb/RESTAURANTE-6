from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def registrar_producto(restaurante):

    try:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese código.")

    except ValueError:
        print("Precio inválido.")


def buscar_producto(restaurante):

    codigo = input("Ingrese código: ")

    producto = restaurante.buscar_producto(codigo)

    if producto:
        print(producto)
    else:
        print("Producto no encontrado.")


def actualizar_producto(restaurante):

    codigo = input("Código del producto: ")

    if restaurante.buscar_producto(codigo):

        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")

        try:
            precio = float(input("Nuevo precio: "))
        except ValueError:
            print("Precio inválido.")
            return

        restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        )

        print("Producto actualizado.")

    else:
        print("Producto no encontrado.")


def eliminar_producto(restaurante):

    codigo = input("Código del producto: ")

    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante):

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario(restaurante):

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado.")
    else:
        print("Ya existe un usuario con esa identificación.")


def listar_usuarios(restaurante):

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(restaurante):

    categorias = restaurante.obtener_categorias()

    if categorias:
        print("Categorías registradas:")
        for categoria in categorias:
            print("-", categoria)
    else:
        print("No existen categorías registradas.")


def main():

    restaurante = Restaurante()

    while True:

        print("\n================================")
        print("      SISTEMA DE RESTAURANTE")
        print("================================")
        print("1. Registrar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("-------------------------------")
        print("6. Registrar usuario")
        print("7. Listar usuarios")
        print("-------------------------------")
        print("8. Mostrar categorías")
        print("9. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            registrar_producto(restaurante)

        elif opcion == 2:
            buscar_producto(restaurante)

        elif opcion == 3:
            actualizar_producto(restaurante)

        elif opcion == 4:
            eliminar_producto(restaurante)

        elif opcion == 5:
            listar_productos(restaurante)

        elif opcion == 6:
            registrar_usuario(restaurante)

        elif opcion == 7:
            listar_usuarios(restaurante)

        elif opcion == 8:
            mostrar_categorias(restaurante)

        elif opcion == 9:
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()