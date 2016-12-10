#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run the main module and generate the class files.
"""
import os

from generator import pos
from generator.yate import *
from mysql import mysql_param


# HOST = 'localhost'
# USERNAME = 'root'
# PASSWORD = '123456'
# PORT = 401
#
# PROJECT = 'project'
# PROJECT_PATH = r'C:\Apps\project'
# AUTHOR = 'child'
#
# DATABASE = 'project'
# TABLE = 'user'
# ENTITY = 'User'
#
# FILE_PATH = r'C:\test'
# # If ${AUTO_PATH} is true, it will be automatically generated to the appropriate directory,
# # otherwise, generated into the ${FILE_PATH} directory
# AUTO_PATH = False


class Generate:
    def __init__(self, host, port, username, password, database, table,
                 entity, author, project, file_path, auto_path,
                 project_path):
        # print(host + ',' + port + ',' + username + ',' + password + ',' + database + ',' + table + ','
        #       + entity + ',' + author + ',' + project + ',' + file_path + ',' + auto_path + ',' + project_path)
        self.param = mysql_param.MySQLParam(table, host, username, password, database, port)
        self.entity = entity
        self.author = author
        self.project = project
        self.file_path = file_path
        self.auto_path = auto_path
        self.project_path = project_path

    def gen(self):
        if self.auto_path == 0:
            entity_path = self.file_path
            example_path = self.file_path
            service_path = self.file_path
            service_impl_path = self.file_path
            mapper_path = self.file_path
            mapper_xml_path = self.file_path
        else:
            # If you want to automatically generate the corresponding directory, please set the package name
            entity_path = pos.search_package(self.project_path, 'com.miz.sinnis.entity', 'entity')
            example_path = pos.search_package(self.project_path, 'com.miz.sinnis.entity.example', 'entity')
            service_path = pos.search_package(self.project_path, 'com.miz.sinnis.service.atom', 'service-atom')
            service_impl_path = pos.search_package(self.project_path, 'com.miz.sinnis.service.atom.impl',
                                                   'service-atom')
            mapper_path = pos.search_package(self.project_path, 'com.miz.sinnis.dao.mapper', 'dao')
            mapper_xml_path = pos.search_package(self.project_path, 'com.miz.sinnis.dao.mapper', 'dao',
                                                 filter='src' + os.sep + 'main' + os.sep + 'resources')

        entity_path = os.path.join(entity_path, self.entity) + '.java'
        example_path = os.path.join(example_path, self.entity) + 'Example.java'
        service_path = os.path.join(service_path, self.entity) + 'Service.java'
        service_impl_path = os.path.join(service_impl_path, self.entity) + 'ServiceImpl.java'
        mapper_path = os.path.join(mapper_path, self.entity) + 'Mapper.java'
        mapper_xml_path = os.path.join(mapper_xml_path, self.entity) + 'Mapper.xml'

        # generate class file
        print('start generate entity class file...')
        with open(entity_path, 'w') as f:
            f.write(product_entity(self.param, self.project, self.entity, self.author, now))

        print('start generate example interface file...')
        with open(example_path, 'w') as f:
            f.write(product_example(self.project, self.entity, self.author, now))

        print('start generate service interface file...')
        with open(service_path, 'w') as f:
            f.write(product_service(self.project, self.entity, self.author, now))

        print('start generate service class file...')
        with open(service_impl_path, 'w') as f:
            f.write(product_service_impl(self.project, self.entity, self.author, now))

        print('start generate mapper interface file...')
        with open(mapper_path, 'w') as f:
            f.write(product_mapper(self.project, self.entity, self.author, now))

        print('start generate mapper.xml configuration file...')
        with open(mapper_xml_path, 'w') as f:
            f.write(product_mapper_xml(self.project, self.entity, self.param.table))
