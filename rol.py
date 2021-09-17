import psycopg2
import conn


class Rol:
    id = 0
    nombre = ''
    descripcion = ''
    cant_roles = 0

    conn = psycopg2.connect(
        host="ec2-54-156-60-12.compute-1.amazonaws.com",
        database="d7h26gu4vod24h",
        user="viutzficoufmpa",
        password="c0d7d5f9df168feff12131f3352922560adbb1250a644651b2cc28442e06de2b"
    )

    cur = conn.cursor()

    def __init__(self, cant_roles):
        self.cant_roles = cant_roles

    def __init__(self):
        pass

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __init__(self, nombre):
        self.nombre = nombre

    def list_roles(self):

        roles = []  # Variable dentro del metodo list_roles
        self.cur.execute('SELECT * FROM rol')

        roles = self.cur.fetchall()

        self.cur.close()

        return roles

    def create(self):
        try:
            self.cur.execute(
                "INSERT INTO rol(nombre,descripcion) VALUES (%s,%s)", (self.nombre, self.descripcion))
            self.conn.commit()
        except Exception:
            print("Error inserting")
        finally:
            self.cur.close()
            self.conn.close()

    def delete(self):
        try:
            self.cur.execute('DELETE FROM rol WHERE nombre=%s', (self.nombre,))
            self.conn.commit()
        finally:
            self.cur.close()
            self.conn.close()

    def get_nombre(self):
        try:

            self.cur.execute(
                'SELECT * FROM rol WHERE nombre=%s', (self.nombre,))

            rol = self.cur.fetchone()
            self.id = rol[0]
            self.nombre = rol[1]
            self.descripcion = rol[2]
        finally:
            self.cur.close()
            self.conn.close()
