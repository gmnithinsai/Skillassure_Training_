import psycopg2

db = {
    'host' : 'localhost',
    'user' : 'gmnithinsai',
    'password' : '2599',
}

def connect(database):
    conn = None
    try:
        db['database'] = database
        conn = psycopg2.connect(**db)
        return conn
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

def close_connection(conn, cur):
    conn.close()
    cur.close()
