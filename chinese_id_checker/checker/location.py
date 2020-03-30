#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29
# @Author  : Lin Luo/ Bruce Liu
# @Email   : 15869300264@163.com
import os
import shutil
from json import dump, load
from time import time

from .exceptions import InvalidFileTypeException, SourceFileLostException, FileNotFoundException, CICException

DIR_NAME = os.path.join(os.path.split(os.path.abspath(__file__))[0], '../data_source')
SOURCE_FILE_NAME = os.path.join(DIR_NAME, 'location.json')
BAK_DIR_NAME = os.path.join(DIR_NAME, 'bak')
BAK_FILE_NAME = os.path.join(BAK_DIR_NAME, 'location.json.bak')


class Location(object):
    @staticmethod
    def bak_file(raise_exception: bool = False) -> bool:
        """
        back up the location source file
        :param raise_exception:
        :return:
        """
        if not os.path.exists(BAK_DIR_NAME):
            os.mkdir(BAK_DIR_NAME)
        if os.path.isfile(SOURCE_FILE_NAME):
            shutil.copyfile(SOURCE_FILE_NAME, BAK_FILE_NAME)
            shutil.copyfile(SOURCE_FILE_NAME, '%s.%d' % (BAK_FILE_NAME, time()))
            return True
        else:
            if raise_exception:
                raise SourceFileLostException(SOURCE_FILE_NAME)
            return False

    @staticmethod
    def roll_back(file_name: str = None) -> bool:
        """
        use the back up file to roll back
        :param file_name: roll back file name, if None then use the default file
        :return:
        """
        if file_name is None:
            file_name = BAK_FILE_NAME
        if os.path.isfile(file_name):
            shutil.copyfile(file_name, SOURCE_FILE_NAME)
            return True
        return False

    @classmethod
    def add_info(cls, id_code: str, province: str, city: str, district: str, update_if_exist: bool = False,
                 is_bak: bool = False) -> bool:
        """
        add an information to json file,
        :param id_code: a string object and the length is 6
        :param province:
        :param city:
        :param district:
        :param update_if_exist: if False and the the id_code is existed will return False
        :param is_bak: if True will back up file when update
        :return:
        """
        if len(id_code) != 6:
            return False
        if is_bak:
            cls.bak_file()
        data = {}
        with open(SOURCE_FILE_NAME, encoding='utf-8') as r:
            data = load(r)
            if data.get(id_code) is None or update_if_exist:
                data[id_code] = [province, city, district]
            else:
                return False
        with open(SOURCE_FILE_NAME, 'w', encoding='utf-8') as f:
            dump(data, f, ensure_ascii=False)
        return True

    @classmethod
    def remove_info(cls, id_code, is_bak: bool = False) -> bool:
        """
        remove info by id_code
        :param id_code:
        :param is_bak:
        :return:
        """
        if is_bak:
            cls.bak_file()
        data = {}
        with open(SOURCE_FILE_NAME, encoding='utf-8') as r:
            data = load(r)
            if data.get(id_code) is not None:
                data.pop(id_code)
            else:
                return False
        with open(SOURCE_FILE_NAME, 'w', encoding='utf-8') as f:
            dump(data, f, ensure_ascii=False)
        return True

    @classmethod
    def output_json_file_from_csv(cls, csv_path: str, output_path: str = None, with_head: bool = True,
                                  columns: iter = (4, 1, 2, 3)) -> None:
        """
        create the location json file from csv
        we provide a example located in folder named data_source
        :param csv_path: the csv you provide
        :param output_path: output file path, if the value is None, then will output to the default path
        :param with_head: True means the csv file has a head line, and it will be ignored
        :param columns: an iter obj is required, the first item is location_code column,
                the second item is province name, the third item is city name and the forth item is district name
        :return:
        """
        if len(columns) != 4:
            raise CICException('the length of columns  should be 4')
        file_name, file_type = os.path.splitext(csv_path)
        if file_type != '.csv':
            raise InvalidFileTypeException('a csv file is required!')
        if not os.path.isfile(csv_path):
            raise FileNotFoundException(csv_path)
        if output_path is None:
            output_path = SOURCE_FILE_NAME
            cls.bak_file()
        res = {}
        with open(csv_path, encoding='utf-8') as f:
            if with_head:
                lines = f.readlines()[1:]
            else:
                lines = f.readlines()
            for line in lines:
                tmp = line.strip('\n').strip('\r').split(',')
                res[tmp[columns[0]]] = [tmp[columns[1]], tmp[columns[2]], tmp[columns[3]]]
        with open(output_path, 'w', encoding='utf-8') as f:
            dump(res, f, ensure_ascii=False)

    @staticmethod
    def get_info(file_path: str = None) -> dict:
        """
        get the location information for file_path
        :param file_path:
        :return:
        """
        if file_path is None:
            file_path = SOURCE_FILE_NAME
        if not os.path.isfile(file_path):
            raise FileNotFoundException(file_path)
        data = {}
        with open(file_path, encoding='utf-8') as f:
            data = load(f)
        return data

    @staticmethod
    def clean_bak_file() -> bool:
        """

        :return:
        """
        pass
