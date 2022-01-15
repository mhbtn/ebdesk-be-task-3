import sqlite3

def conn():
    with sqlite3.connect("youtube.db") as conn:
        return conn

def select(query, conn):
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

        # make output as dictionary
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))

        return results

def insert(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    data = [{
        'message': 'Successful insert data',
    }]

    return data

def delete(query, conn, id):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return [{
        "message" : "Successful delete data with id {}".format(id)
    }]

def update(query, conn, id, data):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return [{
        "message" : "Successful update data with id {}".format(id),
        "result" : data
    }]

def search(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    # make output as dictionary
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    return results