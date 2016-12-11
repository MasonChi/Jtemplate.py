#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
读取资源文件
"""
import os
import sys


def resource_path(relative_path):
    """定义一个读取相对路径的函数"""
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
