import tkinter.messagebox
from tkinter import ttk

import pymysql

'''
mysql常规操作封装
'''


class Mysql:
    def __init__(self, db_conf_dict, database):
        db = None
        if database is None:
            try:
                db = pymysql.connect(host=db_conf_dict.get('url'),
                                 port=int(db_conf_dict.get('port')),
                                 user=db_conf_dict.get('username'),
                                 password=db_conf_dict.get('password'))

            except Exception as e :
                tkinter.messagebox.showerror(title="error", message=str(e))
        else:
            try:
                db = pymysql.connect(host=db_conf_dict.get('url'),
                                 port=int(db_conf_dict.get('port')),
                                 user=db_conf_dict.get('username'),
                                 password=db_conf_dict.get('password'),
                                 database=database)

            except Exception as e :
                tkinter.messagebox.showerror(title="error", message=str(e))

        if db is not None:
            self.cursor = db.cursor()
        else:
            self.cursor = None

    # 获得sql游标
    def get_cursor(self):
        return self.cursor

    # 执行sql查询
    def query(self, sql):
        if self.cursor is not None:
            self.cursor.execute("{sql};".format(sql=sql))
            rows_data = self.cursor.fetchall()
            return rows_data

    # 根据表名获取表所有的数据
    def list(self, table_name):
        if self.cursor is not None:
            self.cursor.execute("select * from {table};".format(table=table_name))
            rows_data = self.cursor.fetchall()
            return rows_data

    # 根据表名分页查询数据
    def page(self, table_name, page=1, size=1000):
        if self.cursor is not None:
            offset_start = (page - 1) * size
            offset_end = offset_start + size
            self.cursor.execute("select * from {table} limit {offset_start},{offset_end}};".format(table=table_name,
                                                                                                   offset_start=offset_start,
                                                                                                   offset_end=offset_end))
            rows_data = self.cursor.fetchall()
            return rows_data

    # 获取连接下的数据库数据
    def show_databases(self):
        if self.cursor is not None:
            self.cursor.execute('show databases;')
            db_data = self.cursor.fetchall()
            return db_data

    # 获取连接下指定数据库下的表数据
    def show_tables(self):
        if self.cursor is not None:
            self.cursor.execute('show tables;')
            table_data = self.cursor.fetchall()
            return table_data

    # 获取连接下指定数据库下指定表的字段
    def show_columns(self, table_name):
        if self.cursor is not None:
            self.cursor.execute(
                "select COLUMN_NAME from information_schema.COLUMNS where table_name = '{table}';".format(
                    table=table_name))
            return self.cursor.fetchall()
