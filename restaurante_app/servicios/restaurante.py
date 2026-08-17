from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:

    def __init__(self):

        # LISTAS
        self.productos = []
        self.usuarios = []

        # TUPLA
        self.opciones_menu = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar usuario",
            "Listar usuarios",
            "Mostrar categorías",
            "Salir"
        )

        # DICCIONARIO
        self.menu_funciones = {
            1: "Registrar producto",
            2: "Buscar producto",
            3: "Actualizar producto",
            4: "Eliminar producto",
            5: "Listar productos",
            6: "Registrar usuario",
            7: "Listar usuarios",
            8: "Mostrar categorías",
            9: "Salir"
        }

    def registrar_producto(self, producto: Producto):

        if self.buscar_producto(producto.codigo):
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str):

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(self, codigo, nombre, categoria, precio):

        producto = self.buscar_producto(codigo)

        if producto:
            producto.nombre = nombre
            producto.categoria = categoria
            producto.precio = precio
            return True

        return False

    def eliminar_producto(self, codigo):

        producto = self.buscar_producto(codigo)

        if producto:
            self.productos.remove(producto)
            return True

        return False

    def listar_productos(self):

        return self.productos

    def registrar_usuario(self, usuario: Usuario):

        for u in self.usuarios:
            if u.identificacion == usuario.identificacion:
                return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self):

        return self.usuarios

    def obtener_categorias(self):

        # CONJUNTO
        categorias = {producto.categoria for producto in self.productos}
        return categorias