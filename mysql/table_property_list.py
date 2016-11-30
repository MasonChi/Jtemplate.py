#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Table's column property list
"""

from mysql import mysql_type


class TablePropertyList(list):
    def __init__(self, table_property=[]):
        """
        init function of TablePropertyList
        :param table_property: table's property list
        """
        list.__init__([])
        self.extend(table_property)

    @staticmethod
    def get_simple_field_type(field_type):
        """
        处理列的属性.
        例:
        将int(10) 转化为int
        将decimal(10,2) 转化为decimal
        """
        if '(' in field_type:
            simple_field_type = field_type[0:field_type.index('(')]
        else:
            return field_type
        return simple_field_type

    @staticmethod
    def mysql_type_2_java_type(field_type):
        """
        根据table表的简单类型字段定义(如field = userId, field_type = int, field_comment = '用户id')
        转换为java中定义的类型定义
        :return: java中定义的类型定义数组
        """
        database_type = field_type.upper()
        if database_type in mysql_type.STRING_TYPE:
            java_type = 'String'
        elif database_type in mysql_type.INT_TYPE:
            java_type = 'Integer'
        elif database_type in mysql_type.LONG_TYPE:
            java_type = 'Long'
        elif database_type in mysql_type.BIGINT_TYPE:
            java_type = 'BigInteger'
        elif database_type in mysql_type.FLOAT_TYPE:
            java_type = 'Float'
        elif database_type in mysql_type.DOUBLE_TYPE:
            java_type = 'Double'
        elif database_type in mysql_type.DECIMAL_TYPE:
            java_type = 'BigDecimal'
        elif database_type in mysql_type.DATE_TYPE:
            java_type = 'Date'
        else:
            java_type = 'String'
        return java_type

    @property
    def simple_field_type(self):
        """
        获取包含简单类型的table表属性字典
        :return: table表属性的字典
        """
        for e in self:
            e.field_type = self.get_simple_field_type(e.field_type)
        return self

    @property
    def java_field_type(self):
        for e in self.simple_field_type:
            e.field_type = self.mysql_type_2_java_type(e.field_type)
        return self
