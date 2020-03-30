#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29
# @Author  : Lin Luo/ Bruce Liu
# @Email   : 15869300264@163.com
from unittest import TestCase

from ..checker.chinese_id_checker import ChineseIdChecker
from ..checker.exceptions import UnknownIdException


class TestChineseId(TestCase):
    def test_chinese_id_correct(self):
        obj = ChineseIdChecker('110101199511114295')
        self.assertTrue(obj.check())
        self.assertEqual('1995-11-11', obj.get_birthday())
        self.assertEqual('北京市,北京市,东城区', obj.get_location())
        self.assertEqual('北京市', obj.get_province())
        self.assertEqual('北京市', obj.get_city())
        self.assertEqual('东城区', obj.get_district())
        self.assertEqual(1, obj.get_sex())
        self.assertEqual(24, obj.get_age())

    def test_chinese_id_error(self):
        obj = ChineseIdChecker('110101199511114291')
        self.assertFalse(obj.check())
        self.assertEqual('1995-11-11', obj.get_birthday())
        self.assertEqual('北京市,北京市,东城区', obj.get_location())
        self.assertEqual('北京市', obj.get_province())
        self.assertEqual('北京市', obj.get_city())
        self.assertEqual('东城区', obj.get_district())
        self.assertEqual(1, obj.get_sex())
        self.assertEqual(24, obj.get_age())

    def test_chinese_id_error_location(self):
        obj = ChineseIdChecker('910101199511114291')
        self.assertFalse(obj.check())
        self.assertEqual('1995-11-11', obj.get_birthday())
        try:
            obj.get_location()
            self.assertEqual('the id should raise error', '')
        except UnknownIdException:
            pass
        self.assertEqual(1, obj.get_sex())
        self.assertEqual(24, obj.get_age())
