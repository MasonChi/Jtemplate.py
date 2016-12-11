#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The file yate.py is used to build java class or java interface template.
This file can product the java entity bean file, java entity example file in spring-mvc project,
java service interface file,java service class file that implements the service interface
and it also can product java mybatis's mapper interface and mapper.xml configuration file.
"""
import time
from string import Template

from mysql import mysql_config
from mysql import table_property_list

from util import resutil

"""
Current Date
"""
DATEFORMAT = '%Y/%m/%d'
now = time.strftime(DATEFORMAT, time.localtime())


def _build_entity_import(attrs):
    """
    build entity class's import package.
    for example:
        import java.math.BigDecimal;
        import java.math.BigInteger;
        import java.util.Date;
    :return:
    """
    global packages
    try:
        # add the imported packages to set
        packageset = set()
        for attr in attrs:
            with open(resutil.resource_path("../templates/entity.package.template")) as packagef:
                package_text = packagef.read()
            package = Template(package_text)
            if attr.field_type == 'BigDecimal':
                text = package.substitute(package_class='java.math.BigDecimal')
            elif attr.field_type == 'BigInteger':
                text = package.substitute(package_class='java.math.BigInteger')
            elif attr.field_type == 'Date':
                text = package.substitute(package_class='java.util.Date')
            else:
                text = ''
            packageset.add(text)

            # convert set to string
            packages = ''
            for e in packageset:
                packages += e
        return packages
    except IOError as error:
        print("File error :" + str(error))


def _build_entity_property(attrs):
    """
    build entity property item,
    include define entity's a property.
    for example:
        @Column
        private BigDecimal total; // totalAmount
    :return:
    """
    try:
        properties = ''
        for attr in attrs:
            with open(resutil.resource_path("../templates/entity.property.template")) as propertyf:
                property_text = propertyf.read()
            prop = Template(property_text)
            annotation = ''
            if attr.field_comment != '':
                annotation = '// ' + attr.field_comment
            properties += prop.substitute(property_type=attr.field_type, property_name=attr.field,
                                          property_annotation=annotation)
        return properties
    except IOError as error:
        print("File error :" + str(error))


def _build_entity_setter_getter(attrs):
    """
    build entity property item,
    include define entity's getter/setter functions.
    for example:
        public BigDecimal getTotal() {
            return total;
        }

        public void setTotal(BigDecimal total) {
            this.total = total;
        }
    :return:
    """
    try:
        setter_getter = ''
        for attr in attrs:
            with open(resutil.resource_path("../templates/entity.getset.template")) as setgetf:
                setget_text = setgetf.read()
            setget = Template(setget_text)
            setter_getter += setget.substitute(property_type=attr.field_type, property_name=attr.field,
                                               property_name_capitalize=(attr.field[0:1].upper() + attr.field[1:]))
        return setter_getter
    except IOError as error:
        print("File error :" + str(error))


def product_entity(mysql_param, project_name, entity_name, creator=None, create_date=now):
    """
    Build entity class by entity.template
    :param mysql_param:
    :param project_name:
    :param entity_name:
    :param creator:
    :param create_date:
    :return:
    """
    # get table's properties
    # (include column's type, column's name, column's comment)
    field_list = mysql_config.mysql_config(mysql_param)
    attrs = table_property_list.TablePropertyList(field_list).java_field_type

    # build entity's import package, properties and setter()/getter() functions.
    entity_import = _build_entity_import(attrs)
    entity_property = _build_entity_property(attrs)
    entity_getset = _build_entity_setter_getter(attrs)
    try:
        with open(resutil.resource_path("../templates/entity.template")) as entityf:
            entity_text = entityf.read()
        entity = Template(entity_text)
        return entity.substitute(project=project_name, table=mysql_param.table, entity=entity_name,
                                 import_package=entity_import, property=entity_property, getter_setter=entity_getset,
                                 creator=creator, create_date=create_date)
    except IOError as error:
        print("File error :" + str(error))


def product_example(project_name, entity_name, creator=None, create_date=now):
    """
    Build example class by entity.template
    """
    try:
        with open(resutil.resource_path("../templates/example.template")) as examplef:
            example_text = examplef.read()
        example = Template(example_text)
        return example.substitute(project=project_name, entity=entity_name, creator=creator, create_date=create_date)
    except IOError as error:
        print("File error :" + str(error))


def product_service(project_name, entity_name, creator=None, create_date=now):
    """
    Build service interface by service.template
    """
    try:
        with open(resutil.resource_path("../templates/service.template")) as servicef:
            service_text = servicef.read()
        service = Template(service_text)
        return service.substitute(project=project_name, entity=entity_name, creator=creator, create_date=create_date)
    except IOError as error:
        print("File error :" + str(error))


def product_service_impl(project_name, entity_name, creator=None, create_date=now):
    """
    Build service implement class by service.template
    :param project_name: project name
    :param entity_name: entity name
    :param creator: author
    :param create_date: file create date
    :return: service class content
    """
    try:
        with open(resutil.resource_path("../templates/service.impl.template")) as serviceimplf:
            service_impl_text = serviceimplf.read()
        service_impl = Template(service_impl_text)
        return service_impl.substitute(project=project_name, entity=entity_name,
                                       entity_first_lowercase=entity_name[0:1].lower() + entity_name[1:],
                                       creator=creator, create_date=create_date)
    except IOError as error:
        print("File error :" + str(error))


def product_mapper(project_name, entity_name, creator=None, create_date=now):
    """
    Build mapper interface by service.template
    :param project_name:
    :param entity_name:
    :param creator:
    :param create_date:
    :return:
    """
    try:
        with open(resutil.resource_path("../templates/mapper.template")) as mapperf:
            mapper_text = mapperf.read()
        mapper = Template(mapper_text)
        return mapper.substitute(project=project_name, entity=entity_name, creator=creator, create_date=create_date)
    except IOError as error:
        print("File error :" + str(error))


def product_mapper_xml(project_name, entity_name, table):
    """
    Build mapper interface xml config by service.template
    """
    try:
        with open(resutil.resource_path("../templates/mapper.xml.template")) as mapperxmlf:
            mapper_xml_text = mapperxmlf.read()
        mapper_xml = Template(mapper_xml_text)
        return mapper_xml.substitute(project=project_name, entity=entity_name, table=table)
    except IOError as error:
        print("File error :" + str(error))
