#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
define a MySQL param setting class
"""


class MySQLParam:
    def __init__(self, table, host, username, password, database, port, charset='UTF8'):
        """
        :param table: database's table name
        :param host: database's connection host
        :param username: database's connection username
        :param password: database's connection password
        :param database: database name
        :param port: database port
        :param charset: database charset(default is utf8)
        :return: MySQL Instance
        """
        self.table = table
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
