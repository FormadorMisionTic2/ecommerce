import psycopg2


def create_connection():

    conn = psycopg2.connect(
        host="ec2-54-156-60-12.compute-1.amazonaws.com",
        database="d7h26gu4vod24h",
        user="viutzficoufmpa",
        password="c0d7d5f9df168feff12131f3352922560adbb1250a644651b2cc28442e06de2b"
    )
    cur = conn.cursor()

    return cur
