import psycopg2
import logging
from settings import Settings

logging.basicConfig(level=logging.INFO)


class DB_Worker:
    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=Settings.DATABASE,
            user=Settings.USER,
            password=Settings.PASSWORD,
            host=Settings.HOST,
            port=Settings.PORT,
        )
        return self

    def __exit__(self, *args):
        self.conn.close()

    def insert(self, table='', object_=None):
        keys = ', '.join([x for x in object_.keys()])
        values = ''
        for index, val in enumerate(object_.values()):
            if type(val) == str:
                values += f'\'{val}\', ' if index < len(object_.values()) - 1 else f'\'{val}\' '
            else:
                values += f'{val}, ' if index < len(object_.values()) - 1 else f'{val} '

            sql_text = f'INSERT INTO {table}({keys}) VALUES ({values})'

            cursor = self.conn.cursor()
            try:
                cursor.execute(sql_text)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()





