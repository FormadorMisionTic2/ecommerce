import psycopg2


class Rol:
    cant_roles = 0

    def __init__(self, cant_roles):
        self.cant_roles = cant_roles

    def __init__(self):
        pass

    def list_roles(self):

        roles = []  # Variable dentro del metodo list_roles

        conn = psycopg2.connect(
            host="ec2-54-156-60-12.compute-1.amazonaws.com",
            database="d7h26gu4vod24h",
            user="viutzficoufmpa",
            password="c0d7d5f9df168feff12131f3352922560adbb1250a644651b2cc28442e06de2b"
        )

        cur = conn.cursor()

        cur.execute('SELECT * FROM rol')

        roles = cur.fetchall()
        self.cant_roles = len(roles)

        cur.close()

        return roles
