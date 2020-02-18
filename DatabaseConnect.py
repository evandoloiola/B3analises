#import pymysql
#conexão


# class connect:
    
#     def __init__(self):
#         try:
#             self.conn = pymysql.connect(
#             host='185.201.10.16',
#             user='webizyco_finantial',
#             password='#Atualidade#13',
#             db='webizyco_finantial')
#             cursor = conn.cursor()
#             return cursor

#         except:
#             print("Erro ao conectar banco de dados :(")
#     def __del__(self):
#         print("Conexão finalizada!")
#         del self
import sys
import pymysql
import logging
import pandas as pd

class Database:
    """Database connection class."""

    def __init__(self):
        self.host = '185.201.10.16'
        self.username = 'webizyco_finantial'
        self.password = '#Atualidade#13'
        self.port = '3306'
        self.dbname = 'webizyco_finantial'
        self.conn = None

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(self.host,
                                            user=self.username,
                                            passwd=self.password,
                                            db=self.dbname,
                                            connect_timeout=5)
        except pymysql.MySQLError as e:
            logging.error(e)
            sys.exit()
        finally:
            logging.info('Connection opened successfully.')

    def run_query(self, query):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                if 'SELECT' in query:
                    records = []
                    cur.execute(query)
                    result = cur.fetchall()
                    for row in result:
                        records.append(row)
                    cur.close()
                    return records
                else:
                    result = cur.execute(query)
                    self.conn.commit()
                    affected = f"{cur.rowcount} rows affected."
                    cur.close()
                    return affected
        except pymysql.MySQLError as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logging.info('Database connection closed.')

    def read_sql(self, query):
        """Execute SQL query with pandas."""
        try:
            self.open_connection()
            if 'SELECT' in query:
                result =[]
                result = pd.read_sql(query,self.conn)
                return result
            else:
                logging.info('for read_sql use only "SELECT" query.')
        except pymysql.MySQLError as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logging.info('Database connection closed.')