#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
文件/文件路径操作及查询
"""
import os

__path_list = []


def search(path, word):
    """
    查询path目录下word相同文件夹名的目录绝对路径
    :param path: 查询的目录
    :param word: 目录名
    :return: 绝对路径list
    """
    for x in os.listdir(path):
        fp = os.path.join(path, x)
        if x == word:
            __path_list.append(os.path.abspath(fp))
        else:
            if os.path.isdir(fp):
                search(fp, word)

    return __path_list


def search_package(project_path, package, module=None, filter='src\\main\\java'):
    """
    查询包路径
    :param project_path:项目路径
    :param package:使用模板生成的类文件需要存放的包名
    :param module:使用模板生成的类文件的模块名, 模块名默认为None，若没有制定，则采用项目名作为模块名
    :param filter:过滤条件(需过滤掉测试目录下,target目录下的同名package目录,默认为'src\\main\\java')
    :return:
    """
    if module is None:
        module = os.path.basename(project_path)
    # 将包名转化为目录
    package_dir = package.replace('.', os.sep)

    # 截取表名的最后目录名
    basename = os.path.basename(package_dir)

    # 查询项目目录下包含basename目录名的所有的目录路径
    # 过滤出包含有package的所有目录路径,并且包含module
    search(project_path, basename)
    filterpath = []
    for e in __path_list:

        if package_dir in e \
                and module in e \
                and filter in e:
            filterpath.append(e)
    if filterpath.__len__() > 1:
        raise Exception('查询到生成文件的路径不唯一,请检查提供的参数是否有误')
    return filterpath[0]


if __name__ == '__main__':
    print(search('C:\\Apps\\sinnis', 'service-atom'))

    path = search_package('C:\\Apps\\sinnis', 'com.miz.sinnis.service.atom', 'service-atom')
    print(path)
