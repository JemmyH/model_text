# _*_ coding:utf-8 _*_
# __author__: 'JemmyH'
import pymysql




def show_database():
    conn = pymysql.Connect(host="127.0.0.1", port=3306, user='hujiaming', passwd='123456', charset='utf8')
    cursor = conn.cursor()
    print(str(cursor.execute("show databases;")) + "个数据库")
    print(cursor.fetchall())


def create_database(database_name):
    conn = pymysql.Connect(host="127.0.0.1", port=3306, user='hujiaming', passwd='123456', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("create database If Not Exists {0};".format(database_name))
    cursor.execute("ALTER DATABASE {0} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci".format(database_name))
    conn.commit()
    print("添加数据库{0}成功".format(database_name))


def drop_database(database_name):
    conn = pymysql.Connect(host="127.0.0.1", port=3306, user='hujiaming', passwd='123456', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("drop database if exists {0};".format(database_name))
    conn.commit()
    print("删除数据库{0}成功".format(database_name))


def execute_sql(db_name, sql):
    # cursor.execute("use {0};{1};".format(db_name, sql))
    conn = pymysql.Connect(host="127.0.0.1", port=3306, user='hujiaming', passwd='123456', charset='utf8',db='{0}'.format(db_name))
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)
    # print(db)
    print("操作成功")


if __name__ == '__main__':
    # show_database()
    # create_database("python_test")
    # drop_database("python_test")
    execute_sql("hujiaming", "select * from jobbole;")
