"""
Aplicacion en python para gestionar envío de productos comprados desde tiendas online.
Usar una base de datos SQlite para guardar la información de los productos, usuarios y viajes.
se compran el producto por el propio usuario  o por un personal shopper, para esto hay que agregarlo a la aplicacion
y ser aprobado por el administrador para luego ser agregado por el cliente al viaje actual para su entrega y esto se revisa nuevamente por el administrador.
solo se pueden agregar productos aprobados al viaje actual, y el producto se marca como pendiente_peso.

Los clientes_vip son los usuarios de confianza que no tienen que pagar subscripcion y tienen un precio por libra especial por ser los mas antiguos o especiales.
Luego de que llega el producto a la bodega y se pesa se le incluye esta info al viaje.
Se crean 3 clases Producto, Usuario y Viaje.
    Producto tiene atributos nombre, id_producto, detalles, tipo, Personal_shopper, peso y destino, id_cliente.
    Usuario tiene atributos nombre, id_usuario, telefono, categoria, correo_electronico, y direccion.
    Viaje tiene atributos id_viaje,id_usuario, id_producto, fecha, detalles, ingresos, gastos, ganancias, cambio_USDLMP.
Van a existir varios tipos de usuarios: administrador, colaborador, delivery, cliente_regular, cliente_miembro, cliente_vip, cada uno con diferentes permisos.
Cada usuario cliente tiene sus propios productos que no pueden ver los de otros usuarios.

Los colaboradores son otras empresas de envio que permiten enviar nuestros productos con ellos,
pero no pueden ver los productos de otros clientes, solo los que tengan asignados a ellos.

Los administradores pueden ver todos los productos y asignar colaboradores a los clientes.

Los 3 tipos de clientes (regular, miembro, vip) tienen diferentes niveles de acceso y beneficios.
podran ver su situacion financiera, pero no la de otros clientes.
Los clientes_miembros y clientes_vip pueden acceder a su historial y agregar productos de viajes anteriores a su viaje actual,
pero los clientes_regulares solo pueden agregar productos nuevos del viaje actual y sus precios son diferentes, los clientes_vip tienen un precio por libra especial.


Los delivery solo pueden ver los productos aprobados para su entrega y actualizar el estado de entrega de los productos.
Los delivery y colaboradores no podran ver los productos pendientes o rechazados ni acceso a la información financiera.


Cada usuario tendra un nombre de usuario y contraseña para acceder a su informacion y podra agregar productos.
Estos productos se guardaran en la base de datos con el id del usuario para relacionarlos con el estado pendiente hasta que seam aprobados por el administrador.
Una vez que se haya aprobado la compra del producto el usuario podra proceder a agregarlo al viaje y se marcara el producto como pendiente_peso,

Una vez que el administrador revise los productos pendientes, podra cambiar su estado aprobado, el usuario puede agregarlo al viaje.

//////////////////////
Author: Alexi Gonzalez
by GlezDelivery.com
"""

import sqlite3
from datetime import datetime
import os

DB_NAME = "envios.db"

# ==========================
# DB INIT
# ==========================


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Usuarios
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        username TEXT UNIQUE,
        password TEXT,
        telefono TEXT,
        categoria TEXT,
        correo TEXT,
        direccion TEXT,
        aprobado INTEGER DEFAULT 0
    )
    """
    )

    # Productos
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        detalles TEXT,
        tipo TEXT,
        personal_shopper TEXT,
        peso REAL,
        destino TEXT,
        id_cliente INTEGER,
        estado TEXT DEFAULT 'pendiente',
        FOREIGN KEY(id_cliente) REFERENCES usuarios(id_usuario)
    )
    """
    )

    # Viajes
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS viajes (
        id_viaje INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        fecha TEXT,
        detalles TEXT,
        ingresos REAL,
        gastos REAL,
        ganancias REAL,
        cambio REAL,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario)
    )
    """
    )

    # Relación viaje-producto
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS viaje_productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_viaje INTEGER,
        id_producto INTEGER,
        FOREIGN KEY(id_viaje) REFERENCES viajes(id_viaje),
        FOREIGN KEY(id_producto) REFERENCES productos(id_producto)
    )
    """
    )

    conn.commit()
    conn.close()


# ==========================
# CLASE USUARIO
# ==========================


class Usuario:
    def __init__(
        self,
        nombre,
        username,
        password,
        categoria,
        telefono="",
        correo="",
        direccion="",
    ):
        self.nombre = nombre
        self.username = username
        self.password = password
        self.telefono = telefono
        self.categoria = categoria
        self.correo = correo
        self.direccion = direccion

    def guardar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO usuarios (nombre, username, password, categoria, telefono, correo, direccion)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                self.nombre,
                self.username,
                self.password,
                self.categoria,
                self.telefono,
                self.correo,
                self.direccion,
            ),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def login(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE username=? AND password=?",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()
        return user


# ==========================
# CLASE PRODUCTO
# ==========================


class Producto:
    def __init__(self, nombre, detalles, tipo, personal_shopper, destino, id_cliente):
        self.nombre = nombre
        self.detalles = detalles
        self.tipo = tipo
        self.personal_shopper = personal_shopper
        self.destino = destino
        self.id_cliente = id_cliente

    def guardar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO productos (nombre, detalles, tipo, personal_shopper, destino, id_cliente)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                self.nombre,
                self.detalles,
                self.tipo,
                self.personal_shopper,
                self.destino,
                self.id_cliente,
            ),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def aprobar_producto(id_producto):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET estado='aprobado' WHERE id_producto=?", (id_producto,)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def marcar_pendiente_peso(id_producto):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET estado='pendiente_peso' WHERE id_producto=?",
            (id_producto,),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def asignar_peso(id_producto, peso):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET peso=?, estado='listo' WHERE id_producto=?",
            (peso, id_producto),
        )
        conn.commit()
        conn.close()


# ==========================
# CLASE VIAJE
# ==========================


class Viaje:
    def __init__(self, id_usuario, detalles, cambio):
        self.id_usuario = id_usuario
        self.fecha = datetime.now().strftime("%Y-%m-%d")
        self.detalles = detalles
        self.ingresos = 0
        self.gastos = 0
        self.ganancias = 0
        self.cambio = cambio

    def guardar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO viajes (id_usuario, fecha, detalles, ingresos, gastos, ganancias, cambio)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                self.id_usuario,
                self.fecha,
                self.detalles,
                self.ingresos,
                self.gastos,
                self.ganancias,
                self.cambio,
            ),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def agregar_producto(id_viaje, id_producto):
        conn = get_connection()
        cursor = conn.cursor()

        # Verificar estado aprobado
        cursor.execute(
            "SELECT estado FROM productos WHERE id_producto=?", (id_producto,)
        )
        estado = cursor.fetchone()

        if estado and estado[0] == "aprobado":
            cursor.execute(
                "INSERT INTO viaje_productos (id_viaje, id_producto) VALUES (?, ?)",
                (id_viaje, id_producto),
            )

            cursor.execute(
                "UPDATE productos SET estado='pendiente_peso' WHERE id_producto=?",
                (id_producto,),
            )

            conn.commit()
        else:
            print("Producto no aprobado")

        conn.close()


# ==========================
# MAIN TEST
# ==========================

if __name__ == "__main__":
    if not os.path.exists(DB_NAME):
        print("Creando base de datos...")
    init_db()

    print("Sistema listo.")
    # caso de prueba: crear usuario, agregar producto, aprobar producto, agregar a viaje
    # crear usuario (nombre, username, password, categoria, telefono, correo, direccion)
    admin = Usuario(
        "Admin User",
        "admin",
        "adminpass",
        "administrador",
        "555-0000",
        "info@glezdelivery.com",
        "",
    )
    user1 = Usuario(
        "Juan Perez",
        "juanp",
        "password123",
        "555-4567",
        "cliente_regular",
        "juanp@example.com",
        "Calle Principal 123",
    )
    user2 = Usuario(
        "Maria Gomez",
        "mariag",
        "password456",
        "555-7890",
        "cliente_vip",
        "mariag@example.com",
        "Avenida Secundaria 456",
    )
    admin.guardar()
    user1.guardar()
    user2.guardar()

    # agregar producto (nombre, detalles, tipo, personal_shopper, destino, id_cliente)
    producto1 = Producto(
        "Zapatillas Deportivas",
        "Zapatillas para correr, talla 42",
        "calzado",
        None,
        "Lima, Perú",
        2,
    )
    producto2 = Producto(
        "Reloj Inteligente",
        "Reloj con GPS y monitor de ritmo cardíaco",
        "tecnología",
        None,
        "Lima, Perú",
        3,
    )

    producto1.guardar()
    producto2.guardar()

    # aprobar producto
    Producto.aprobar_producto(1)
    Producto.aprobar_producto(2)
    # agregar a viaje (id_viaje, id_producto)
    viaje1 = Viaje(2, "Viaje de marzo 2026", 3.5)
    viaje1.guardar()
    Viaje.agregar_producto(1, 1)
    Viaje.agregar_producto(1, 2)
    # asignar peso al producto
    Producto.asignar_peso(1, 2.5)
    Producto.asignar_peso(2, 1.8)

    # mostrar resultados
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print("Usuarios:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM productos")
    print("\nProductos:")
    for row in cursor.fetchall():
        print(row)
    # imrpimir viajes y productos asociados relacionando los id con los nombres de los cliente y de los productos
    cursor.execute(
        """ SELECT v.id_viaje, u.nombre, p.nombre, v.fecha, v.detalles
            FROM viajes v
            JOIN usuarios u ON v.id_usuario = u.id_usuario
            JOIN viaje_productos vp ON v.id_viaje = vp.id_viaje
            JOIN productos p ON vp.id_producto = p.id_producto
        """
    )
    print("\nViajes y productos asociados:")
    for row in cursor.fetchall():
        print(row)
    conn.close()
