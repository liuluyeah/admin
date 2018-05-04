# admin
django+mongodb+hui 实现的后台管理系统

运行环境：windows10 + pytcharm + anaconda3 

实验前：需要在本地安装mongodb，并建立test数据库，以及在models.py创建相关表格

下载后将admin改名为myadmin, 并将static压缩文件解压到当前文件夹下

# mongodb 基本操作

连接远程mongodb: mongo ip地址：端口号

查看数据库： show dbs;

使用数据库： use test;

查看数据表： show collections;

删除goods表中address字段: db.goods.update({},{$unset:{'address':''}},false, true)
