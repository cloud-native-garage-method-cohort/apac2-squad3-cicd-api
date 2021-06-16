import psycopg2

class Model(object):
    def __init__(self):
        pass

    def _exec(self, sql):
        conn=psycopg2.connect(database="testdb",user="postgres",password="postgres",host="172.21.106.94",port="5432")
        cur=conn.cursor()

        cur.execute(sql)
        results=cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()

        return results
