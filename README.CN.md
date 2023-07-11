## alexdb

##### [中文](./README.CN.md)｜[英文](./README.md)



##### 要求

1. Python3.9+(需包含 tcl/tk)
2. pymysql (操作mysql需要)
3. PIL (图像处理需要)
4. Pyinstaller (打包需要)

##### 截图示例

![](/Users/alex/PycharmProjects/alexdb/example.png)

##### 关于

Navicat是一款非常优秀的数据库管理工具，alexDB借鉴了它非常多优秀的设计和操作方式，使用纯~~java的openjfx~~python的tkinter开发了一款免费，开源的数据库管理工具替代品



##### 打包 

举例(MacOS)

```shell
pyinstaller -D -y -w --noconsole -i icon/logo.png --name alexdb main.py && cp -r icon/ dist/alexdb.app/Contents/MacOS/icon
```

