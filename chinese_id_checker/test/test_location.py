#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29
# @Author  : Lin Luo/ Bruce Liu
# @Email   : 15869300264@163.com
from unittest import TestCase

from ..checker.location import Location


class TestLocation(TestCase):
    def test_output_from_csv(self):
        obj = Location()
        obj.output_json_file_from_csv('D:\projects\chinese_id_checker\data_source\data_source_200327.csv')

    def test_bak_file(self):
        obj = Location()
        obj.bak_file()

    def test_roll_back_file(self):
        obj = Location()
        obj.roll_back()

    def test_add_info(self):
        obj = Location()
        self.assertTrue(obj.add_info('999999','xxx','xxx','xxx'))

    def test_remove_info(self):
        obj = Location()
        self.assertTrue(obj.remove_info('999999'))