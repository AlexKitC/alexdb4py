from tkinter import ttk, END, HORIZONTAL, VERTICAL, RIGHT, Y, BOTTOM, X

'''
表格数据渲染
'''


class Table:
    def __init__(self, root, columns, data_list):
        """
        :type columns: list
        """
        self.data_table = ttk.Treeview(master=root,
                                       columns=columns,
                                       show="headings")

        # 表头
        for item in columns:
            self.data_table.heading(item, text=item)
        # 表数据渲染
        for item in data_list:
            self.data_table.insert(parent='', index=END, values=item)

        scroll_bar_tree_x = ttk.Scrollbar(master=self.data_table, orient=HORIZONTAL, command=self.data_table.xview)
        self.data_table.configure(xscrollcommand=scroll_bar_tree_x.set)
        scroll_bar_tree_x.pack(side=BOTTOM, fill=X)

        scroll_bar_tree_y = ttk.Scrollbar(master=self.data_table, orient=VERTICAL, command=self.data_table.yview)
        self.data_table.configure(yscrollcommand=scroll_bar_tree_y.set)
        scroll_bar_tree_y.pack(side=RIGHT, fill=Y)

    def get_instance(self):
        self.data_table.place(x=300, y=64, relwidth=0.7, relheight=0.9)
        return self.data_table
