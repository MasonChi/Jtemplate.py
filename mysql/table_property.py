#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Table's Column Property:
    field : column's name
    file_type : column's property type
    file_comment : column's commentary
"""


class TableProperty:
    def __init__(self, field, field_type=None, field_comment=None):
        self.field = field
        self.field_type = field_type
        self.field_comment = field_comment
