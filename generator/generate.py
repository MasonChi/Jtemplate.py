#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run the main module and generate the class files.
"""
import os

from generator import pos
from generator.yate import *

HOST = 'localhost'
USERNAME = 'root'
PASSWORD = '123456'
PORT = 401

PROJECT = 'project'
PROJECT_PATH = r'C:\Apps\project'
AUTHOR = 'child'

DATABASE = 'project'
TABLE = 'user'
ENTITY = 'User'

FILE_PATH = r'C:\test'
# If ${AUTO_PATH} is true, it will be automatically generated to the appropriate directory,
# otherwise, generated into the ${FILE_PATH} directory
AUTO_PATH = False

if __name__ == '__main__':
    param = MySQLParam(TABLE, HOST, USERNAME, PASSWORD, DATABASE, PORT)

    if AUTO_PATH is False:
        entity_path = FILE_PATH
        example_path = FILE_PATH
        service_path = FILE_PATH
        service_impl_path = FILE_PATH
        mapper_path = FILE_PATH
        mapper_xml_path = FILE_PATH
    else:
        # If you want to automatically generate the corresponding directory, please set the package name
        entity_path = pos.search_package(PROJECT_PATH, 'com.miz.sinnis.entity', 'entity')
        example_path = pos.search_package(PROJECT_PATH, 'com.miz.sinnis.entity.example', 'entity')
        service_path = pos.search_package(PROJECT_PATH, 'com.miz.sinnis.service.atom', 'service-atom')
        service_impl_path = pos.search_package(PROJECT_PATH, 'com.miz.sinnis.service.atom.impl', 'service-atom')
        mapper_path = pos.search_package(PROJECT_PATH, 'com.miz.sinnis.dao.mapper', 'dao')
        mapper_xml_path = pos.search_package(PROJECT_PATH, 'com.miz.sinnis.dao.mapper', 'dao',
                                             filter='src' + os.sep + 'main' + os.sep + 'resources')

    entity_path = os.path.join(entity_path, ENTITY) + '.java'
    example_path = os.path.join(example_path, ENTITY) + 'Example.java'
    service_path = os.path.join(service_path, ENTITY) + 'Service.java'
    service_impl_path = os.path.join(service_impl_path, ENTITY) + 'ServiceImpl.java'
    mapper_path = os.path.join(mapper_path, ENTITY) + 'Mapper.java'
    mapper_xml_path = os.path.join(mapper_xml_path, ENTITY) + 'Mapper.xml'

    # generate class file
    print('start generate entity class file...')
    with open(entity_path, 'w') as f:
        f.write(product_entity(param, PROJECT, ENTITY, AUTHOR, now))

    print('start generate example interface file...')
    with open(example_path, 'w') as f:
        f.write(product_example(PROJECT, ENTITY, AUTHOR, now))

    print('start generate service interface file...')
    with open(service_path, 'w') as f:
        f.write(product_service(PROJECT, ENTITY, AUTHOR, now))

    print('start generate service class file...')
    with open(service_impl_path, 'w') as f:
        f.write(product_service_impl(PROJECT, ENTITY, AUTHOR, now))

    print('start generate mapper interface file...')
    with open(mapper_path, 'w') as f:
        f.write(product_mapper(PROJECT, ENTITY, AUTHOR, now))

    print('start generate mapper.xml configuration file...')
    with open(mapper_xml_path, 'w') as f:
        f.write(product_mapper_xml(PROJECT, ENTITY, TABLE))
