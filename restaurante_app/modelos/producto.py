class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )