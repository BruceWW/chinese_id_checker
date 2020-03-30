#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29
# @Author  : Lin Luo/ Bruce Liu
# @Email   : 15869300264@163.com


class CICException(BaseException):
    def __init__(self, msg: str):
        self._msg = msg

    def __str__(self):
        return '%s, %s' % (self.__class__.__name__, self._msg)


class InvalidIdStringLengthException(CICException):
    pass


class InvalidIdStringCharException(CICException):
    pass


class InvalidBirthdayException(CICException):
    pass


class InvalidFileTypeException(CICException):
    pass


class FileNotFoundException(CICException):
    def __init__(self, msg):
        self._msg = 'file %s not found' % msg


class SourceFileLostException(CICException):
    def __init__(self, msg):
        self._msg = 'source file %s lost' % msg


class UnknownIdException(CICException):
    pass
