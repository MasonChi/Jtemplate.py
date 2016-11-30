#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
mysql connection config
"""
import pymysql

from mysql import table_property


def mysql_config(mysql_param):
    """
    query database's definition.
    :param mysql_param: mysql parameter instance, it include:
        table: database's table name
        host: database's connection host
        username: database's connection username
        password: database's connection password
        database: database name
        port: database port
        charset: database charset(default is utf8)
    :return: table properties list
    """
    conn = pymysql.connect(host=mysql_param.host, user=mysql_param.username, passwd=mysql_param.password,
                           db=mysql_param.database, port=mysql_param.port, charset=mysql_param.charset)

    cursor = conn.cursor()

    table_column_sql = "SHOW FULL COLUMNS FROM {0}.{1}".format(mysql_param.database, mysql_param.table)

    result = []
    try:
        cursor.execute(table_column_sql)
        result = cursor.fetchall()
    except:
        print("Error: query table column failed")
    column_list = []
    for e in result:
        data = table_property.TableProperty(e[0], e[1], e[8])
        column_list.append(data)

    cursor.close()
    conn.close()
    return column_list
