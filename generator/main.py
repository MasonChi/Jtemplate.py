#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Run the main module and generate the class files.
"""
from generator.yate import *

HOST = 'localhost'
USERNAME = 'root'
PASSWORD = '123456'
PORT = 801

PROJECT = 'project'
AUTHOR = 'child'

DATABASE = 'project'
TABLE = 'user'
ENTITY = 'User'

FILE_PATH = 'C:\\test\\'

if __name__ == '__main__':
    param = MySQLParam(TABLE, HOST, USERNAME, PASSWORD, DATABASE, PORT)

    print('start generate entity class file...')
    with open(FILE_PATH + ENTITY + '.java', 'w') as f:
        f.write(product_entity(param, PROJECT, ENTITY, AUTHOR, now))

    print('start generate example interface file...')
    with open(FILE_PATH + ENTITY + 'Example.java', 'w') as f:
        f.write(product_example(PROJECT, ENTITY, AUTHOR, now))

    print('start generate service interface file...')
    with open(FILE_PATH + ENTITY + 'Service.java', 'w') as f:
        f.write(product_service(PROJECT, ENTITY, AUTHOR, now))

    print('start generate service class file...')
    with open(FILE_PATH + ENTITY + 'ServiceImpl.java', 'w') as f:
        f.write(product_service_impl(PROJECT, ENTITY, AUTHOR, now))

    print('start generate mapper interface file...')
    with open(FILE_PATH + ENTITY + 'Mapper.java', 'w') as f:
        f.write(product_mapper(PROJECT, ENTITY, AUTHOR, now))

    print('start generate mapper.xml configuration file...')
    with open(FILE_PATH + ENTITY + 'Mapper.xml', 'w') as f:
        f.write(product_mapper_xml(PROJECT, ENTITY, TABLE))