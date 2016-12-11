#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run the main module and generate the class files.
"""
import os
import pickle

from generator.yate import *
from mysql import mysql_param
from util import resutil


class Generate:
    def __init__(self, host, port, username, password, database, table, entity, author, project, file_path):
        """
        init param
        """
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__database = database
        self.__table = table
        self.__entity = entity
        self.__author = author
        self.__project = project
        self.__file_path = file_path

        self.param = mysql_param.MySQLParam(table, host, username, password, database, port)

    @staticmethod
    def put_to_store(input_param):
        """
        store params
        :return:
        """
        params = dict()
        params["host"] = input_param.__host
        params["port"] = input_param.__port
        params["username"] = input_param.__username
        params["password"] = input_param.__password
        params["database"] = input_param.__database
        params["table"] = input_param.__table
        params["entity"] = input_param.__entity
        params["author"] = input_param.__author
        params["project"] = input_param.__project
        params["file_path"] = input_param.__file_path
        try:
            with open(resutil.resource_path('../resources/input.pickle'), 'wb') as f:
                pickle.dump(params, f)
        except IOError as ioerr:
            print('File error (put_and_store): ' + str(ioerr))
        return params

    @staticmethod
    def get_from_store():
        """
        get params
        :return:
        """
        params = {}
        try:
            with open(resutil.resource_path('../resources/input.pickle'), 'rb') as f:
                params = pickle.load(f)
        except IOError as ioerr:
            print('File error (get_from_store): ' + str(ioerr))
        return params

    def gen(self):
        """
        generate files
        :return:
        """
        # store params
        Generate.put_to_store(self)

        # if self.auto_path == 0:
        #     entity_path = self.file_path
        #     example_path = self.file_path
        #     service_path = self.file_path
        #     service_impl_path = self.file_path
        #     mapper_path = self.file_path
        #     mapper_xml_path = self.file_path
        # else:
        #     # If you want to automatically generate the corresponding directory, please set the package name
        #     entity_path = pos.search_package(self.project_path, 'com.miz.sinnis.entity', 'entity')
        #     example_path = pos.search_package(self.project_path, 'com.miz.sinnis.entity.example', 'entity')
        #     service_path = pos.search_package(self.project_path, 'com.miz.sinnis.service.atom', 'service-atom')
        #     service_impl_path = pos.search_package(self.project_path, 'com.miz.sinnis.service.atom.impl',
        #                                            'service-atom')
        #     mapper_path = pos.search_package(self.project_path, 'com.miz.sinnis.dao.mapper', 'dao')
        #     mapper_xml_path = pos.search_package(self.project_path, 'com.miz.sinnis.dao.mapper', 'dao',
        #                                          filter='src' + os.sep + 'main' + os.sep + 'resources')

        entity_path = self.__file_path
        example_path = self.__file_path
        service_path = self.__file_path
        service_impl_path = self.__file_path
        mapper_path = self.__file_path
        mapper_xml_path = self.__file_path

        entity_path = os.path.join(entity_path, self.__entity) + '.java'
        example_path = os.path.join(example_path, self.__entity) + 'Example.java'
        service_path = os.path.join(service_path, self.__entity) + 'Service.java'
        service_impl_path = os.path.join(service_impl_path, self.__entity) + 'ServiceImpl.java'
        mapper_path = os.path.join(mapper_path, self.__entity) + 'Mapper.java'
        mapper_xml_path = os.path.join(mapper_xml_path, self.__entity) + 'Mapper.xml'

        # generate class file
        print('start generate entity class file...')
        with open(entity_path, 'w') as f:
            f.write(product_entity(self.param, self.__project, self.__entity, self.__author, now))

        print('start generate example interface file...')
        with open(example_path, 'w') as f:
            f.write(product_example(self.__project, self.__entity, self.__author, now))

        print('start generate service interface file...')
        with open(service_path, 'w') as f:
            f.write(product_service(self.__project, self.__entity, self.__author, now))

        print('start generate service class file...')
        with open(service_impl_path, 'w') as f:
            f.write(product_service_impl(self.__project, self.__entity, self.__author, now))

        print('start generate mapper interface file...')
        with open(mapper_path, 'w') as f:
            f.write(product_mapper(self.__project, self.__entity, self.__author, now))

        print('start generate mapper.xml configuration file...')
        with open(mapper_xml_path, 'w') as f:
            f.write(product_mapper_xml(self.__project, self.__entity, self.param.table))
