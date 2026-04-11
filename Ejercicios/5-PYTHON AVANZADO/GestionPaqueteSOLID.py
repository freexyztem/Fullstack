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
from abc import ABC, abstractmethod

DB_NAME = "envios.db"

# ==========================
# DB CONNECTION (SRP)
# ==========================


class Database:
    @staticmethod
    def get_connection():
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def init_db():
        conn = Database.get_connection()
        cursor = conn.cursor()

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
            direccion TEXT
        )
        """
        )

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
            estado TEXT
        )
        """
        )

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
            cambio REAL
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS viaje_productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_viaje INTEGER,
            id_producto INTEGER
        )
        """
        )

        conn.commit()
        conn.close()


# ==========================
# REPOSITORIES (SRP + DIP)
# ==========================


class UsuarioRepository:
    def guardar(self, usuario):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO usuarios (nombre, username, password, telefono, categoria, correo, direccion)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                usuario.nombre,
                usuario.username,
                usuario.password,
                usuario.telefono,
                usuario.categoria,
                usuario.correo,
                usuario.direccion,
            ),
        )
        conn.commit()
        conn.close()


class ProductoRepository:
    def guardar(self, producto):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO productos (nombre, detalles, tipo, personal_shopper, destino, id_cliente, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                producto.nombre,
                producto.detalles,
                producto.tipo,
                producto.personal_shopper,
                producto.destino,
                producto.id_cliente,
                producto.estado,
            ),
        )
        conn.commit()
        conn.close()

    def actualizar_estado(self, id_producto, estado):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET estado=? WHERE id_producto=?", (estado, id_producto)
        )
        conn.commit()
        conn.close()


class ViajeRepository:
    def guardar(self, viaje):
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
        INSERT INTO viajes (id_usuario, fecha, detalles, ingresos, gastos, ganancias, cambio)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                viaje.id_usuario,
                viaje.fecha,
                viaje.detalles,
                viaje.ingresos,
                viaje.gastos,
                viaje.ganancias,
                viaje.cambio,
            ),
        )
        conn.commit()
        conn.close()


# ==========================
# DOMAIN MODELS (OCP + LSP)
# ==========================


class Usuario:
    def __init__(
        self, nombre, username, password, telefono, categoria, correo, direccion
    ):
        self.nombre = nombre
        self.username = username
        self.password = password
        self.telefono = telefono
        self.categoria = categoria
        self.correo = correo
        self.direccion = direccion


class Cliente(Usuario, ABC):

    @abstractmethod
    def calcular_precio(self, peso):
        pass

    @abstractmethod
    def puede_reutilizar(self):
        pass


class ClienteRegular(Cliente):
    def calcular_precio(self, peso):
        return peso * 10

    def puede_reutilizar(self):
        return False


class ClienteMiembro(Cliente):
    def calcular_precio(self, peso):
        return peso * 8

    def puede_reutilizar(self):
        return True


class ClienteVIP(Cliente):
    def calcular_precio(self, peso):
        return peso * 6

    def puede_reutilizar(self):
        return True


class Producto:
    def __init__(self, nombre, detalles, tipo, personal_shopper, destino, id_cliente):
        self.nombre = nombre
        self.detalles = detalles
        self.tipo = tipo
        self.personal_shopper = personal_shopper
        self.destino = destino
        self.id_cliente = id_cliente
        self.estado = "pendiente"


class Viaje:
    def __init__(self, id_usuario, detalles, cambio):
        self.id_usuario = id_usuario
        self.fecha = datetime.now().strftime("%Y-%m-%d")
        self.detalles = detalles
        self.ingresos = 0
        self.gastos = 0
        self.ganancias = 0
        self.cambio = cambio


# ==========================
# SERVICES (SRP + OCP)
# ==========================


class ProductoService:
    def __init__(self, repo):
        self.repo = repo

    def aprobar_producto(self, id_producto):
        self.repo.actualizar_estado(id_producto, "aprobado")

    def marcar_pendiente_peso(self, id_producto):
        self.repo.actualizar_estado(id_producto, "pendiente_peso")


class ViajeService:
    def __init__(self, producto_repo):
        self.producto_repo = producto_repo

    def agregar_producto(self, id_viaje, id_producto):
        conn = Database.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT estado FROM productos WHERE id_producto=?", (id_producto,)
        )
        estado = cursor.fetchone()

        if estado and estado[0] == "aprobado":
            cursor.execute(
                "INSERT INTO viaje_productos (id_viaje, id_producto) VALUES (?, ?)",
                (id_viaje, id_producto),
            )

            self.producto_repo.actualizar_estado(id_producto, "pendiente_peso")
            conn.commit()
        else:
            print("Producto no aprobado")

        conn.close()


# ==========================
# FACTORY (DIP)
# ==========================


def crear_cliente(tipo, *args):
    if tipo == "regular":
        return ClienteRegular(*args)
    elif tipo == "miembro":
        return ClienteMiembro(*args)
    elif tipo == "vip":
        return ClienteVIP(*args)
    else:
        raise ValueError("Tipo de cliente inválido")


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":
    if not os.path.exists(DB_NAME):
        print("Creando base de datos...")

    Database.init_db()

    print("Sistema con SOLID listo.")
