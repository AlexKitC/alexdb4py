#!/usr/local/bin/python3
import os.path
# -D 文件夹打包
# -F 单文件打包
# -w 不显示命令行
# --noconsole 不显示console
# pyinstaller -D -y -w --noconsole --name alexkit main.py

import tkinter as tk
from tkinter.messagebox import *

root = tk.Tk()
gui_width = 960
gui_height = 640
win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()

gui_offset_x = int((win_width - gui_width) / 2)
gui_offset_y = int((win_height - gui_height) / 2)
gui_offset = '{w}x{h}+{x}+{y}'.format(w=gui_width, h=gui_height, x=gui_offset_x, y=gui_offset_y)

new_conn_offset = '{w}x{h}+{x}+{y}'.format(w=640, h=480, x=gui_offset_x + 160, y=gui_offset_y + 80)


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

    new_query_btn = tk.Button(master=root, text="new connection")
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
            bool_save_or_cancel = askokcancel(title="需要确认", message='当前配置名为：{name}已经存在！是否覆盖?'.format(name=name))
            if bool_save_or_cancel:
                # 覆盖则需要删除再写入
                pass
            else:
                # 不覆盖则关闭窗口
                cur_view.destroy()
        else:
            # 不存在则存储配置文件
            conf_fd = open(file='local.conf'.format(name=name), mode='x')
            conf_fd.write("{name}\r\n{url}\r\n{port}\r\n{username}\r\n{password}".format(
                name=name,
                url=url,
                port=port,
                username=username,
                password=password
            ))
            conf_fd.close()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 渲染窗体
    render_gui("alexkit")
