import pymysql

'''
mysql常规操作封装
'''


class Mysql:
    def __init__(self, db_conf_dict, database):
        if database is None:
            db = pymysql.connect(host=db_conf_dict.get('url'),
                                 port=int(db_conf_dict.get('port')),
                                 user=db_conf_dict.get('username'),
                                 password=db_conf_dict.get('password'))
        else:
            db = pymysql.connect(host=db_conf_dict.get('url'),
                                 port=int(db_conf_dict.get('port')),
                                 user=db_conf_dict.get('username'),
                                 password=db_conf_dict.get('password'),
                                 database=database)

        self.cursor = db.cursor()

    # 获得sql游标
    def get_cursor(self):
        return self.cursor

    # 执行sql查询
    def query(self, sql):
        self.cursor.execute("{sql};".format(sql=sql))
        rows_data = self.cursor.fetchall()
        return rows_data

    # 获取连接下的数据库数据
    def show_databases(self):
        self.cursor.execute('show databases;')
        db_data = self.cursor.fetchall()
        return db_data

    # 获取连接下指定数据库下的表数据
    def show_tables(self):
        self.cursor.execute('show tables;')
        table_data = self.cursor.fetchall()
        return table_data

    # 获取连接下指定数据库下指定表的字段
    def show_columns(self, table_name):
        self.cursor.execute(
            "select COLUMN_NAME from information_schema.COLUMNS where table_name = '{table}';".format(
                table=table_name))
        return self.cursor.fetchall()
