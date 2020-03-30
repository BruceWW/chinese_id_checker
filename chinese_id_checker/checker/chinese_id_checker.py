#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29
# @Author  : Lin Luo / Bruce Liu
# @Email   : 15869300264@163.com
from datetime import date

from chinese_id_checker.checker.location import Location, SOURCE_FILE_NAME
from .exceptions import InvalidIdStringLengthException, InvalidIdStringCharException, InvalidBirthdayException, \
    UnknownIdException


class ChineseIdChecker(object):
    def __init__(self, id_str: str, location_file_path: str = None, location_load: bool = False, location_obj=Location):
        """
        the initial method
        simple usage
        chinese_id_obj = ChineseIdChecker('110101199511114295')
        pre load the location information
        chinese_id_obj = ChineseIdChecker('110101199511114295', location_load=True)
        use your location json file and pre load location information
        chinese_id_obj = ChineseIdChecker('110101199511114295', location_load=True, location_file_path='/usr/local/data/location.json')

        you may use the property to change the id_str
        chinese_id_obj.id_str = '110101199511116098'

        :param id_str: the chinese id str that need to be checked
        :param location_file_path: the path of location file template, if the value is None, then use the default file, json file is required
        :param location_load: if the value if True, the location info will be loaded when object is initialing and the data will be cached
        :param location_obj: the location object, please do not change the value
        """
        self._target_location = [(0, 7), (1, 9), (2, 10), (3, 5), (4, 8), (5, 4), (6, 2), (7, 1), (8, 6), (9, 3),
                                 (10, 7), (11, 9), (12, 10), (13, 5), (14, 8), (15, 4), (16, 2)]
        self._final_mapping = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        self._id_length_check(id_str)
        self._valid_key = None
        self._id_str = id_str
        self.check()
        if location_file_path is None:
            self._location_file_path = SOURCE_FILE_NAME
        self._location_load = location_load
        self._location_obj = location_obj
        if location_load:
            self._location_info = location_obj.get_info(self._location_file_path)
        else:
            self._location_info = {}

    @property
    def id_str(self) -> str:
        """
        get the id_str
        :return:
        """
        return self._id_str

    @id_str.setter
    def id_str(self, id_str: str) -> None:
        """
        reset the id_str
        and the valid_key will be reset
        :param id_str:
        :return:
        """
        self._id_str = id_str
        self._valid_key = None

    def _id_length_check(self, id_str: str) -> None:
        """
        check the length of id_str is valid or not
        :param id_str:
        :return:
        """
        if len(id_str) != 18:
            raise InvalidIdStringLengthException('the length of id_str should be 18!')
        try:
            int(id_str[:-1])
        except ValueError:
            raise InvalidIdStringCharException('id_str contains invalid char')
        if id_str[-1] not in self._final_mapping:
            raise InvalidIdStringCharException('the last char of id_str should be one of %s' % str(self._final_mapping))

    def check(self) -> bool:
        """
        check the id_str is valid or not
        :return: False means invalid
        """
        if self._valid_key is None:
            lack = sum([int(self._id_str[items[0]]) * items[1] for items in self._target_location]) % 11
            final_item = self._final_mapping[lack]
            if final_item == self._id_str[-1]:
                self._valid_key = True
            else:
                self._valid_key = False
        return self._valid_key

    def get_sex(self) -> int:
        """

        :return: 0 means female, 1 means male
        """
        return int(self._id_str[-2]) % 2

    def get_birthday(self, result_type: int = 0):
        """

        :param result_type: 0 return string with formatted 'yyyy-MM-dd'; 1 return date object
        :return:
        """
        try:
            year = int(self._id_str[6:10])
            month = int(self._id_str[10:12])
            day = int(self._id_str[12:14])
            if result_type == 1:
                return date(year=year, month=month, day=day)
            else:
                return '%d-%d-%d' % (year, month, day)
        except ValueError as e:
            raise InvalidBirthdayException(str(e))

    def get_age(self) -> int:
        """
        get the age
        :return:
        """
        birth_date = self.get_birthday(1)
        today = date.today()
        return (today - birth_date).days // 365

    def _get_info(self) -> list or None:
        """
        get location info
        :return:
        """
        if self._location_load:
            return self._location_info.get(self._id_str[:6])
        else:
            return self._location_obj.get_info(self._location_file_path).get(self.id_str[:6])

    def get_location(self) -> str:
        """
        get the location of this id_str
        :return: '[province],[city],[district]'
        """
        data = self._get_info()
        if data is None:
            raise UnknownIdException('can not get location')
        else:
            return ','.join(data)

    def get_province(self) -> str:
        """
        get the province of this id_str
        :return:
        """
        data = self._get_info()
        if data is None:
            raise UnknownIdException('can not get province')
        else:
            return data[0]

    def get_city(self) -> str:
        """
        get the city of this id_str
        :return:
        """
        data = self._get_info()
        if data is None:
            raise UnknownIdException('can not get city')
        else:
            return data[1]

    def get_district(self) -> str:
        """
        get the district of this id_str
        :return:
        """
        data = self._get_info()
        if data is None:
            raise UnknownIdException('can not get district')
        else:
            return data[2]
