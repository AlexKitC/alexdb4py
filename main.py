#!/usr/local/bin/python3
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter.constants import END, BOTTOM, HORIZONTAL, VERTICAL, RIGHT, X, Y
from tkinter.messagebox import *

from PIL import Image, ImageTk

from component.Table import Table
from util.Conf import Conf
from util.Mysql import Mysql

# -D 文件夹打包
# -F 单文件打包
# -w 不显示命令行
# --noconsole 不显示console

# pyinstaller -D -y -w --noconsole -i icon/logo.png --name alexdb main.py && cp -r icon/ dist/alexdb.app/Contents/MacOS/icon

root = tk.Tk()
gui_width = 960
gui_height = 640
win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()

gui_offset_x = int((win_width - gui_width) / 2)
gui_offset_y = int((win_height - gui_height) / 2)
gui_offset = '{w}x{h}+{x}+{y}'.format(w=gui_width, h=gui_height, x=gui_offset_x, y=gui_offset_y)

new_conn_offset = '{w}x{h}+{x}+{y}'.format(w=640, h=480, x=gui_offset_x + 160, y=gui_offset_y + 80)

# 连接信息的tree
conn_tree = ttk.Treeview(master=root)
# 连接信息tree的滚动条
scroll_bar_tree_x = tk.Scrollbar(master=conn_tree, orient=HORIZONTAL, command=conn_tree.xview)
conn_tree.configure(xscrollcommand=scroll_bar_tree_x.set)
scroll_bar_tree_x.pack(side=BOTTOM, fill=X)

scroll_bar_tree_y = tk.Scrollbar(master=conn_tree, orient=VERTICAL, command=conn_tree.yview)
conn_tree.configure(yscrollcommand=scroll_bar_tree_y.set)
scroll_bar_tree_y.pack(side=RIGHT, fill=Y)

# 连接的tree conf级别 item的映射  conf_name->conf_item
conn_tree_conf_dict = {}
# 连接的tree db级别item的映射 db_name->db_item
conn_tree_db_dict = {}
# 连接的tree table级别item的映射 table_name->table_item
conn_tree_table_dict = {}

# 当前使用的连接文件
current_selected_conn_file = ''
# 当前选中的db
current_selected_db = ''

# 当前conf包含的db_list
conf_db_list = {}
# 当前db包含的table_list
db_table_list = {}
# 当前table包含的column_list
table_column_list = {}

# 当前执行文件路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# icon
icon_mysql = ImageTk.PhotoImage(Image.open('{path}/icon/mysql.png'.format(path=cur_path)).resize((16, 16)))
icon_database = ImageTk.PhotoImage(Image.open('{path}/icon/database.png'.format(path=cur_path)).resize((12, 16)))
icon_table = ImageTk.PhotoImage(Image.open('{path}/icon/table.png'.format(path=cur_path)).resize((13, 13)))


# 渲染主窗体
def render_gui(name):
    root.title(name)
    root.geometry(gui_offset)

    # 渲染顶部功能按钮
    render_top_func_btn()

    root.mainloop()


# 渲染顶部功能按钮
def render_top_func_btn():
    new_conn_btn = tk.Button(master=root, text="new connection", command=render_new_conn)
    new_conn_btn.place(x=16, y=8)

    new_query_btn = tk.Button(master=root, text="new query")
    new_query_btn.place(x=160, y=8)


# 渲染新建连接视图
def render_new_conn():
    new_conn_view = tk.Toplevel()
    new_conn_view.title("new connection")
    new_conn_view.geometry(new_conn_offset)
    label_x = 48
    label_y = 32
    y_range = 48
    entry_x = 132
    # 新建连接具体输入
    label_name = tk.Label(master=new_conn_view, text="name")
    label_name.place(x=label_x, y=label_y)
    entry_name = tk.Entry(master=new_conn_view, width=32)
    entry_name.place(x=entry_x, y=label_y)

    label_url = tk.Label(master=new_conn_view, text="url")
    label_url.place(x=label_x, y=label_y + y_range * 1)
    entry_url = tk.Entry(master=new_conn_view, width=32)
    entry_url.place(x=entry_x, y=label_y + y_range * 1)

    label_port = tk.Label(master=new_conn_view, text="port")
    label_port.place(x=label_x, y=label_y + y_range * 2)
    entry_port = tk.Entry(master=new_conn_view, width=16)
    entry_port.place(x=entry_x, y=label_y + y_range * 2)

    label_username = tk.Label(master=new_conn_view, text="username")
    label_username.place(x=label_x, y=label_y + y_range * 3)
    entry_username = tk.Entry(master=new_conn_view, width=32)
    entry_username.place(x=entry_x, y=label_y + y_range * 3)

    label_pass = tk.Label(master=new_conn_view, text="password")
    label_pass.place(x=label_x, y=label_y + y_range * 4)
    entry_pass = tk.Entry(master=new_conn_view, width=32)
    entry_pass.place(x=entry_x, y=label_y + y_range * 4)

    # 测试连接按钮
    test_conn_btn = tk.Button(master=new_conn_view, text="test connection")
    test_conn_btn.place(x=label_x, y=label_y + y_range * 6)
    test_conn_label = tk.Label(master=new_conn_view, text="connection success !!!")
    test_conn_label.place(x=label_x + 138, y=label_y + y_range * 6 + 3)

    # 存储连接按钮
    save_conn_btn = tk.Button(master=new_conn_view,
                              text="save",
                              command=lambda: save_new_conn(
                                  cur_view=new_conn_view,
                                  name=entry_name.get(),
                                  url=entry_url.get(),
                                  port=entry_port.get(),
                                  username=entry_username.get(),
                                  password=entry_pass.get()))
    save_conn_btn.place(x=label_x, y=label_y + y_range * 8)

    # 返回按钮
    cancel_new_conn_btn = tk.Button(master=new_conn_view, text="cancel", command=lambda: new_conn_view.destroy())
    cancel_new_conn_btn.place(x=label_x + 96, y=label_y + y_range * 8)


# 存储新建连接
def save_new_conn(cur_view, name, url, port, username, password):
    if name == '':
        showwarning(title="warn", message="connection name can not be empty")
    elif url == '':
        showwarning(title="warn", message="connection url can not be empty")
    elif port == '':
        showwarning(title="warn", message="connection port can not be empty")
    elif username == '':
        showwarning(title="warn", message="connection username can not be empty")
    elif password == '':
        showwarning(title="warn", message="connection url can not be empty")
    else:
        # 根据name检测是否已经存在配置文件
        is_conf_file_exist = os.path.exists('./{fname}.conf'.format(fname=name))
        if is_conf_file_exist:
            # 如果存在当前配置文件提示是否需要更新覆盖
            bool_save_or_cancel = askokcancel(title="需要确认",
                                              message='当前配置名为：{name}已经存在！是否覆盖?'.format(name=name))
            if bool_save_or_cancel:
                # 覆盖则需要删除再写入
                pass
            else:
                # 不覆盖则关闭窗口
                cur_view.destroy()
        else:
            # 不存在则存储配置文件
            conf_fd = open(file='{path}/{name}.conf'.format(path=os.path.dirname(os.path.realpath(__file__)), name=name), mode='x')
            conf_fd.write("{name}\r\n{url}\r\n{port}\r\n{username}\r\n{password}".format(
                name=name,
                url=url,
                port=port,
                username=username,
                password=password
            ))
            conf_fd.close()
            cur_view.destroy()
            # 同时追加连接到treeview去
            conn_tree.insert(parent="", index=END, text=name, values=1)
            root.update()


# 读取存在的连接配置列表
def get_conf_list():
    target_list = []
    file_list = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    for file in file_list:
        if file.endswith('.conf'):
            target_list.append(file.replace(".conf", ''))

    return target_list


# 根据获取的配置文件列表渲染连接的treeview
def render_conn_tree():
    # 插入第一级：配置文件列表
    file_list = get_conf_list()
    for file in file_list:
        global icon_mysql
        top_level_tree_item = conn_tree.insert(parent='',
                                               index=END,
                                               text=file,
                                               image=icon_mysql,
                                               values=1)
        conn_tree_conf_dict[file] = top_level_tree_item
    # 绑定一个双击事件
    conn_tree.bind("<Double-1>", double_click_conf_name)
    conn_tree.place(x=16, y=48, relwidth=0.22, relheight=0.9)


# 双击连接名
def double_click_conf_name(event):
    global current_selected_conn_file
    e = event.widget
    iid = e.identify("item", event.x, event.y)
    clicked_item_name = e.item(iid, "text")
    level = e.item(iid, "values")[0]

    if level == '1':
        current_selected_conn_file = clicked_item_name

    db_conf_dict = Conf(current_selected_conn_file).read_conn_conf()
    global icon_database
    # 如果是最顶级则直接执行db连接
    if level == '1':

        db_data = Mysql(db_conf_dict, None).show_databases()
        parent = conn_tree_conf_dict.get(clicked_item_name)
        db_list = []

        # 追加database到父节点
        for db in db_data:
            if len(conf_db_list) == 0 or db[0] not in conf_db_list[clicked_item_name]:
                db_item = conn_tree.insert(parent=parent,
                                           index=END,
                                           text=db[0],
                                           image=icon_database,
                                           values=2)
                conn_tree_db_dict[db[0]] = db_item
                db_list.append(db[0])

        if len(db_list) > 0:
            conf_db_list[clicked_item_name] = db_list

        # table
    elif level == '2':
        global current_selected_db
        current_selected_db = clicked_item_name

        table_data = Mysql(db_conf_dict, current_selected_db).show_tables()
        parent = conn_tree_db_dict.get(current_selected_db)
        table_list = []
        global icon_table

        for table in table_data:
            if len(db_table_list) == 0 or (
                    current_selected_db not in db_table_list.keys() and table[0] not in db_table_list.get(
                current_selected_db)):
                table_item = conn_tree.insert(parent=parent,
                                              index=END,
                                              text=table[0],
                                              image=icon_table,
                                              values=3)
                conn_tree_table_dict[table[0]] = table_item
                table_list.append(table[0])
        if len(table_list) > 0:
            db_table_list[current_selected_db] = table_list

    elif level == '3':
        column_data = Mysql(db_conf_dict, current_selected_db).show_columns(clicked_item_name)
        # 当前表字段
        columns = []
        for item in column_data:
            columns.append(item[0])
        # 再获取表行数据
        table_rows_data = Mysql(db_conf_dict, current_selected_db).query(
            "select * from {table};".format(table=clicked_item_name))
        Table(root, columns, table_rows_data).get_instance()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    render_conn_tree()
    # 渲染窗体
    render_gui("alexdb")
